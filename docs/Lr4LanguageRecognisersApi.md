# feersum_nlu.Lr4LanguageRecognisersApi

All URIs are relative to *https://nlu.playground.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lr4_language_recogniser_create**](Lr4LanguageRecognisersApi.md#lr4_language_recogniser_create) | **POST** /lr4_language_recognisers | Create a LR4 text language detector.
[**lr4_language_recogniser_get_details**](Lr4LanguageRecognisersApi.md#lr4_language_recogniser_get_details) | **GET** /lr4_language_recognisers/{instance_name} | Get details of named instance.
[**lr4_language_recogniser_get_details_all**](Lr4LanguageRecognisersApi.md#lr4_language_recogniser_get_details_all) | **GET** /lr4_language_recognisers | Get list of loaded LR4 text language detectors.
[**lr4_language_recogniser_get_labels**](Lr4LanguageRecognisersApi.md#lr4_language_recogniser_get_labels) | **GET** /lr4_language_recognisers/{instance_name}/get_labels | Get list of possible labels.
[**lr4_language_recogniser_retrieve**](Lr4LanguageRecognisersApi.md#lr4_language_recogniser_retrieve) | **POST** /lr4_language_recognisers/{instance_name}/retrieve | Recognise the language the text is written in.


# **lr4_language_recogniser_create**
> Lr4InstanceDetail lr4_language_recogniser_create(lr4_create_details)

Create a LR4 text language detector.

Create a new LR4 language detector from the pre-trained model name provided. 'lid_za' is currently the only pre-trained model that is available, but it was trained on all 11 languages and is pretty accurate. Returns the detail of the new instance.

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
api_instance = feersum_nlu.Lr4LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
lr4_create_details = feersum_nlu.Lr4CreateDetails() # Lr4CreateDetails | The details of the instance to create.

try:
    # Create a LR4 text language detector.
    api_response = api_instance.lr4_language_recogniser_create(lr4_create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Lr4LanguageRecognisersApi->lr4_language_recogniser_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lr4_create_details** | [**Lr4CreateDetails**](Lr4CreateDetails.md)| The details of the instance to create. | 

### Return type

[**Lr4InstanceDetail**](Lr4InstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lr4_language_recogniser_get_details**
> Lr4InstanceDetail lr4_language_recogniser_get_details(instance_name)

Get details of named instance.

Get the details of the named LR4 text language detector instance.

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
api_instance = feersum_nlu.Lr4LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get details of named instance.
    api_response = api_instance.lr4_language_recogniser_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Lr4LanguageRecognisersApi->lr4_language_recogniser_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**Lr4InstanceDetail**](Lr4InstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lr4_language_recogniser_get_details_all**
> Lr4InstanceDetailList lr4_language_recogniser_get_details_all()

Get list of loaded LR4 text language detectors.

Get the list of loaded LR4 text language detectors.

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
api_instance = feersum_nlu.Lr4LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))

try:
    # Get list of loaded LR4 text language detectors.
    api_response = api_instance.lr4_language_recogniser_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Lr4LanguageRecognisersApi->lr4_language_recogniser_get_details_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Lr4InstanceDetailList**](Lr4InstanceDetailList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lr4_language_recogniser_get_labels**
> ClassLabelList lr4_language_recogniser_get_labels(instance_name)

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
api_instance = feersum_nlu.Lr4LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get list of possible labels.
    api_response = api_instance.lr4_language_recogniser_get_labels(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Lr4LanguageRecognisersApi->lr4_language_recogniser_get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**ClassLabelList**](ClassLabelList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lr4_language_recogniser_retrieve**
> ScoredLabelList lr4_language_recogniser_retrieve(instance_name, text_input)

Recognise the language the text is written in.

Recognise the language the text is written in. Returns the list of scored language codes.

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
api_instance = feersum_nlu.Lr4LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try:
    # Recognise the language the text is written in.
    api_response = api_instance.lr4_language_recogniser_retrieve(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Lr4LanguageRecognisersApi->lr4_language_recogniser_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 

### Return type

[**ScoredLabelList**](ScoredLabelList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

