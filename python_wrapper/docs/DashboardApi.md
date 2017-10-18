# feersum_nlu.DashboardApi

All URIs are relative to *http://nlu.playground.feersum.io:8100/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_get_details**](DashboardApi.md#dashboard_get_details) | **GET** /dashboard | Your service dashboard.


# **dashboard_get_details**
> DashboardDetail dashboard_get_details()

Your service dashboard.

Get your list of loaded model instances, the total API hits for each, API version, etc.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.DashboardApi()

try: 
    # Your service dashboard.
    api_response = api_instance.dashboard_get_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardDetail**](DashboardDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

