import os
import hubspot
from hubspot.crm.imports import ApiException

client = hubspot.Client.create(
    access_token=os.environ.get("HUBSPOT_KEY"))

try:
    api_response = client.crm.imports.core_api.get_page()
    print(api_response)
except ApiException as e:
    print("Exception when calling core_api->get_page: %s\n" % e)