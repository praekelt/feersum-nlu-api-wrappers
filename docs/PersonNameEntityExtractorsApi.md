# feersum_nlu.PersonNameEntityExtractorsApi

All URIs are relative to *https://nlu.feersum.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**person_name_entity_extractor_create**](PersonNameEntityExtractorsApi.md#person_name_entity_extractor_create) | **POST** /nlu/v2/person_name_entity_extractors | Create a person_name entity extractor.
[**person_name_entity_extractor_del**](PersonNameEntityExtractorsApi.md#person_name_entity_extractor_del) | **DELETE** /nlu/v2/person_name_entity_extractors/{instance_name} | Delete named instance.
[**person_name_entity_extractor_get_details**](PersonNameEntityExtractorsApi.md#person_name_entity_extractor_get_details) | **GET** /nlu/v2/person_name_entity_extractors/{instance_name} | Get details of named instance.
[**person_name_entity_extractor_get_details_all**](PersonNameEntityExtractorsApi.md#person_name_entity_extractor_get_details_all) | **GET** /nlu/v2/person_name_entity_extractors | Get list of loaded regular expression entity extractors.
[**person_name_entity_extractor_get_params**](PersonNameEntityExtractorsApi.md#person_name_entity_extractor_get_params) | **GET** /nlu/v2/person_name_entity_extractors/{instance_name}/params | Get the editable model parameters of named person name entity extractor.
[**person_name_entity_extractor_retrieve**](PersonNameEntityExtractorsApi.md#person_name_entity_extractor_retrieve) | **POST** /nlu/v2/person_name_entity_extractors/{instance_name}/retrieve | Extract information based on the regular expression.
[**person_name_entity_extractor_set_params**](PersonNameEntityExtractorsApi.md#person_name_entity_extractor_set_params) | **POST** /nlu/v2/person_name_entity_extractors/{instance_name}/params | Set the model parameters of named person name entity extractor.
[**person_name_entity_extractor_vaporise**](PersonNameEntityExtractorsApi.md#person_name_entity_extractor_vaporise) | **POST** /nlu/v2/person_name_entity_extractors/{instance_name}/vaporise | Vaporise the named model.


# **person_name_entity_extractor_create**
> PersonNameEntityExtractorInstanceDetail person_name_entity_extractor_create(create_details, x_caller=x_caller)

Create a person_name entity extractor.

Create a new person_name entity extractor or reload one from the trash.

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
api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.PersonNameEntityExtractorCreateDetails() # PersonNameEntityExtractorCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create a person_name entity extractor.
    api_response = api_instance.person_name_entity_extractor_create(create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonNameEntityExtractorsApi->person_name_entity_extractor_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**PersonNameEntityExtractorCreateDetails**](PersonNameEntityExtractorCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**PersonNameEntityExtractorInstanceDetail**](PersonNameEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_name_entity_extractor_del**
> PersonNameEntityExtractorInstanceDetail person_name_entity_extractor_del(instance_name, x_caller=x_caller)

Delete named instance.

Delete and return the details of the named person_name entity extractor instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.person_name_entity_extractor_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonNameEntityExtractorsApi->person_name_entity_extractor_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**PersonNameEntityExtractorInstanceDetail**](PersonNameEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_name_entity_extractor_get_details**
> PersonNameEntityExtractorInstanceDetail person_name_entity_extractor_get_details(instance_name, x_caller=x_caller)

Get details of named instance.

Get the details of the named person_name entity extractor instance.

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
api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.person_name_entity_extractor_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonNameEntityExtractorsApi->person_name_entity_extractor_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**PersonNameEntityExtractorInstanceDetail**](PersonNameEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_name_entity_extractor_get_details_all**
> list[PersonNameEntityExtractorInstanceDetail] person_name_entity_extractor_get_details_all(x_caller=x_caller)

Get list of loaded regular expression entity extractors.

Get the list of loaded person_name entity extractors.

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
api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of loaded regular expression entity extractors.
    api_response = api_instance.person_name_entity_extractor_get_details_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonNameEntityExtractorsApi->person_name_entity_extractor_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[PersonNameEntityExtractorInstanceDetail]**](PersonNameEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_name_entity_extractor_get_params**
> ModelParams person_name_entity_extractor_get_params(instance_name, x_caller=x_caller)

Get the editable model parameters of named person name entity extractor.

Get the editable model parameters of named person name entity extractor.

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
api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the editable model parameters of named person name entity extractor.
    api_response = api_instance.person_name_entity_extractor_get_params(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonNameEntityExtractorsApi->person_name_entity_extractor_get_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**ModelParams**](ModelParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_name_entity_extractor_retrieve**
> list[PersonNameEntity] person_name_entity_extractor_retrieve(instance_name, text_input, x_caller=x_caller)

Extract information based on the regular expression.

Extract the entities parsed by person_name.

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
api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Extract information based on the regular expression.
    api_response = api_instance.person_name_entity_extractor_retrieve(instance_name, text_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonNameEntityExtractorsApi->person_name_entity_extractor_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[PersonNameEntity]**](PersonNameEntity.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_name_entity_extractor_set_params**
> PersonNameEntityExtractorInstanceDetail person_name_entity_extractor_set_params(instance_name, model_params, x_caller=x_caller)

Set the model parameters of named person name entity extractor.

Set the model parameters of named person name entity extractor.

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
api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Set the model parameters of named person name entity extractor.
    api_response = api_instance.person_name_entity_extractor_set_params(instance_name, model_params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonNameEntityExtractorsApi->person_name_entity_extractor_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**PersonNameEntityExtractorInstanceDetail**](PersonNameEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_name_entity_extractor_vaporise**
> PersonNameEntityExtractorInstanceDetail person_name_entity_extractor_vaporise(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named model.
    api_response = api_instance.person_name_entity_extractor_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonNameEntityExtractorsApi->person_name_entity_extractor_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**PersonNameEntityExtractorInstanceDetail**](PersonNameEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

