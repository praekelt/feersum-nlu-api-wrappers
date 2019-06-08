# feersum_nlu.SentimentDetectorsApi

All URIs are relative to *https://nlu.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sentiment_detector_retrieve**](SentimentDetectorsApi.md#sentiment_detector_retrieve) | **POST** /sentiment_detectors/{instance_name}/retrieve | Detect sentiment.


# **sentiment_detector_retrieve**
> Sentiment sentiment_detector_retrieve(instance_name, text_input, x_caller=x_caller, origin=origin)

Detect sentiment.

Detect the general sentiment in the input text.

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
api_instance = feersum_nlu.SentimentDetectorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Detect sentiment.
    api_response = api_instance.sentiment_detector_retrieve(instance_name, text_input, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentimentDetectorsApi->sentiment_detector_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**Sentiment**](Sentiment.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

