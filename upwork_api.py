import os
import hubspot
from pprint import pprint
from hubspot.crm.deals import SimplePublicObjectInputForCreate, ApiException

client = hubspot.Client.create(access_token=os.environ.get("HUBSPOT_KEY"))

properties = {
    'dealname': 'test2',
    'dealstage': 'appointmentscheduled'
}
simple_public_object_input_for_create = SimplePublicObjectInputForCreate(associations=[], object_write_trace_id="string", properties=properties)
try:
    api_response = client.crm.deals.basic_api.create(simple_public_object_input_for_create=simple_public_object_input_for_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling basic_api->create: %s\n" % e)