# feersum_nlu.ImageReadersApi

All URIs are relative to *https://nlu.feersum.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_reader_retrieve**](ImageReadersApi.md#image_reader_retrieve) | **POST** /vision/v2/image_readers/{instance_name}/retrieve | Read text from the image.


# **image_reader_retrieve**
> list[Paragraph] image_reader_retrieve(instance_name, image_input, x_caller=x_caller)

Read text from the image.

Read text from the image. Returns list of strings found.

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
api_instance = feersum_nlu.ImageReadersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
image_input = feersum_nlu.ImageInput() # ImageInput | The input image.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Read text from the image.
    api_response = api_instance.image_reader_retrieve(instance_name, image_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageReadersApi->image_reader_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **image_input** | [**ImageInput**](ImageInput.md)| The input image. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[Paragraph]**](Paragraph.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

