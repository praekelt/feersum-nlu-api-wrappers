# feersum_nlu.ApiKeysApi

All URIs are relative to *https://nlu.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_create**](ApiKeysApi.md#api_key_create) | **POST** /api_keys | Create an API key.
[**api_key_del**](ApiKeysApi.md#api_key_del) | **DELETE** /api_keys/{instance_name} | Delete named API key.
[**api_key_get_details**](ApiKeysApi.md#api_key_get_details) | **GET** /api_keys/{instance_name} | Get details of named API key.
[**api_key_get_details_all**](ApiKeysApi.md#api_key_get_details_all) | **GET** /api_keys | Get list of API keys. Admin rights are required to get the full list of API keys.


# **api_key_create**
> ApiKeyInstanceDetail api_key_create(create_details)

Create an API key.

Create a new API key. Admin rights are required to create an API key.

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
api_instance = feersum_nlu.ApiKeysApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.ApiKeyCreateDetails() # ApiKeyCreateDetails | The details of the API key to create.

try:
    # Create an API key.
    api_response = api_instance.api_key_create(create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->api_key_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**ApiKeyCreateDetails**](ApiKeyCreateDetails.md)| The details of the API key to create. | 

### Return type

[**ApiKeyInstanceDetail**](ApiKeyInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_del**
> ApiKeyInstanceDetail api_key_del(instance_name)

Delete named API key.

Delete and return the details of the named API key.

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
api_instance = feersum_nlu.ApiKeysApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The API key.

try:
    # Delete named API key.
    api_response = api_instance.api_key_del(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->api_key_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The API key. | 

### Return type

[**ApiKeyInstanceDetail**](ApiKeyInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_get_details**
> ApiKeyInstanceDetail api_key_get_details(instance_name)

Get details of named API key.

Get the details of the named API key.

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
api_instance = feersum_nlu.ApiKeysApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The API key.

try:
    # Get details of named API key.
    api_response = api_instance.api_key_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->api_key_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The API key. | 

### Return type

[**ApiKeyInstanceDetail**](ApiKeyInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_key_get_details_all**
> list[ApiKeyInstanceDetail] api_key_get_details_all()

Get list of API keys. Admin rights are required to get the full list of API keys.

Get list of API keys.

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
api_instance = feersum_nlu.ApiKeysApi(feersum_nlu.ApiClient(configuration))

try:
    # Get list of API keys. Admin rights are required to get the full list of API keys.
    api_response = api_instance.api_key_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->api_key_get_details_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiKeyInstanceDetail]**](ApiKeyInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

