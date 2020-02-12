# feersum_nlu.DashboardApi

All URIs are relative to *https://nlu.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_get_details**](DashboardApi.md#dashboard_get_details) | **GET** /dashboard | Your service dashboard. Same as POST endpoint, but doesn&#39;t allow params to be supplied to the operation.
[**dashboard_get_details_with_params**](DashboardApi.md#dashboard_get_details_with_params) | **POST** /dashboard | Your service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.


# **dashboard_get_details**
> DashboardDetail dashboard_get_details(x_caller=x_caller)

Your service dashboard. Same as POST endpoint, but doesn't allow params to be supplied to the operation.

Get your list of loaded model instances, the API version, etc. Same as POST endpoint, but doesn't allow params to be supplied to the operation.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.DashboardApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Your service dashboard. Same as POST endpoint, but doesn't allow params to be supplied to the operation.
    api_response = api_instance.dashboard_get_details(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**DashboardDetail**](DashboardDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_get_details_with_params**
> DashboardDetail dashboard_get_details_with_params(params, x_caller=x_caller)

Your service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.

Get your list of loaded model instances, the API version, etc. Same as GET endpoint, but allows params to be supplied to the operation.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.DashboardApi(feersum_nlu.ApiClient(configuration))
params = feersum_nlu.DashboardParams() # DashboardParams | Params like 'show_data_objects' that influence the dashboard's response.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Your service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.
    api_response = api_instance.dashboard_get_details_with_params(params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_details_with_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**DashboardParams**](DashboardParams.md)| Params like &#39;show_data_objects&#39; that influence the dashboard&#39;s response. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**DashboardDetail**](DashboardDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

