# feersum_nlu.TextPipelinesApi

All URIs are relative to *https://nlu.feersum.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_pipeline_add_models**](TextPipelinesApi.md#text_pipeline_add_models) | **POST** /nlu/v2/text_pipelines/{instance_name}/models | Add list of models.
[**text_pipeline_create**](TextPipelinesApi.md#text_pipeline_create) | **POST** /nlu/v2/text_pipelines | Create a text pipeline.
[**text_pipeline_create_from_path**](TextPipelinesApi.md#text_pipeline_create_from_path) | **POST** /nlu/v2/text_pipelines/{instance_name} | Create a text pipeline.
[**text_pipeline_del**](TextPipelinesApi.md#text_pipeline_del) | **DELETE** /nlu/v2/text_pipelines/{instance_name} | Delete named instance.
[**text_pipeline_del_models**](TextPipelinesApi.md#text_pipeline_del_models) | **DELETE** /nlu/v2/text_pipelines/{instance_name}/models | Delete list of models.
[**text_pipeline_del_models_all**](TextPipelinesApi.md#text_pipeline_del_models_all) | **DELETE** /nlu/v2/text_pipelines/{instance_name}/models_all | Delete all models from the pipeline.
[**text_pipeline_get_details**](TextPipelinesApi.md#text_pipeline_get_details) | **GET** /nlu/v2/text_pipelines/{instance_name} | Get details of named instance.
[**text_pipeline_get_details_all**](TextPipelinesApi.md#text_pipeline_get_details_all) | **GET** /nlu/v2/text_pipelines | Get list of text pipelines.
[**text_pipeline_get_models**](TextPipelinesApi.md#text_pipeline_get_models) | **GET** /nlu/v2/text_pipelines/{instance_name}/models | Get list of models.
[**text_pipeline_get_params**](TextPipelinesApi.md#text_pipeline_get_params) | **GET** /nlu/v2/text_pipelines/{instance_name}/params | Get the editable model parameters of named text pipeline.
[**text_pipeline_retrieve**](TextPipelinesApi.md#text_pipeline_retrieve) | **POST** /nlu/v2/text_pipelines/{instance_name}/retrieve | Run the text pipeline and return the results.
[**text_pipeline_set_params**](TextPipelinesApi.md#text_pipeline_set_params) | **POST** /nlu/v2/text_pipelines/{instance_name}/params | Set the model parameters of named text pipeline.
[**text_pipeline_update_models**](TextPipelinesApi.md#text_pipeline_update_models) | **PUT** /nlu/v2/text_pipelines/{instance_name}/models | Update pipeline models by UUID.
[**text_pipeline_vaporise**](TextPipelinesApi.md#text_pipeline_vaporise) | **POST** /nlu/v2/text_pipelines/{instance_name}/vaporise | Vaporise the named pipeline.


# **text_pipeline_add_models**
> list[PipelineModel] text_pipeline_add_models(instance_name, pipeline_model_list, x_caller=x_caller)

Add list of models.

Add models to named text pipeline. Returns the samples added to the instance.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
pipeline_model_list = [feersum_nlu.PipelineModel()] # list[PipelineModel] | List of models to add.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add list of models.
    api_response = api_instance.text_pipeline_add_models(instance_name, pipeline_model_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_add_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **pipeline_model_list** | [**list[PipelineModel]**](PipelineModel.md)| List of models to add. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[PipelineModel]**](PipelineModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_create**
> TextPipelineInstanceDetail text_pipeline_create(create_details, x_caller=x_caller)

Create a text pipeline.

Create a new text pipeline or reload one from the trash. Returns the details of the instance.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.TextPipelineCreateDetails() # TextPipelineCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create a text pipeline.
    api_response = api_instance.text_pipeline_create(create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**TextPipelineCreateDetails**](TextPipelineCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextPipelineInstanceDetail**](TextPipelineInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_create_from_path**
> TextPipelineInstanceDetail text_pipeline_create_from_path(instance_name, create_details, x_caller=x_caller)

Create a text pipeline.

Create a new text pipeline or reload one from the trash. Returns the details of the instance.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
create_details = feersum_nlu.TextPipelineCreateDetails() # TextPipelineCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create a text pipeline.
    api_response = api_instance.text_pipeline_create_from_path(instance_name, create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_create_from_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **create_details** | [**TextPipelineCreateDetails**](TextPipelineCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextPipelineInstanceDetail**](TextPipelineInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_del**
> TextPipelineInstanceDetail text_pipeline_del(instance_name, x_caller=x_caller)

Delete named instance.

Delete and return the details of the named text pipeline instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.text_pipeline_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextPipelineInstanceDetail**](TextPipelineInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_del_models**
> list[PipelineModel] text_pipeline_del_models(instance_name, pipeline_model_list, x_caller=x_caller)

Delete list of models.

Delete the listed models of the named text pipeline. Returns the deleted names.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
pipeline_model_list = [feersum_nlu.PipelineModel()] # list[PipelineModel] | List of pipeline models.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete list of models.
    api_response = api_instance.text_pipeline_del_models(instance_name, pipeline_model_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_del_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **pipeline_model_list** | [**list[PipelineModel]**](PipelineModel.md)| List of pipeline models. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[PipelineModel]**](PipelineModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_del_models_all**
> list[PipelineModel] text_pipeline_del_models_all(instance_name, x_caller=x_caller)

Delete all models from the pipeline.

Delete all models from the named pipeline. Returns the deleted models.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all models from the pipeline.
    api_response = api_instance.text_pipeline_del_models_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_del_models_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[PipelineModel]**](PipelineModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_get_details**
> TextPipelineInstanceDetail text_pipeline_get_details(instance_name, x_caller=x_caller)

Get details of named instance.

Get the details of the named text pipeline instance.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.text_pipeline_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextPipelineInstanceDetail**](TextPipelineInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_get_details_all**
> list[TextPipelineInstanceDetail] text_pipeline_get_details_all(x_caller=x_caller)

Get list of text pipelines.

Get the list of text pipelines.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of text pipelines.
    api_response = api_instance.text_pipeline_get_details_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[TextPipelineInstanceDetail]**](TextPipelineInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_get_models**
> list[PipelineModel] text_pipeline_get_models(instance_name, x_caller=x_caller, index=index, len=len)

Get list of models.

Get the models of the named text pipeline.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get list of models.
    api_response = api_instance.text_pipeline_get_models(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_get_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 
 **index** | **int**| The sample index to start from. | [optional] 
 **len** | **int**| The number of samples to return. | [optional] 

### Return type

[**list[PipelineModel]**](PipelineModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_get_params**
> PipelineParams text_pipeline_get_params(instance_name, x_caller=x_caller)

Get the editable model parameters of named text pipeline.

Get the editable model parameters of named text pipeline.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the editable model parameters of named text pipeline.
    api_response = api_instance.text_pipeline_get_params(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_get_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**PipelineParams**](PipelineParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_retrieve**
> TextPipelineResponse text_pipeline_retrieve(instance_name, text_input, x_caller=x_caller)

Run the text pipeline and return the results.

Run the text pipeline and return the results.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Run the text pipeline and return the results.
    api_response = api_instance.text_pipeline_retrieve(instance_name, text_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextPipelineResponse**](TextPipelineResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_set_params**
> TextPipelineInstanceDetail text_pipeline_set_params(instance_name, pipeline_params, x_caller=x_caller)

Set the model parameters of named text pipeline.

Set the model parameters of named text pipeline.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
pipeline_params = feersum_nlu.PipelineParams() # PipelineParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Set the model parameters of named text pipeline.
    api_response = api_instance.text_pipeline_set_params(instance_name, pipeline_params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **pipeline_params** | [**PipelineParams**](PipelineParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextPipelineInstanceDetail**](TextPipelineInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_update_models**
> list[PipelineModel] text_pipeline_update_models(instance_name, pipeline_model_list, x_caller=x_caller)

Update pipeline models by UUID.

Update models of the named text pipeline. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
pipeline_model_list = [feersum_nlu.PipelineModel()] # list[PipelineModel] | List of pipeline models to update. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update pipeline models by UUID.
    api_response = api_instance.text_pipeline_update_models(instance_name, pipeline_model_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_update_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **pipeline_model_list** | [**list[PipelineModel]**](PipelineModel.md)| List of pipeline models to update. A sample&#39;s UUIDs is used to uniquely identify it. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[PipelineModel]**](PipelineModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_pipeline_vaporise**
> TextPipelineInstanceDetail text_pipeline_vaporise(instance_name, x_caller=x_caller)

Vaporise the named pipeline.

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
api_instance = feersum_nlu.TextPipelinesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named pipeline.
    api_response = api_instance.text_pipeline_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextPipelinesApi->text_pipeline_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextPipelineInstanceDetail**](TextPipelineInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

