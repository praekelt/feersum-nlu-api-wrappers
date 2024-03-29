# feersum_nlu.CrfEntityExtractorsApi

All URIs are relative to *https://nlu.qa.feersum.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crf_entity_extractor_add_testing_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_add_testing_samples) | **POST** /nlu/v2/crf_entity_extractors/{instance_name}/testing_samples | Add testing samples.
[**crf_entity_extractor_add_training_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_add_training_samples) | **POST** /nlu/v2/crf_entity_extractors/{instance_name}/training_samples | Add training samples.
[**crf_entity_extractor_create**](CrfEntityExtractorsApi.md#crf_entity_extractor_create) | **POST** /nlu/v2/crf_entity_extractors | Create a crf entity extractor.
[**crf_entity_extractor_del**](CrfEntityExtractorsApi.md#crf_entity_extractor_del) | **DELETE** /nlu/v2/crf_entity_extractors/{instance_name} | Delete named instance.
[**crf_entity_extractor_del_testing_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_del_testing_samples) | **DELETE** /nlu/v2/crf_entity_extractors/{instance_name}/testing_samples | Delete testing samples.
[**crf_entity_extractor_del_testing_samples_all**](CrfEntityExtractorsApi.md#crf_entity_extractor_del_testing_samples_all) | **DELETE** /nlu/v2/crf_entity_extractors/{instance_name}/testing_samples_all | Delete all testing samples.
[**crf_entity_extractor_del_training_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_del_training_samples) | **DELETE** /nlu/v2/crf_entity_extractors/{instance_name}/training_samples | Delete training samples.
[**crf_entity_extractor_del_training_samples_all**](CrfEntityExtractorsApi.md#crf_entity_extractor_del_training_samples_all) | **DELETE** /nlu/v2/crf_entity_extractors/{instance_name}/training_samples_all | Delete all training samples.
[**crf_entity_extractor_get_details**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_details) | **GET** /nlu/v2/crf_entity_extractors/{instance_name} | Get details of named instance.
[**crf_entity_extractor_get_details_all**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_details_all) | **GET** /nlu/v2/crf_entity_extractors | Get list of crf entity extractors.
[**crf_entity_extractor_get_labels**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_labels) | **GET** /nlu/v2/crf_entity_extractors/{instance_name}/labels | Get list of possible labels.
[**crf_entity_extractor_get_params**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_params) | **GET** /nlu/v2/crf_entity_extractors/{instance_name}/params | Get the editable model parameters of named crf entity extractor.
[**crf_entity_extractor_get_testing_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_testing_samples) | **GET** /nlu/v2/crf_entity_extractors/{instance_name}/testing_samples | Get testing samples.
[**crf_entity_extractor_get_training_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_training_samples) | **GET** /nlu/v2/crf_entity_extractors/{instance_name}/training_samples | Get training samples.
[**crf_entity_extractor_retrieve**](CrfEntityExtractorsApi.md#crf_entity_extractor_retrieve) | **POST** /nlu/v2/crf_entity_extractors/{instance_name}/retrieve | Predict which entities was mentioned.
[**crf_entity_extractor_set_params**](CrfEntityExtractorsApi.md#crf_entity_extractor_set_params) | **POST** /nlu/v2/crf_entity_extractors/{instance_name}/params | Set the model parameters of named crf entity extractor.
[**crf_entity_extractor_test**](CrfEntityExtractorsApi.md#crf_entity_extractor_test) | **POST** /nlu/v2/crf_entity_extractors/{instance_name}/test | Test the named crf entity extractor.
[**crf_entity_extractor_train**](CrfEntityExtractorsApi.md#crf_entity_extractor_train) | **POST** /nlu/v2/crf_entity_extractors/{instance_name}/train | Train the named crf extractor.
[**crf_entity_extractor_update_testing_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_update_testing_samples) | **PUT** /nlu/v2/crf_entity_extractors/{instance_name}/testing_samples | Update testing samples by UUID.
[**crf_entity_extractor_update_training_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_update_training_samples) | **PUT** /nlu/v2/crf_entity_extractors/{instance_name}/training_samples | Update training samples by UUID.
[**crf_entity_extractor_vaporise**](CrfEntityExtractorsApi.md#crf_entity_extractor_vaporise) | **POST** /nlu/v2/crf_entity_extractors/{instance_name}/vaporise | Vaporise the named model.


# **crf_entity_extractor_add_testing_samples**
> list[CrfSample] crf_entity_extractor_add_testing_samples(instance_name, crf_sample_list, x_caller=x_caller)

Add testing samples.

Add testing samples to named extractor. Returns the samples added to the instance.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add testing samples.
    api_response = api_instance.crf_entity_extractor_add_testing_samples(instance_name, crf_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_add_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_add_training_samples**
> list[CrfSample] crf_entity_extractor_add_training_samples(instance_name, crf_sample_list, x_caller=x_caller)

Add training samples.

Add training samples to named extractor. Returns the samples added to the instance.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add training samples.
    api_response = api_instance.crf_entity_extractor_add_training_samples(instance_name, crf_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_add_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_create**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_create(create_details, x_caller=x_caller)

Create a crf entity extractor.

Create a new crf entity extractor or reload one from the trash.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.CrfEntityExtractorCreateDetails() # CrfEntityExtractorCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create a crf entity extractor.
    api_response = api_instance.crf_entity_extractor_create(create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**CrfEntityExtractorCreateDetails**](CrfEntityExtractorCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_del(instance_name, x_caller=x_caller)

Delete named instance.

Delete and get the details of the named crf entity extractor instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.crf_entity_extractor_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del_testing_samples**
> list[CrfSample] crf_entity_extractor_del_testing_samples(instance_name, crf_sample_list, x_caller=x_caller)

Delete testing samples.

Delete the listed testing samples of the named extractor. Returns the deleted samples.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete testing samples.
    api_response = api_instance.crf_entity_extractor_del_testing_samples(instance_name, crf_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del_testing_samples_all**
> list[CrfSample] crf_entity_extractor_del_testing_samples_all(instance_name, x_caller=x_caller)

Delete all testing samples.

Delete all testing samples of the named extractor. Returns the deleted samples.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all testing samples.
    api_response = api_instance.crf_entity_extractor_del_testing_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del_testing_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del_training_samples**
> list[CrfSample] crf_entity_extractor_del_training_samples(instance_name, crf_sample_list, x_caller=x_caller)

Delete training samples.

Delete the listed training samples of the named extractor. Returns the deleted samples.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete training samples.
    api_response = api_instance.crf_entity_extractor_del_training_samples(instance_name, crf_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del_training_samples_all**
> list[CrfSample] crf_entity_extractor_del_training_samples_all(instance_name, x_caller=x_caller)

Delete all training samples.

Delete all training samples of the named extractor. Returns the deleted samples.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all training samples.
    api_response = api_instance.crf_entity_extractor_del_training_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del_training_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_details**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_get_details(instance_name, x_caller=x_caller)

Get details of named instance.

Get the details of the named crf entity extractor instance.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.crf_entity_extractor_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_details_all**
> list[CrfEntityExtractorInstanceDetail] crf_entity_extractor_get_details_all(x_caller=x_caller)

Get list of crf entity extractors.

Get the list of crf entity extractors.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of crf entity extractors.
    api_response = api_instance.crf_entity_extractor_get_details_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfEntityExtractorInstanceDetail]**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_labels**
> list[ClassLabel] crf_entity_extractor_get_labels(instance_name, x_caller=x_caller)

Get list of possible labels.

Returns the extractor's list of possible entity labels.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of possible labels.
    api_response = api_instance.crf_entity_extractor_get_labels(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_labels: %s\n" % e)
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

# **crf_entity_extractor_get_params**
> ModelParams crf_entity_extractor_get_params(instance_name, x_caller=x_caller)

Get the editable model parameters of named crf entity extractor.

Get the editable model parameters of named crf entity extractor.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the editable model parameters of named crf entity extractor.
    api_response = api_instance.crf_entity_extractor_get_params(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_params: %s\n" % e)
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

# **crf_entity_extractor_get_testing_samples**
> list[CrfSample] crf_entity_extractor_get_testing_samples(instance_name, x_caller=x_caller, index=index, len=len)

Get testing samples.

Get the testing samples of the named extractor.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get testing samples.
    api_response = api_instance.crf_entity_extractor_get_testing_samples(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 
 **index** | **int**| The sample index to start from. | [optional] 
 **len** | **int**| The number of samples to return. | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_training_samples**
> list[CrfSample] crf_entity_extractor_get_training_samples(instance_name, x_caller=x_caller, index=index, len=len)

Get training samples.

Get the training samples of the named extractor.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get training samples.
    api_response = api_instance.crf_entity_extractor_get_training_samples(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 
 **index** | **int**| The sample index to start from. | [optional] 
 **len** | **int**| The number of samples to return. | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_retrieve**
> list[CrfEntity] crf_entity_extractor_retrieve(instance_name, text_input, x_caller=x_caller)

Predict which entities was mentioned.

Predict which entities was mentioned.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Predict which entities was mentioned.
    api_response = api_instance.crf_entity_extractor_retrieve(instance_name, text_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfEntity]**](CrfEntity.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_set_params**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_set_params(instance_name, model_params, x_caller=x_caller)

Set the model parameters of named crf entity extractor.

Set the model parameters of named crf entity extractor.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Set the model parameters of named crf entity extractor.
    api_response = api_instance.crf_entity_extractor_set_params(instance_name, model_params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_test**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_test(instance_name, test_details, x_caller=x_caller)

Test the named crf entity extractor.

Test the named crf entity extractor with the testing data already provided. Returns the details of the instance.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
test_details = feersum_nlu.TestDetails() # TestDetails | The arguments provided to the test operation.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Test the named crf entity extractor.
    api_response = api_instance.crf_entity_extractor_test(instance_name, test_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **test_details** | [**TestDetails**](TestDetails.md)| The arguments provided to the test operation. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_train**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_train(instance_name, train_details, x_caller=x_caller)

Train the named crf extractor.

Train the named crf extractor with the training and testing data already provided. Returns the updated instance details.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Train the named crf extractor.
    api_response = api_instance.crf_entity_extractor_train(instance_name, train_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **train_details** | [**TrainDetails**](TrainDetails.md)| The arguments provided to the train operation. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_update_testing_samples**
> list[CrfSample] crf_entity_extractor_update_testing_samples(instance_name, crf_sample_list, x_caller=x_caller)

Update testing samples by UUID.

Update training samples of the named entity extractor. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update testing samples by UUID.
    api_response = api_instance.crf_entity_extractor_update_testing_samples(instance_name, crf_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_update_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. A sample&#39;s UUIDs is used to uniquely identify it. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_update_training_samples**
> list[CrfSample] crf_entity_extractor_update_training_samples(instance_name, crf_sample_list, x_caller=x_caller)

Update training samples by UUID.

Update training samples of the named entity extractor. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update training samples by UUID.
    api_response = api_instance.crf_entity_extractor_update_training_samples(instance_name, crf_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_update_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. A sample&#39;s UUIDs is used to uniquely identify it. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_vaporise**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_vaporise(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named model.
    api_response = api_instance.crf_entity_extractor_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

