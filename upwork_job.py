from upwork_demo import gen_job, UPWORK_DEMO
import requests, json, os
from openai import OpenAI

# freshsales_token = os.environ.get("FRESHSALES_KEY")
# openai_client = OpenAI(api_key=os.environ.get("AI_KEY"))

class UpworkClient:
    def __init__(self, job_posting):
        self.name = self.get_name(job_posting["client"]["freelancers_feedback"])
        self.timezone = job_posting["client"]["timezone"]
        self.country = job_posting["client"]["country"]
        self.payment_method_verified = job_posting["client"]["payment_method_verified"]
        self.phone_number_verified = job_posting["client"]["phone_number_verified"]
        try:
            self.avg_hourly_spend = job_posting["client"]["avg_hourly_spend"]
        except:
            self.avg_hourly_spend = None
        try:
            self.rate = job_posting["client"]["rate"]
        except:
            self.rate = None
        self.freelancers_feedback = job_posting["client"]["freelancers_feedback"]
        self.hires = job_posting["additionalInfo"]["clientNumberOfHiresOnCreate"]
        self.spent = job_posting["additionalInfo"]["clientTotalSpentOnCreate"]["rawValue"]

    def get_name(self, feedback):
        if len(feedback) > 0:
            lines = ""
            for msg in feedback:
                lines += f"- {msg}\n"
            prompt = f"""
            Here are few feedback messages from freelancers to the client:
            {lines}
            Sometimes they use client's name, sometimes don't: you need to read feedback masseges and find client's name. Respond with the client name only, if you fail to find the name, respond with "None"
            """

            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                response_format={
                    "type": "text"
                },
                temperature=1,
                max_tokens=400,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            return response.choices[0].message.content
        return "None"
    
