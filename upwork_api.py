import hubspot
from hubspot.crm.imports import ApiException

client = hubspot.Client.create(access_token="YOUR_ACCESS_TOKEN")

try:
    api_response = client.crm.imports.core_api.get_page()
    print(api_response)
except ApiException as e:
    print("Exception when calling core_api->get_page: %s\n" % e)