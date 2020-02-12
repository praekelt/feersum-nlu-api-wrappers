# feersum_nlu.TextDatasetsApi

All URIs are relative to *https://nlu.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_dataset_add_samples**](TextDatasetsApi.md#text_dataset_add_samples) | **POST** /text_datasets/{instance_name}/samples | Add samples.
[**text_dataset_create**](TextDatasetsApi.md#text_dataset_create) | **POST** /text_datasets | Create a text dataset.
[**text_dataset_del**](TextDatasetsApi.md#text_dataset_del) | **DELETE** /text_datasets/{instance_name} | Delete named instance.
[**text_dataset_del_samples**](TextDatasetsApi.md#text_dataset_del_samples) | **DELETE** /text_datasets/{instance_name}/samples | Delete samples.
[**text_dataset_del_samples_all**](TextDatasetsApi.md#text_dataset_del_samples_all) | **DELETE** /text_datasets/{instance_name}/samples_all | Delete all samples.
[**text_dataset_get_details**](TextDatasetsApi.md#text_dataset_get_details) | **GET** /text_datasets/{instance_name} | Get details of named instance.
[**text_dataset_get_details_all**](TextDatasetsApi.md#text_dataset_get_details_all) | **GET** /text_datasets | Get list of loaded text datasets.
[**text_dataset_get_labels**](TextDatasetsApi.md#text_dataset_get_labels) | **GET** /text_datasets/{instance_name}/labels | Get list of possible labels.
[**text_dataset_get_params**](TextDatasetsApi.md#text_dataset_get_params) | **GET** /text_datasets/{instance_name}/params | Get the editable model parameters of named text dataset.
[**text_dataset_get_samples**](TextDatasetsApi.md#text_dataset_get_samples) | **GET** /text_datasets/{instance_name}/samples | Get samples.
[**text_dataset_set_params**](TextDatasetsApi.md#text_dataset_set_params) | **POST** /text_datasets/{instance_name}/params | Set the model parameters of named text dataset.
[**text_dataset_update_samples**](TextDatasetsApi.md#text_dataset_update_samples) | **PUT** /text_datasets/{instance_name}/samples | Update samples by UUID.
[**text_dataset_vaporise**](TextDatasetsApi.md#text_dataset_vaporise) | **POST** /text_datasets/{instance_name}/vaporise | Vaporise the named model.


# **text_dataset_add_samples**
> list[LabelledTextSample] text_dataset_add_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Add samples.

Add samples to named text dataset. Returns the samples added to the model.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add samples.
    api_response = api_instance.text_dataset_add_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_add_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_create**
> TextDatasetInstanceDetail text_dataset_create(create_details, x_caller=x_caller)

Create a text dataset.

Create a new text dataset or reload one from the trash. Returns the details of the new or loaded instance.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.TextDatasetCreateDetails() # TextDatasetCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create a text dataset.
    api_response = api_instance.text_dataset_create(create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**TextDatasetCreateDetails**](TextDatasetCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextDatasetInstanceDetail**](TextDatasetInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_del**
> TextDatasetInstanceDetail text_dataset_del(instance_name, x_caller=x_caller)

Delete named instance.

Delete and return the details of the named text dataset instance. Deleted instances can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.text_dataset_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextDatasetInstanceDetail**](TextDatasetInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_del_samples**
> list[LabelledTextSample] text_dataset_del_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Delete samples.

Delete the listed samples of the named text dataset. Returns the deleted samples.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete samples.
    api_response = api_instance.text_dataset_del_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_del_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_del_samples_all**
> list[LabelledTextSample] text_dataset_del_samples_all(instance_name, x_caller=x_caller)

Delete all samples.

Delete all samples of the named text dataset. Returns the deleted samples.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all samples.
    api_response = api_instance.text_dataset_del_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_del_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_get_details**
> TextDatasetInstanceDetail text_dataset_get_details(instance_name, x_caller=x_caller)

Get details of named instance.

Get the details of the named text dataset instance.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.text_dataset_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextDatasetInstanceDetail**](TextDatasetInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_get_details_all**
> list[TextDatasetInstanceDetail] text_dataset_get_details_all(x_caller=x_caller)

Get list of loaded text datasets.

Get the list of loaded text datasets.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of loaded text datasets.
    api_response = api_instance.text_dataset_get_details_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[TextDatasetInstanceDetail]**](TextDatasetInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_get_labels**
> list[ClassLabel] text_dataset_get_labels(instance_name, x_caller=x_caller)

Get list of possible labels.

Returns the dataset's list of possible class labels.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of possible labels.
    api_response = api_instance.text_dataset_get_labels(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[ClassLabel]**](ClassLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_get_params**
> ModelParams text_dataset_get_params(instance_name, x_caller=x_caller)

Get the editable model parameters of named text dataset.

Get the editable model parameters of named text dataset.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the editable model parameters of named text dataset.
    api_response = api_instance.text_dataset_get_params(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_get_params: %s\n" % e)
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

# **text_dataset_get_samples**
> list[LabelledTextSample] text_dataset_get_samples(instance_name, x_caller=x_caller, index=index, len=len, sub_sample=sub_sample)

Get samples.

Get the samples of the named text dataset.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)
sub_sample = 56 # int | If provided, the size of the shuffled sub-sample to return. (optional)

try:
    # Get samples.
    api_response = api_instance.text_dataset_get_samples(instance_name, x_caller=x_caller, index=index, len=len, sub_sample=sub_sample)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_get_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **index** | **int**| The sample index to start from. | [optional] 
 **len** | **int**| The number of samples to return. | [optional] 
 **sub_sample** | **int**| If provided, the size of the shuffled sub-sample to return. | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_set_params**
> TextDatasetInstanceDetail text_dataset_set_params(instance_name, model_params, x_caller=x_caller)

Set the model parameters of named text dataset.

Set the model parameters of named text dataset.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Set the model parameters of named text dataset.
    api_response = api_instance.text_dataset_set_params(instance_name, model_params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextDatasetInstanceDetail**](TextDatasetInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_update_samples**
> list[LabelledTextSample] text_dataset_update_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Update samples by UUID.

Update samples of the named text dataset. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of text samples to update. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update samples by UUID.
    api_response = api_instance.text_dataset_update_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_update_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of text samples to update. A sample&#39;s UUIDs is used to uniquely identify it. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_dataset_vaporise**
> TextDatasetInstanceDetail text_dataset_vaporise(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named model.
    api_response = api_instance.text_dataset_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextDatasetsApi->text_dataset_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextDatasetInstanceDetail**](TextDatasetInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

