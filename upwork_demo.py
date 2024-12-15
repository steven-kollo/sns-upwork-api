upwork_proposal_sample = [
    ""
]

upwork_job_sample = {
    "data": {
        "jobPosting": {
            "id": 4,
            # "info": JobPostingInfo,
            "visibility": "PUBLIC_INDEX",
            # "ownership": JobPostingOwnership,
            "content": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingContent
                "title": "abc123",
                "description": "xyz789"
            },
            # "attachment": [JobPostingAttachment],
            "classification": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingClassification
                "skills": [ # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-Skill
                    {
                        "prettyName": "API"
                    }
                ],
                "customSkills": [ # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-CustomJobPostSkill
                    {
                        "freeText": "MySQL"
                    }
                ],
                "additionalSkills": [ # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-Skill
                    {
                        "prettyName": "Python"
                    }
                ],
                "customAdditionalSkills": [
                    "Google Cloud"
                ]
            },
            # "segmentationData": JobPostingSegmentationData,
            "contractTerms": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingContractTerms
                "contractType": "HOURLY", # FIXED
                "personsToHire": 2,
                "experienceLevel": "ENTRY_LEVEL", # INTERMEDIATE # EXPERT
                "fixedPriceContractTerms": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-FixedPriceContractTerms
                    "amount": { "rawValue": "30.11" },
                    "maxAmount": { "rawValue": "30.11" },
                    "engagementDuration": { "weeks": 16 }
                },
                "hourlyContractTerms": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-HourlyContractTerms
                    "engagementDuration": { "weeks": 16 },
                    "engagementType": "FULL_TIME", # PART_TIME # AS_NEEDED # NOT_SURE
                    "notSureProjectDuration": False,
                    "hourlyBudgetType": "DEFAULT", # MANUAL # NOT_PROVIDED
                    "hourlyBudgetMin": 25.00,
                    "hourlyBudgetMax": 40.00
                }
            },
            "contractorSelection": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingContractorSelection
                "location": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingLocation
                    "countries": ["United States", "United Kingdom"],
                    "timezones": ["UTC-5"]
                },
                "proposalRequirement": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingProposalRequirements
                    "screeningQuestions": [ # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingQuestion
                        {
                            "question": "xyz789"
                        }
                    ]
                },
                "qualification": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingQualification
                    "englishProficiency": "ANY", # BASIC # CONVERSATIONAL # FLUENT # NATIVE
                    "hasPortfolio": False, 
                    "risingTalent": False,
                    "jobSuccessScore": 90,
                }
            },
            "additionalInfo": { # https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingAdditionalInfo
                "clientTotalSpentOnCreate": {
                    "rawValue": "110.00"
                },
                "clientNumberOfHiresOnCreate": 10
            }
            # "ptcInfo": JobPostingPtcInfo,
            # "proposalsStatistics": ProposalsStatistics,
            # "customFields": [JobPostingCustomFields]
        }
    }
}

# jobPosting QUERY EXAMPLE
# https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#query-jobPosting

# + Job's Title https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingContent
# + Job's Description https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingContent

# + Client's total spend https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingAdditionalInfo
# + Client's hires total https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingAdditionalInfo

# + Job's location limitation (or worldwide) https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingLocation
# + Job's timezone limitation https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingLocation

# + Screening questions (if exist) https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingProposalRequirements

# + Job Success Score https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingQualification
# + English level

# + Skills required for the job https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingClassification

# + Expertise level https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-JobPostingContractTerms
# + Job's hourly rate (min and max if exist) https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-HourlyContractTerms
# + Job's fixed price (if exists) https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-FixedPriceContractTerms
# + Job's duration

