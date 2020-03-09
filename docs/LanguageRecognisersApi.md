# feersum_nlu.LanguageRecognisersApi

All URIs are relative to *https://nlu.feersum.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**language_recogniser_create**](LanguageRecognisersApi.md#language_recogniser_create) | **POST** /nlu/v2/language_recognisers | Create a text language detector.
[**language_recogniser_del**](LanguageRecognisersApi.md#language_recogniser_del) | **DELETE** /nlu/v2/language_recognisers/{instance_name} | Delete named instance.
[**language_recogniser_get_details**](LanguageRecognisersApi.md#language_recogniser_get_details) | **GET** /nlu/v2/language_recognisers/{instance_name} | Get details of named instance.
[**language_recogniser_get_details_all**](LanguageRecognisersApi.md#language_recogniser_get_details_all) | **GET** /nlu/v2/language_recognisers | Get list of text language detectors.
[**language_recogniser_get_labels**](LanguageRecognisersApi.md#language_recogniser_get_labels) | **GET** /nlu/v2/language_recognisers/{instance_name}/labels | Get list of possible labels.
[**language_recogniser_get_params**](LanguageRecognisersApi.md#language_recogniser_get_params) | **GET** /nlu/v2/language_recognisers/{instance_name}/params | Get the editable model parameters of named language recogniser.
[**language_recogniser_retrieve**](LanguageRecognisersApi.md#language_recogniser_retrieve) | **POST** /nlu/v2/language_recognisers/{instance_name}/retrieve | Recognise the language the text is written in.
[**language_recogniser_set_params**](LanguageRecognisersApi.md#language_recogniser_set_params) | **POST** /nlu/v2/language_recognisers/{instance_name}/params | Set the model parameters of named language recogniser.
[**language_recogniser_vaporise**](LanguageRecognisersApi.md#language_recogniser_vaporise) | **POST** /nlu/v2/language_recognisers/{instance_name}/vaporise | Vaporise the named model.


# **language_recogniser_create**
> LanguageRecogniserInstanceDetail language_recogniser_create(create_details, x_caller=x_caller)

Create a text language detector.

Create  new language detector from the pre-trained model name provided. 'lid_za' is currently the only pre-trained model that is available, but it was trained on all 11 languages and is pretty accurate. Returns the detail of the new instance.

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.LanguageRecogniserCreateDetails() # LanguageRecogniserCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create a text language detector.
    api_response = api_instance.language_recogniser_create(create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**LanguageRecogniserCreateDetails**](LanguageRecogniserCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**LanguageRecogniserInstanceDetail**](LanguageRecogniserInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_recogniser_del**
> LanguageRecogniserInstanceDetail language_recogniser_del(instance_name, x_caller=x_caller)

Delete named instance.

Delete and return the details of the named text language detector instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.language_recogniser_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**LanguageRecogniserInstanceDetail**](LanguageRecogniserInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_recogniser_get_details**
> LanguageRecogniserInstanceDetail language_recogniser_get_details(instance_name, x_caller=x_caller)

Get details of named instance.

Get the details of the named text language detector instance.

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.language_recogniser_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**LanguageRecogniserInstanceDetail**](LanguageRecogniserInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_recogniser_get_details_all**
> list[LanguageRecogniserInstanceDetail] language_recogniser_get_details_all(x_caller=x_caller)

Get list of text language detectors.

Get the list of text language detectors.

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of text language detectors.
    api_response = api_instance.language_recogniser_get_details_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[LanguageRecogniserInstanceDetail]**](LanguageRecogniserInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_recogniser_get_labels**
> list[ClassLabel] language_recogniser_get_labels(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of possible labels.
    api_response = api_instance.language_recogniser_get_labels(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_get_labels: %s\n" % e)
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

# **language_recogniser_get_params**
> ModelParams language_recogniser_get_params(instance_name, x_caller=x_caller)

Get the editable model parameters of named language recogniser.

Get the editable model parameters of named language recogniser.

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the editable model parameters of named language recogniser.
    api_response = api_instance.language_recogniser_get_params(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_get_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**ModelParams**](ModelParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_recogniser_retrieve**
> list[ScoredLabel] language_recogniser_retrieve(instance_name, text_input, x_caller=x_caller)

Recognise the language the text is written in.

Recognise the language the text is written in. Returns the list of scored language codes (ISO 639-3).

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Recognise the language the text is written in.
    api_response = api_instance.language_recogniser_retrieve(instance_name, text_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_retrieve: %s\n" % e)
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

# **language_recogniser_set_params**
> LanguageRecogniserInstanceDetail language_recogniser_set_params(instance_name, model_params, x_caller=x_caller)

Set the model parameters of named language recogniser.

Set the model parameters of named language recogniser.

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Set the model parameters of named language recogniser.
    api_response = api_instance.language_recogniser_set_params(instance_name, model_params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**LanguageRecogniserInstanceDetail**](LanguageRecogniserInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_recogniser_vaporise**
> LanguageRecogniserInstanceDetail language_recogniser_vaporise(instance_name, x_caller=x_caller)

Vaporise the named model.

Permanently vaporises a model even if not trashed.

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
api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named model.
    api_response = api_instance.language_recogniser_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageRecognisersApi->language_recogniser_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**LanguageRecogniserInstanceDetail**](LanguageRecogniserInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

