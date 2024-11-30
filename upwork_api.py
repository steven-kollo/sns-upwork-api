import requests, json, os

token = os.environ.get("FRESHSALES_KEY")

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Token token={token}'
}

json_data = {
    "deal": {    
        "name": "Name",
        "amount": 1010,
        "tags": [
            "Hourly",
            "Sr",
            "< 1 mos",
            "WW" 
        ],
        "custom_field": {
            "cf_required_skills": "API;Automation;Google Sheets",
            "cf_connects_required": 8,
            "cf_job_url": "https://google.com",
            "cf_client_name": "John Doe",
            "cf_client_location": "US",
            "cf_client_spend": 1600,
            "cf_client_rate": 4.8,
            "cf_client_time_zone": 1
        }
    }
}

deal = requests.post(
    "https://sns1-782924923744476135.myfreshworks.com/crm/sales/api/deals/", 
    json=json_data, 
    headers=headers
)

note = requests.post(
    "https://sns1-782924923744476135.myfreshworks.com/crm/sales/api/notes/", 
    headers=headers,
    json={
        "note": {
            "targetable_type":"Deal",
            "targetable_id":deal.json()["deal"]["id"],
            "description":"Hello Note"
        }
    }
)

r = json.dumps(note.json(), indent=4)
print(r)

