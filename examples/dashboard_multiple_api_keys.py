""" Example: Shows how to get info about the service using the Dashboard endpoint.  """

import urllib3
from typing import List, Tuple

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

key_detail_list = []  # type: List[Tuple[str, str]]

# Configure API key authorization: APIKeyHeader
admin_configuration = feersum_nlu.Configuration()

# admin_configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
admin_configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

admin_configuration.host = feersumnlu_host
print(admin_configuration.host)

keys_api_instance = feersum_nlu.ApiKeysApi(feersum_nlu.ApiClient(admin_configuration))
try:
    print("Get the details of all API keys:")
    api_response = keys_api_instance.api_key_get_details_all()

    for key_detail in api_response:
        key_detail_list.append((key_detail.api_key, key_detail.desc))
    print()

except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_details: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)

for key, desc in key_detail_list:
    # Configure API key authorization: APIKeyHeader
    configuration = feersum_nlu.Configuration()
    configuration.api_key['X-Auth-Token'] = key
    configuration.host = feersumnlu_host
    print("===")
    print(desc, configuration.host)

    api_instance = feersum_nlu.DashboardApi(feersum_nlu.ApiClient(configuration))
    dash_params = feersum_nlu.DashboardParams(show_data_objects=True,
                                              history_size=5)
    caller_name = 'example_caller'

    try:
        api_response, api_response_code, api_response_header = \
            api_instance.dashboard_nlu_get_details_with_params_with_http_info(x_caller=caller_name,
                                                                              params=dash_params,
                                                                              _request_timeout=2)
        model_list = api_response.model_list

        for model in model_list:
            if (('sentence_encoder' in model.model_type) is False) and \
                    (('image_encoder' in model.model_type) is False) and \
                    (('date_parser' in model.model_type) is False) and \
                    (('sentiment_detector' in model.model_type) is False) and \
                    (('emotion_detector' in model.model_type) is False) and \
                    (('image_encoder' in model.model_type) is False) and \
                    (('image_encoder' in model.model_type) is False):
                print("* model.name:", model.name)
                print("  model.model_type:", model.model_type)
                print("  model.long_name:", model.long_name)
                print("  model.desc:", model.desc)
                print("  model.trashed:", model.trashed)

    except ApiException as e:
        print("Exception when calling DashboardApi->dashboard_get_details: %s\n" % e)
    except urllib3.exceptions.HTTPError as e:
        print("Connection HTTPError! %s\n" % e)

    print("===")
    print()