class UpworkJob:
    def __init__(self, job):
        job_posting = job["data"]["jobPosting"]
        self.id = job_posting["id"]
        self.client = UpworkClient(job_posting) # TODO process other fields
        self.title = job_posting["content"]["title"]
        self.description = job_posting["content"]["description"]
        self.screening_questions = list(map(lambda x: x["question"], job_posting["contractorSelection"]["proposalRequirement"]["screeningQuestions"]))
        self.screening_answers = self.screening_questions_with_ai()
        self.required_english_proficiency = job_posting["contractorSelection"]["qualification"]["englishProficiency"]
        try:
            self.location_limit = job_posting["contractorSelection"]["location"]["countries"]
        except:
            self.location_limit = None
        try:
            self.location_limit = job_posting["contractorSelection"]["location"]["timezones"]
        except:
            self.timezones_limit = None
        try:
            self.required_has_portfolio = job_posting["contractorSelection"]["qualification"]["hasPortfolio"]
        except:
            self.required_has_portfolio = False
        try:
            self.required_rising_talent = job_posting["contractorSelection"]["qualification"]["risingTalent"]
        except:
            self.required_rising_talent = False
        try:
            self.required_job_success_score = job_posting["contractorSelection"]["qualification"]["jobSuccessScore"]
        except:
            self.required_job_success_score = 0
        
        self.process_skills(job_posting["classification"])
        self.process_contract_terms(job_posting["contractTerms"])
        self.min_connects = job_posting["min_connects"]
        self.url = job_posting["url"]
        self.response = self.respond_with_ai()
        self.add_job_to_crm()

    def process_skills(self, classification):
        self.required_skills =  [
            list(map(lambda x: x["prettyName"], classification["skills"])),
            list(map(lambda x: x["freeText"], classification["customSkills"])),
            list(map(lambda x: x["prettyName"], classification["additionalSkills"])),
            classification["customAdditionalSkills"]
        ]
    
    def process_contract_terms(self, contract_terms):
        self.required_experience_level = { "ENTRY_LEVEL": 1, "INTERMEDIATE": 2, "EXPERT": 3 }[contract_terms["experienceLevel"]]
        self.contract_type = contract_terms["contractType"]
        if self.contract_type == "HOURLY":
            self.duration = contract_terms["hourlyContractTerms"]["engagementDuration"]["weeks"]
            self.min_payment_rate = contract_terms["hourlyContractTerms"]["hourlyBudgetMin"]["rawValue"]
            self.max_payment_rate = contract_terms["hourlyContractTerms"]["hourlyBudgetMax"]["rawValue"]
            try:
                self.not_sure_duration = contract_terms["hourlyContractTerms"]["notSureProjectDuration"]
            except:
                self.not_sure_duration = False
            try:
                self.hourly_budget_type = contract_terms["hourlyContractTerms"]["hourlyBudgetType"]
            except:
                self.hourly_budget_type = "DEFAULT"
        else:
            self.duration = contract_terms["fixedPriceContractTerms"]["engagementDuration"]["weeks"]
            self.min_payment_rate = contract_terms["fixedPriceContractTerms"]["amount"]["rawValue"]
            self.max_payment_rate = contract_terms["fixedPriceContractTerms"]["maxAmount"]["rawValue"]
    
    def respond_with_ai(self):
        prompt = self.prepare_proposal_prompt()
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            response_format={
                "type": "text"
            },
            temperature=1,
            max_tokens=1230,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].message.content
    
    # TODO
    def screening_questions_with_ai(self):
        if len(self.screening_questions) > 0:
            questions = "===== Questions =====\n"
            for i in range(len(self.screening_questions)):
                questions += f"{i+1}. {self.screening_questions[i]}\n"
            return questions
        return None
        # TODO Build an advanced mechanism for answering based on my actuial experience. 
        # If I get a new question, I should answer myself and load it to the model
        if len(self.screening_questions) > 0:
            prompt = self.prepare_screening_questions_prompt()
            print(prompt)
            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                response_format={
                    "type": "text"
                },
                temperature=1,
                max_tokens=1230,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            return response.choices[0].message.content
        return None

    def prepare_screening_questions_prompt(self):
        questions = ""
        for i in range(len(self.screening_questions)):
            questions += f"{i+1}. {self.screening_questions[i]}\n"
        return f"""
You are an experienced Upwork freelancer. This is a job description: \n{self.description}\n\n
Answer the following questions based on the job description:\n{questions}\n
Respond with the following format:
1. Question 1
Answer for the 1st question
2. Question 2
Answer for the 2nd question
...
"""

    def prepare_proposal_prompt(self):
        name = f"  {self.client.name}," if self.client.name != "None" else ""
        skills = "\n- ".join(self.required_skills[0])+"\n- ".join(self.required_skills[1])+"\n- ".join(self.required_skills[2])+"\n- ".join(self.required_skills[3])
        if skills != "": skills = "- " + skills

        return f"""
You are an experienced Upwork freelancer. Write a professional and tailored proposal based on the following samples:
1) 
Hi{name}
I would love to be your freelance developer and help you execute your JavaScript task.

I have five years of experience building automation scripts, including Google Apps Scripts, Cloud functions, and more. Below, I’ve linked two samples that showcase my projects in a similar niche to your business. As you can see, I understand your workflow and know how to write code that works fast and simple enough to build another tools on top of it.

Would that work for your needs? Let me know if my qualifications meet your expectations, and we can set up a time for a 15 minutes zoom about your project in more detail.

Example #1 (link)
Example #2 (link)

Thanks,
Steven

2)
Hello{name}
If you need high-quality automation solutions for your business at an affordable price, I am the right developer for you! My goal with every app I build is to lead your team along their workflow — saving working hours and saving your money by the end of the day.

As you can see in my Upwork profile, I am a full-time freelancer and I have five years of experience writing apps and automation scripts just like yours. Linked below are two samples that demonstrate my ability to develop an excellent business environment with automation.

- Example #1 (link)
- Example #2 (link)

My current turnaround time for such task is two days. If my work aligns with what you need, can we set up a time for a 15 minutes zoom to discuss your goals for this project?

Best regards,
Steven

3)
Hello{name}

I’m a detail-driven developer who turns business needs into lightweight solutions for clients just like you. I enjoy working for various niches (e-com, healthcare, education, etc.). You can find examples of my past project on my Upwork profile, plus Example #1 (link) and Example #2 (link).

My experience has given me a deep understanding of business processes, ways to simplify them, help your team to save working hours and save money for you by the end of the day.

My rate is $100 for projects like this one, and I can have a finished solution delivered to you this week if you’re interested. Let’s set up a 15 minutes zoom to discuss your goals for this project!

– Steven.

Base the proposal on the Job Description:
{self.description}

Focus on skills like:
{skills}

The proposal should be 1000 characters long. You are not allowed to use any font styling (like bold), use "-" as a bullet-point 
"""
    
    # self.payment_method_verified = job_posting["client"]["payment_method_verified"]
    # self.phone_number_verified = job_posting["client"]["phone_number_verified"]
    # try:
    #     self.avg_hourly_spend = job_posting["client"]["avg_hourly_spend"]
    # except:
    #     self.avg_hourly_spend = None
    # self.freelancers_feedback = job_posting["client"]["freelancers_feedback"]
    # self.hires = job_posting["additionalInfo"]["clientNumberOfHiresOnCreate"]

    # job_posting = job["data"]["jobPosting"]
    # self.id = job_posting["id"]
    # self.client = UpworkClient(job_posting) # TODO process other fields
    # self.required_english_proficiency = job_posting["contractorSelection"]["qualification"]["englishProficiency"]
    # self.process_contract_terms(job_posting["contractTerms"])

    def add_job_to_crm(self):
        # TODO
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token token={freshsales_token}'
        }

        skills = self.skills_to_line()
        duration = self.pick_duration()
        location = self.pick_location()
        json_data = {
            "deal": {    
                "name": self.title,
                "amount": self.calculate_price(),
                "tags": [
                    str(self.contract_type)[0],
                    {1: "Jn", 2: "Md", 3: "Sr"}[self.required_experience_level],
                    duration,
                    location
                ],
                "custom_field": {
                    "cf_required_skills": skills,
                    "cf_connects_required": self.min_connects,
                    "cf_job_url": self.url,
                    "cf_client_name": self.client.name,
                    "cf_client_location": self.client.country,
                    "cf_client_spend": self.client.spent,
                    "cf_client_rate": self.client.rate,
                    "cf_client_time_zone": self.client.timezone
                }
            }
        }

        deal = requests.post(
            "https://sns1-782924923744476135.myfreshworks.com/crm/sales/api/deals/", 
            json=json_data, 
            headers=headers
        )

        requests.post(
            "https://sns1-782924923744476135.myfreshworks.com/crm/sales/api/notes/", 
            headers=headers,
            json={
                "note": {
                    "targetable_type":"Deal",
                    "targetable_id":deal.json()["deal"]["id"],
                    "description": "===== Skills =====\n" + str(skills).replace(";", "\n")
                }
            }
        )

        requests.post(
            "https://sns1-782924923744476135.myfreshworks.com/crm/sales/api/notes/", 
            headers=headers,
            json={
                "note": {
                    "targetable_type":"Deal",
                    "targetable_id":deal.json()["deal"]["id"],
                    "description": self.response
                }
            }
        )

        requests.post(
            "https://sns1-782924923744476135.myfreshworks.com/crm/sales/api/notes/", 
            headers=headers,
            json={
                "note": {
                    "targetable_type":"Deal",
                    "targetable_id":deal.json()["deal"]["id"],
                    "description": self.description
                }
            }
        )

        if self.screening_answers:
            requests.post(
                "https://sns1-782924923744476135.myfreshworks.com/crm/sales/api/notes/", 
                headers=headers,
                json={
                    "note": {
                        "targetable_type":"Deal",
                        "targetable_id":deal.json()["deal"]["id"],
                        "description": self.screening_answers
                    }
                }
            )
        
    def skills_to_line(self):
        skills = []
        skills_filtered = [var for var in self.required_skills if var]
        for i in skills_filtered:
            skills.append(";".join(i))
        return ";".join(skills)
    
    def pick_duration(self):
        if not self.duration:
            return "< 1 mos"
        if self.duration > 24:
            return "> 6 mos"
        elif self.duration > 12:
            return "4-6 mos"
        elif self.duration > 4:
            return "1-3 mos"
        return "< 1 mos"

    # TODO
    def pick_location(self):
        location = "WW"
        # if self.location_limit > 24:
        #     location = "WW"
        # elif self.location_limit > 12:
        #     location = "WW"
        # elif self.location_limit > 4:
        #     location = "WW"
        return location

    def calculate_price(self):
        if not self.min_payment_rate:
            return 0
        elif self.max_payment_rate:
            return (float(self.max_payment_rate) + float(self.min_payment_rate)) /  2
        else:
            return float(self.min_payment_rate)

# for n in range(len(UPWORK_DEMO)):
#     UpworkJob(gen_job(UPWORK_DEMO[n]))
UpworkJob(gen_job(UPWORK_DEMO[6]))

