# feersum_nlu.DataObjectsApi

All URIs are relative to *https://nlu.feersum.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_object_del**](DataObjectsApi.md#data_object_del) | **DELETE** /nlu/v2/data_objects/{instance_name} | Trash a data_object.
[**data_object_del_all**](DataObjectsApi.md#data_object_del_all) | **DELETE** /nlu/v2/data_objects | Delete all data_objects. Returns list of names of data_objects deleted. Note that this is a convenience operation. The objects will still need to be vaporised one by one.
[**data_object_get_details**](DataObjectsApi.md#data_object_get_details) | **GET** /nlu/v2/data_objects/{instance_name} | Get a data_object.
[**data_object_get_names_all**](DataObjectsApi.md#data_object_get_names_all) | **GET** /nlu/v2/data_objects | Get list of names of loaded data_objects.
[**data_object_post**](DataObjectsApi.md#data_object_post) | **POST** /nlu/v2/data_objects/{instance_name} | Update/create a data_object.
[**data_object_untrash**](DataObjectsApi.md#data_object_untrash) | **POST** /nlu/v2/data_objects/{instance_name}/untrash | Untrash the named data_object.
[**data_object_vaporise**](DataObjectsApi.md#data_object_vaporise) | **POST** /nlu/v2/data_objects/{instance_name}/vaporise | Vaporise the named data_object.


# **data_object_del**
> DataObject data_object_del(instance_name, x_caller=x_caller)

Trash a data_object.

Trash a data_object.

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
api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the data_object.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Trash a data_object.
    api_response = api_instance.data_object_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataObjectsApi->data_object_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the data_object. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**DataObject**](DataObject.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_object_del_all**
> list[DataObjectName] data_object_del_all(x_caller=x_caller)

Delete all data_objects. Returns list of names of data_objects deleted. Note that this is a convenience operation. The objects will still need to be vaporised one by one.

Get the list of names of loaded data_objects.

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
api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all data_objects. Returns list of names of data_objects deleted. Note that this is a convenience operation. The objects will still need to be vaporised one by one.
    api_response = api_instance.data_object_del_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataObjectsApi->data_object_del_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[DataObjectName]**](DataObjectName.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_object_get_details**
> DataObject data_object_get_details(instance_name, x_caller=x_caller)

Get a data_object.

Get a data_object.

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
api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the data_object.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get a data_object.
    api_response = api_instance.data_object_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataObjectsApi->data_object_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the data_object. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**DataObject**](DataObject.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_object_get_names_all**
> list[DataObjectName] data_object_get_names_all(x_caller=x_caller)

Get list of names of loaded data_objects.

Get the list of names of loaded data_objects.

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
api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of names of loaded data_objects.
    api_response = api_instance.data_object_get_names_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataObjectsApi->data_object_get_names_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[DataObjectName]**](DataObjectName.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_object_post**
> DataObject data_object_post(instance_name, data, x_caller=x_caller)

Update/create a data_object.

Update/create a data_object.

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
api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the data_object.
data = feersum_nlu.DataObject() # DataObject | The data_object.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update/create a data_object.
    api_response = api_instance.data_object_post(instance_name, data, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataObjectsApi->data_object_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the data_object. | 
 **data** | [**DataObject**](DataObject.md)| The data_object. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**DataObject**](DataObject.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_object_untrash**
> DataObject data_object_untrash(instance_name, x_caller=x_caller)

Untrash the named data_object.

Bring the named data_object back from the trash.

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
api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the data_object.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Untrash the named data_object.
    api_response = api_instance.data_object_untrash(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataObjectsApi->data_object_untrash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the data_object. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**DataObject**](DataObject.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_object_vaporise**
> DataObject data_object_vaporise(instance_name, x_caller=x_caller)

Vaporise the named data_object.

Permanently vaporise the named data_object.

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
api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the data_object.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named data_object.
    api_response = api_instance.data_object_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataObjectsApi->data_object_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the data_object. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**DataObject**](DataObject.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

