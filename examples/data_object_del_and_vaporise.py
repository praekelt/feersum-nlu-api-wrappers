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
    data_object_to_delete = 'user_782'

    print("Delete named data object:")
    api_response = api_instance.data_object_del(instance_name=data_object_to_delete)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise named data object:")
    api_response = api_instance.data_object_vaporise(instance_name=data_object_to_delete)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a data object operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
