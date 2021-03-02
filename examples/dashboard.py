""" Example: Shows how to get info about the service using the Dashboard endpoint.  """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

import time

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host
print(configuration.host)

api_client = feersum_nlu.ApiClient(configuration)

# Example of how to setup request retries!
api_client.rest_client.pool_manager.connection_pool_kw['retries'] = 5
api_instance = feersum_nlu.DashboardApi(api_client)

dash_params = feersum_nlu.DashboardParams(show_data_objects=True,
                                          history_size=5)

caller_name = 'example_caller'

print()

try:
    # Note: The _with_http_info function also returns the api_response_header!
    #       The header contains response headers like X-Rate-Limit-Remain.

    start = time.time()

    print("Get dashboard content (use CUSTOM operation params):")
    api_response, api_response_code, api_response_header = \
        api_instance.dashboard_nlu_get_details_with_params_with_http_info(x_caller=caller_name,
                                                                          params=dash_params,
                                                                          _request_timeout=2)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print(" type(api_response_code)", type(api_response_code))
    print(" api_response_code", api_response_code)
    print(" type(api_response_header)", type(api_response_header))
    print(" api_response_header", api_response_header)
    print(" calls remaining in this cycle ('-1' means no limit) =", api_response_header.get("X-RateLimit-Remaining"))

    # model_list = api_response.model_list
    # for model_detail in model_list:
    #     print(str(model_detail.model_type))

    # print("Get dashboard content (use DEFAULT operations params):")
    # api_response, api_response_code, api_response_header = \
    #     api_instance.dashboard_get_details_with_http_info(x_caller=caller_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print(" type(api_response_code)", type(api_response_code))
    # print(" api_response_code", api_response_code)
    # print(" type(api_response_header)", type(api_response_header))
    # print(" api_response_header", api_response_header)
    # print(" calls remaining in this cycle ('-1' means no limit) =", api_response_header.get("X-RateLimit-Remaining"))

    print()
    end = time.time()
    print("dashboard query time =", end - start)
    print()

except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_details: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
