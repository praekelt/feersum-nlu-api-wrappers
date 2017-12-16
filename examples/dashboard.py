""" Example: Shows how to get info about the service using the Dashboard endpoint.  """

import urllib3

import os
import feersum_nlu
from feersum_nlu.rest import ApiException


# Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
# You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

# configuration.host = "http://127.0.0.1:8100/nlu/v2"
configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

api_instance = feersum_nlu.DashboardApi(feersum_nlu.ApiClient(configuration))

print()

try:
    print("Get dashboard content:")
    api_response = api_instance.dashboard_get_details()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_details: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
