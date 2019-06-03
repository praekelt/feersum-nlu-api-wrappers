""" Example: Shows how to get info about the service using the Dashboard endpoint.  """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host
print(configuration.host)

api_instance = feersum_nlu.HealthApi(feersum_nlu.ApiClient(configuration))

caller_name = 'example_caller'

print()

try:
    print("Get health status:")
    api_response, api_response_code, api_response_header = \
        api_instance.health_get_status_with_http_info(x_caller=caller_name)

    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print(" type(api_response_code)", type(api_response_code))
    print(" api_response_code", api_response_code)
    print(" type(api_response_header)", type(api_response_header))
    print(" api_response_header", api_response_header)
    print(" calls remaining in this cycle ('-1' means no limit) =", api_response_header.get("X-RateLimit-Remaining"))
    print()

except ApiException as e:
    print("Exception when calling HealthApi->health_get_status: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
