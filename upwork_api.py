import requests, json, os
token = os.environ.get("FRESHSALES_KEY")
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Token token={token}'
}

json_data = {
    'deal': {
        'name': 'Sample deal',
        'amount': 23456,
        'tags': [
            '10-20 con'
        ],
        'custom_field': {
            'cf_connects_required': 8
        }
    },
}

r = requests.post(
    "https://sns1-782924923744476135.myfreshworks.com/crm/sales/api/deals/", 
    json=json_data, 
    headers=headers
)

print(json.dumps(r.json(), indent=4))
