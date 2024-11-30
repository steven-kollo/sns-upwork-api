import os
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("AI_KEY"))

job_description = "Looking for a BI specialist to build dashboards using Google Data Studio."
client_name = "John Doe"
skills = "Data visualization, Google Data Studio, Google Analytics, Python"
experience = "6 years of marketing data experience, 2 years as CMO."

prompt = f"""
You are an experienced freelancer. Write a professional and tailored proposal based on the following details:
- Job Description: {job_description}
- Client Name: {client_name}
- Skills: {skills}
- Experience: {experience}
The proposal should highlight why the client should hire you.
"""


response = client.chat.completions.create(
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

print(response.choices[0].message.content)