# Job's URL ??? = JOB_ID 
# Minimum connects to send a proposal
# Client's time zone https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-MarketPlaceJobSearchLocation
# Client's country https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-MarketPlaceJobSearchLocation
# Client's payment_method_verified https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-MarketplaceJobPosting
# Client's phone_number_verified https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-MarketplaceJobPosting
# Client's AVG hourly spend
# Client's rate
# Client's freelancers feedback https://www.upwork.com/developer/documentation/graphql/api/docs/index.html#definition-FreelancerFeedback

UPWORK_DEMO = [
    {
        "id": "021865975999087553775",
        "client": {
            "timezone": "UTC -6",
            "country": "United States",
            "payment_method_verified": True,
            "phone_number_verified": False,
            "avg_hourly_spend": "35.40",
            "rate": "4.1",
            "freelancers_feedback": [],
            "hires": 7,
            "spent": "60K"
        },
        "title": "Restaurant Inventory Supply Tracker",
        "description": "I am looking for someone to develop a dynamic google sheet that helps my restaurant managers track individual item inventory and purchases with starting and ending inventory, par levels, cost of item, purchases, waste, etc.\n\nIt should be dynamic enough so that the ending inventory from the last inventory count dynamically leads into the starting inventory count of the next inventory. It should be developed in Google sheets.\n\nIf you have developed something previously, please provide an example that can be used. I have 17 restaurant managers so there also needs to be an analysis tab as well so total purchases can be tracked.",
        "required_english_proficiency": "FLUENT",
        "screening_questions": [],
        "required_skills": [[],[],["Inventory Management", "Microsoft Excel", "Order Management", "Google Sheets", "Google Sheets Automation"],[]],
        "required_experience_level": "EXPERT",
        "contract_type": "FIXED",
        "min_payment_rate": "100.00",
        "max_payment_rate": None,
        "duration": None,
        "min_connects": "13",
        "url": "https://www.upwork.com/jobs/~021865975999087553775"
    },
    {
        "id": "021865956325868219631",
        "client": {
            "timezone": "UTC -8",
            "country": "United States",
            "payment_method_verified": True,
            "phone_number_verified": False,
            "avg_hourly_spend": "2.71",
            "rate": "4.7",
            "freelancers_feedback": [
                "Great client to work with",
                "I enjoyed working on this project. Thanks",
                "Great Working with Mike. Highly cooperative in working along with.", 
                "I would like to appreciate for quick payment process, quick reply for everything furthermore I enjoyed very much to serve this Client. I want say thanks and I love to serve you again!",
                "Not Interested for Communication",
                "I enjoyed working with Mike, although the experience could have been better if he had more patience, I wish him all the best with his site!",
                "It was a pleasure to work for Mike, Great Client looking to work for further projects in future.",
                "Thanks for the contract!"
            ],
            "hires": 15,
            "spent": "4.2K"
        },
        "title": "Google Sheet help",
        "description": "I have a google sheet that doesn't work transferring data to the third tab in a dashboard, but it works in excel",
        "required_english_proficiency": "FLUENT",
        "screening_questions": [],
        "required_skills": [["Google Docs", "Microsoft Excel", "Google Sheets", "AppSheet", "Google"],[],[],["Data Entry"]],
        "required_experience_level": "INTERMEDIATE",
        "contract_type": "HOURLY",
        "min_payment_rate": None,
        "max_payment_rate": None,
        "duration": 4,
        "min_connects": "10",
        "url": "https://www.upwork.com/jobs/~021865956325868219631/"
    },
    {
        "id": "021865971322597177797",
        "client": {
            "timezone": "UTC +11",
            "country": "Australia",
            "payment_method_verified": True,
            "phone_number_verified": False,
            "avg_hourly_spend": "50.15",
            "rate": "5.0",
            "freelancers_feedback": [
                "Jeremy has been an amazing client. Would love to support him",
                "As like always, it was great to work with Jeremy. He is collaborative, kind and has clear requirements and vision. I hope I can support him in future whenever needed.",
                "Absolutely stellar client, very responsive, collaborative and appreciative. I hope to support Jeremy and Benny whenever they need!",
                "Jeremey is fantastic to work with, providing clear communication and outlines for his projects.",
                "I enjoyed working on this project.",
                "It had been a pleasure working with Jeremy on Moolah app. Clear requirements with videos attached is what makes it way easier to work with him."
            ],
            "hires": 44,
            "spent": "47K"
        },
        "title": "Google API Setup for Retrieving Location-Based Reviews",
        "description": "I have google reviews spread across multiple store locations under my company. I am looking to setup an api to pull these all into our database",
        "required_english_proficiency": "ANY",
        "screening_questions": [],
        "required_skills": [["API", "JavaScript", "PHP", "Python", "WordPress"],[],[],[]],
        "required_experience_level": "INTERMEDIATE",
        "contract_type": "FIXED",
        "min_payment_rate": "300.00",
        "max_payment_rate": None,
        "duration": None,
        "min_connects": "13",
        "url": "https://www.upwork.com/jobs/~021865971322597177797"
    },
    {
        "id": "021865699811924421871",
        "client": {
            "timezone": "UTC +4",
            "country": "United Arab Emirates",
            "payment_method_verified": True,
            "phone_number_verified": True,
            "avg_hourly_spend": "35.00",
            "rate": "0.00",
            "freelancers_feedback": [],
            "hires": 1,
            "spent": "78.00"
        },
        "title": "AppSheet Application Development Using Google Sheets & AppScripts",
        "description": "We are looking for a skilled developer to create a Google AppSheet application that integrates seamlessly with our existing databases for orders, transactions, and clients, which are based on Google Sheets and App Scripts. The ideal candidate should have a strong understanding of Google AppSheet, Google Sheets, and Apps Scripts and be able to translate our data requirements into a functional and user-friendly application. If you have experience developing applications on the Google AppSheet platform and can efficiently use App Scripts for automation, we would love to hear from you!",
        "required_english_proficiency": "ANY",
        "screening_questions": [
            "Describe your recent experience with similar projects",
            "Describe your approach to testing and improving QA"
        ],
        "required_skills": [["Google Sheets", "Google Apps Script", "AppSheet"],[],[],[]],
        "required_experience_level": "INTERMEDIATE",
        "contract_type": "HOURLY",
        "duration": 9,
        "min_payment_rate": "15.00",
        "max_payment_rate": "30.00",
        "min_connects": "17",
        "url": "https://www.upwork.com/jobs/~021865699811924421871"
    },
    {
        "id": "021865697085172994780",
        "client": {
            "timezone": "UTC +4",
            "country": "United Arab Emirates",
            "payment_method_verified": True,
            "phone_number_verified": True,
            "rate": "5.0",
            "freelancers_feedback": [
                "Working with Raj was an absolute pleasure! The project was well-defined from the start, and their communication was clear and prompt throughout the process. They were open to ideas and provided timely feedback, which made it easy to deliver results that matched their expectations. I appreciate the professionalism and look forward to collaborating again in the future. Highly recommend working with Raj",
                "Working with Raj has been an excellent experience. His clear communication, collaborative approach, and insightful inputs have significantly contributed to the project's success. Raj consistently demonstrates professionalism and a strong commitment to achieving outstanding results. It's been a pleasure collaborating with him.",
                "I enjoyed consulting with Raj on the scope of work. His openness to feedback made it easy to align our goals. I value his professionalism and hope to work together again!"
            ],
            "hires": 13,
            "spent": "3.7K"
        },
        "title": "Javascript for blocking buttons from displayingMs office , Google workspace and linked in (7 tools)",
        "description": 'JavaScript Developer Needed to Restrict Application Functionalities in Productivity Tools \nJob Description:\n We are looking for an experienced JavaScript developer to create custom scripts that will disable specific functionalities in productivity tools like Excel, Word, PowerPoint, google sheets, google sldies , google docs and linked in . Workspace equivalents. These scripts will prevent actions that could lead to data leaks, such as exporting to email, API integrations, or other unauthorized functionalities.\nThe task involves analyzing the interface of these tools, identifying potential vulnerabilities (e.g., "Export," "Share," "Save As" options), and writing JavaScript code to restrict them. You’ll focus on features that, even within a controlled user environment, might enable unintended data sharing or retrieval.\n\nThis is a phased project:\nYou will work on one tool as a test case.After approval, you will work on an additional five similar tools.\nUpon approval of those, you will move to 40+ tools, with a similar approach.\n\nBudget:\nThe budget for the initial phase (6 tools) is $300, as the tools share similarities. Future tasks will be priced based on scope and successful completion of the initial phase.\n\nResponsibilities:\nAnalyze Tool Interfaces:\n\nIdentify buttons, integrations, or actions in Excel, Word, PowerPoint, and Google Workspace tools that could result in unauthorized data transfer.\n\nFocus on features like:"Export to email."\n"Save As" to external locations.\nIntegrations with APIs or third-party tools.\n\nDevelop Custom JavaScript:\n\nWrite JavaScript to dynamically disable or modify these functionalities while maintaining essential usability.\n\nEnsure scripts can be easily integrated into the environment.\n\nTesting and Documentation:\n\nSuggest methods to validate that the scripts are functioning as intended within the specified tools.\nProvide clear documentation on how the scripts work and the steps taken to identify and restrict features.\n\nSkills Required:\n\nJavaScript Expertise\nStrong understanding of DOM manipulation and event handling.\nFamiliarity with productivity tools (Excel, Word, PowerPoint, and Google Workspace).\nExperience identifying and disabling specific UI features using JavaScript.\nDeliverables:\nCustom JavaScript Code:\n\nTo disable specific functionalities in:\nExcel, Word, PowerPoint (desktop versions).\nGoogle Workspace tools (Docs, Sheets, Slides).\n\nScripts must target escape-prone actions like "Export to email," API integrations, and "Save As."\nDocumentation:\n\nA guide on how the script interacts with the tools.\nRecommendations for potential improvements or additional restrictions.\n\nValidated Test Results:\n\nEnsure the restricted functionalities are applied effectively without breaking essential features.\nPhased Approach:\nPhase 1: Develop and deliver a script for one tool (e.g., Excel) as a test case.\n\nPhase 2: Apply similar scripts to five additional tools after approval.\n\nPhase 3: Extend the solution to 40+ tools, using the same methodology.\n\nHow to Apply:\n\nShare your experience working on projects involving feature restrictions or UI customization using JavaScript.\nProvide a brief proposal outlining how you would approach this task.\nInclude examples of your past work related to similar requirements.',
        "required_english_proficiency": "ANY",
        "screening_questions": [],
        "required_skills": [[],["Scripting"],["JavaScript", "Web Development"],[]],
        "required_experience_level": "EXPERT",
        "contract_type": "FIXED",
        "min_payment_rate": "400.00",
        "max_payment_rate": None,
        "duration": None,
        "min_connects": "13",
        "url": "https://www.upwork.com/jobs/~021865697085172994780"
    },
    {
        "id": "021865892368664672012",
        "client": {
            "timezone": "UTC −3",
            "country": "Chile",
            "payment_method_verified": True,
            "phone_number_verified": True,
            "rate": "5.0",
            "freelancers_feedback": [
                "Nice client",
                "Very good communication, clear instructions, friendly and fast in response Will definitely work with Ignacio again"
            ],
            "hires": 4,
            "spent": "60.00"
        },
        "title": "Fix my code GraphQL Shopify + App Scripts from Google",
        "description": "I am having some issues fixing my code for Google Apps Script and Shopify GraphQL. I need to update the inventory for all the variants available. I get this error: It's not possible to get the inventory for Variant GID: gid://shopify/ProductVariant/*****",
        "required_english_proficiency": "ANY",
        "screening_questions": [],
        "required_skills": [["Shopify", "JavaScript"],[],[],[]],
        "required_experience_level": "EXPERT",
        "contract_type": "FIXED",
        "min_payment_rate": "30.00",
        "max_payment_rate": None,
        "duration": None,
        "min_connects": "10",
        "url": "https://www.upwork.com/jobs/~021865892368664672012"
    },
    {
        "id": "021865930345637918476",
        "client": {
            "timezone": "UTC +11",
            "country": "Australia",
            "payment_method_verified": True,
            "phone_number_verified": True,
            "freelancers_feedback": [],
            "hires": None,
            "spent": ""
        },
        "title": "JotForm Development for Excel Diagnostics Tool Integration",
        "description": "We are seeking a skilled freelancer to create a user-friendly form using JotForm that interfaces seamlessly with our existing Risk based IR diagnostics tool developed in Excel. The project will involve designing a front end for the form, complete with clear instructions for users. The ideal candidate will have experience with both JotForm and Excel, ensuring data flows smoothly between the two platforms. The input form poses a number of questions to the user requiring two answers when used in basic form and provides a calculation to the user based on the scores entered. The form also needs an option for entering the controls for the risks if this is chosen by the administrator of the form - otherwise these questions will be blanked out\n\nThe freelancer must be experienced in these tools including using formulas in Jotform - if it interfaces to excell will need Zapier as interface tool. Approx 39 line items for the questions.",
        "required_english_proficiency": "ANY",
        "screening_questions": [
            "Describe your recent experience with similar projects",
            "Describe your approach to testing and improving QA",
            "Please list any certifications related to this project",
            "What frameworks have you worked with? "
        ],
        "required_skills": [["Microsoft Excel", "API", "Visual Basic for Applications", "JavaScript", "Automation"],[],[],["VBA"]],
        "required_experience_level": "INTERMEDIATE",
        "contract_type": "FIXED",
        "min_payment_rate": "200.00",
        "max_payment_rate": None,
        "duration": None,
        "min_connects": "8",
        "url": "https://www.upwork.com/jobs/~021865930345637918476"
    }
]

