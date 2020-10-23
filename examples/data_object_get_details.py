""" Example: Shows how to use data objects. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))

print()

try:
    instance_name = 'user007'

    # print("Get the names of all data objects:")
    # object_name_list = api_instance.data_object_get_names_all()
    # print(" type(api_response)", type(object_name_list))
    # print(" api_response", object_name_list)
    # print()

    print("Get details of named data object:")
    api_response = api_instance.data_object_get_details(instance_name=instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a data object operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
