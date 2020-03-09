# feersum_nlu.EmotionClassifiersApi

All URIs are relative to *https://nlu.feersum.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emotion_classifier_get_labels**](EmotionClassifiersApi.md#emotion_classifier_get_labels) | **GET** /nlu/v2/emotion_classifiers/{instance_name}/labels | Get list of possible labels.
[**emotion_classifier_retrieve**](EmotionClassifiersApi.md#emotion_classifier_retrieve) | **POST** /nlu/v2/emotion_classifiers/{instance_name}/retrieve | Classify emotion.


# **emotion_classifier_get_labels**
> list[ClassLabel] emotion_classifier_get_labels(instance_name, x_caller=x_caller)

Get list of possible labels.

Returns the classifier's list of possible class labels.

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
api_instance = feersum_nlu.EmotionClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of possible labels.
    api_response = api_instance.emotion_classifier_get_labels(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmotionClassifiersApi->emotion_classifier_get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[ClassLabel]**](ClassLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emotion_classifier_retrieve**
> list[ScoredLabel] emotion_classifier_retrieve(instance_name, text_input, x_caller=x_caller)

Classify emotion.

Classifies the emotion in the text and returns a probability sorted list of classes.

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
api_instance = feersum_nlu.EmotionClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Classify emotion.
    api_response = api_instance.emotion_classifier_retrieve(instance_name, text_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmotionClassifiersApi->emotion_classifier_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[ScoredLabel]**](ScoredLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

