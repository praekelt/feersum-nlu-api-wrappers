import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

# feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
feersum_nlu.configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

api_instance = feersum_nlu.DashboardApi()

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
