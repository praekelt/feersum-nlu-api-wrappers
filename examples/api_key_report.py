""" Example: Shows how to create and manage API keys. """
import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token


# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.ApiKeysApi(feersum_nlu.ApiClient(configuration))

print()

try:
    api_key = feersum_nlu_auth_token
    print("api_key =", api_key)
    print()

    # print("Get the details of all API keys:")
    # api_response = api_instance.api_key_get_details_all()
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print(" len(api_response) =", len(api_response))
    # print()

    print("Get the details of specific named API key:")
    api_response = api_instance.api_key_get_details(api_key)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an api key operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