def gen_job(data):
    return {"data": {
        "jobPosting": {
            "id": data["id"],
            "url": data["url"],
            "client": data["client"],
            "min_connects": "8",
            "content": {
                "title": data["title"],
                "description": data["description"]
            },
            "classification": {
                "skills": list(map(lambda x: {"prettyName": x}, data["required_skills"][0])),
                "customSkills": list(map(lambda x: {"freeText": x}, data["required_skills"][1])),
                "additionalSkills": list(map(lambda x: {"prettyName": x}, data["required_skills"][2])),
                "customAdditionalSkills": data["required_skills"][3],
            },
            "contractTerms": process_contract_terms(data),
            "contractorSelection": {
                "proposalRequirement": { 
                    "screeningQuestions": list(map(lambda x: {"question": x}, data["screening_questions"]))
                },
                "qualification": { 
                    "englishProficiency": data["required_english_proficiency"], 
                }
            },
            "additionalInfo": { 
                "clientTotalSpentOnCreate": {
                    "rawValue": data["client"]["spent"]
                },
                "clientNumberOfHiresOnCreate": data["client"]["hires"]
            }
        }
    }
}

def process_contract_terms(data):
    if data["contract_type"] == "FIXED": return {
        "contractType": data["contract_type"],
        "experienceLevel": data["required_experience_level"],
        "fixedPriceContractTerms": {
            "amount": { "rawValue": data["min_payment_rate"] },
            "maxAmount": { "rawValue": "" },
            "engagementDuration": { "weeks": data["duration"] }
        },
        "hourlyContractTerms": {}

    } 
    else: return {
        "contractType": data["contract_type"],
        "experienceLevel": data["required_experience_level"],
        "fixedPriceContractTerms": {},
        "hourlyContractTerms": {
            "hourlyBudgetMin": { "rawValue": data["min_payment_rate"] },
            "hourlyBudgetMax": { "rawValue": data["max_payment_rate"] },
            "engagementDuration": { "weeks": data["duration"] }
        }
    }



