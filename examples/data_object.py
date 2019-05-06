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

instance_name = 'app_data'

data = {"app_attr1_key": "app_attr1_value",
        "app_attr2_key": "app_attr1_value"}

print()

try:
    print("Create the data object:")
    api_response = api_instance.data_object_post(instance_name=instance_name, data=data)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the names of all data objects:")
    api_response = api_instance.data_object_get_names_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named data object:")
    api_response = api_instance.data_object_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Delete specific named data object:")
    # api_response = api_instance.data_object_del(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Vaporise specific named data object:")
    # api_response = api_instance.data_object_vaporise(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

except ApiException as e:
    print("Exception when calling a data object operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
