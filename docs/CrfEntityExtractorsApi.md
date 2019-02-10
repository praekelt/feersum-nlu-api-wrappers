# feersum_nlu.CrfEntityExtractorsApi

All URIs are relative to *https://nlu.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crf_entity_extractor_add_testing_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_add_testing_samples) | **POST** /crf_entity_extractors/{instance_name}/testing_samples | Add testing samples.
[**crf_entity_extractor_add_training_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_add_training_samples) | **POST** /crf_entity_extractors/{instance_name}/training_samples | Add training samples.
[**crf_entity_extractor_create**](CrfEntityExtractorsApi.md#crf_entity_extractor_create) | **POST** /crf_entity_extractors | Create a crf entity extractor.
[**crf_entity_extractor_del**](CrfEntityExtractorsApi.md#crf_entity_extractor_del) | **DELETE** /crf_entity_extractors/{instance_name} | Delete named instance.
[**crf_entity_extractor_del_testing_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_del_testing_samples) | **DELETE** /crf_entity_extractors/{instance_name}/testing_samples | Delete testing samples.
[**crf_entity_extractor_del_testing_samples_all**](CrfEntityExtractorsApi.md#crf_entity_extractor_del_testing_samples_all) | **DELETE** /crf_entity_extractors/{instance_name}/testing_samples_all | Delete all testing samples.
[**crf_entity_extractor_del_training_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_del_training_samples) | **DELETE** /crf_entity_extractors/{instance_name}/training_samples | Delete training samples.
[**crf_entity_extractor_del_training_samples_all**](CrfEntityExtractorsApi.md#crf_entity_extractor_del_training_samples_all) | **DELETE** /crf_entity_extractors/{instance_name}/training_samples_all | Delete all training samples.
[**crf_entity_extractor_get_details**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_details) | **GET** /crf_entity_extractors/{instance_name} | Get details of named instance.
[**crf_entity_extractor_get_details_all**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_details_all) | **GET** /crf_entity_extractors | Get list of loaded crf entity extractors.
[**crf_entity_extractor_get_labels**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_labels) | **GET** /crf_entity_extractors/{instance_name}/get_labels | Get list of possible labels.
[**crf_entity_extractor_get_params**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_params) | **GET** /crf_entity_extractors/{instance_name}/params | Get the editable model parameters of named crf entity extractor.
[**crf_entity_extractor_get_testing_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_testing_samples) | **GET** /crf_entity_extractors/{instance_name}/testing_samples | Get testing samples.
[**crf_entity_extractor_get_training_samples**](CrfEntityExtractorsApi.md#crf_entity_extractor_get_training_samples) | **GET** /crf_entity_extractors/{instance_name}/training_samples | Get training samples.
[**crf_entity_extractor_retrieve**](CrfEntityExtractorsApi.md#crf_entity_extractor_retrieve) | **POST** /crf_entity_extractors/{instance_name}/retrieve | Predict which entities was mentioned.
[**crf_entity_extractor_set_params**](CrfEntityExtractorsApi.md#crf_entity_extractor_set_params) | **POST** /crf_entity_extractors/{instance_name}/params | Set the model parameters of named crf entity extractor.
[**crf_entity_extractor_train**](CrfEntityExtractorsApi.md#crf_entity_extractor_train) | **POST** /crf_entity_extractors/{instance_name}/train | Train the named crf extractor.
[**crf_entity_extractor_vaporise**](CrfEntityExtractorsApi.md#crf_entity_extractor_vaporise) | **POST** /crf_entity_extractors/{instance_name}/vaporise | Vaporise the named model.


# **crf_entity_extractor_add_testing_samples**
> TotalSamples crf_entity_extractor_add_testing_samples(instance_name, crf_sample_list)

Add testing samples.

Add testing samples to named extractor. Returns the extractor's updated number of testing samples.

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
instance_name = 'instance_name_example' # str | The name of the model instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples.

try:
    # Add testing samples.
    api_response = api_instance.crf_entity_extractor_add_testing_samples(instance_name, crf_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_add_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. | 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_add_training_samples**
> TotalSamples crf_entity_extractor_add_training_samples(instance_name, crf_sample_list)

Add training samples.

Add training samples to named extractor. Returns the extractor's updated number of training samples.

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
instance_name = 'instance_name_example' # str | The name of the model instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples.

try:
    # Add training samples.
    api_response = api_instance.crf_entity_extractor_add_training_samples(instance_name, crf_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_add_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. | 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_create**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_create(create_details)

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

try:
    # Create a crf entity extractor.
    api_response = api_instance.crf_entity_extractor_create(create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**CrfEntityExtractorCreateDetails**](CrfEntityExtractorCreateDetails.md)| The details of the instance to create. | 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_del(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete named instance.
    api_response = api_instance.crf_entity_extractor_del(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del_testing_samples**
> list[CrfSample] crf_entity_extractor_del_testing_samples(instance_name, crf_sample_list)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples.

try:
    # Delete testing samples.
    api_response = api_instance.crf_entity_extractor_del_testing_samples(instance_name, crf_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. | 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del_testing_samples_all**
> list[CrfSample] crf_entity_extractor_del_testing_samples_all(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete all testing samples.
    api_response = api_instance.crf_entity_extractor_del_testing_samples_all(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del_testing_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del_training_samples**
> list[CrfSample] crf_entity_extractor_del_training_samples(instance_name, crf_sample_list)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
crf_sample_list = [feersum_nlu.CrfSample()] # list[CrfSample] | List of crf samples.

try:
    # Delete training samples.
    api_response = api_instance.crf_entity_extractor_del_training_samples(instance_name, crf_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **crf_sample_list** | [**list[CrfSample]**](CrfSample.md)| List of crf samples. | 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_del_training_samples_all**
> list[CrfSample] crf_entity_extractor_del_training_samples_all(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete all training samples.
    api_response = api_instance.crf_entity_extractor_del_training_samples_all(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_del_training_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_details**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_get_details(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get details of named instance.
    api_response = api_instance.crf_entity_extractor_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_details_all**
> list[CrfEntityExtractorInstanceDetail] crf_entity_extractor_get_details_all()

Get list of loaded crf entity extractors.

Get the list of loaded crf entity extractors.

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

try:
    # Get list of loaded crf entity extractors.
    api_response = api_instance.crf_entity_extractor_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_details_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CrfEntityExtractorInstanceDetail]**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_labels**
> list[ClassLabel] crf_entity_extractor_get_labels(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get list of possible labels.
    api_response = api_instance.crf_entity_extractor_get_labels(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[ClassLabel]**](ClassLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_params**
> ModelParams crf_entity_extractor_get_params(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get the editable model parameters of named crf entity extractor.
    api_response = api_instance.crf_entity_extractor_get_params(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**ModelParams**](ModelParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_testing_samples**
> list[CrfSample] crf_entity_extractor_get_testing_samples(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get testing samples.
    api_response = api_instance.crf_entity_extractor_get_testing_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_get_training_samples**
> list[CrfSample] crf_entity_extractor_get_training_samples(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get training samples.
    api_response = api_instance.crf_entity_extractor_get_training_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_get_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[CrfSample]**](CrfSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_retrieve**
> list[CrfEntity] crf_entity_extractor_retrieve(instance_name, text_input)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try:
    # Predict which entities was mentioned.
    api_response = api_instance.crf_entity_extractor_retrieve(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 

### Return type

[**list[CrfEntity]**](CrfEntity.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_set_params**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_set_params(instance_name, model_params)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.

try:
    # Set the model parameters of named crf entity extractor.
    api_response = api_instance.crf_entity_extractor_set_params(instance_name, model_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_train**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_train(instance_name, train_details)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.

try:
    # Train the named crf extractor.
    api_response = api_instance.crf_entity_extractor_train(instance_name, train_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **train_details** | [**TrainDetails**](TrainDetails.md)| The arguments provided to the train operation. | 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crf_entity_extractor_vaporise**
> CrfEntityExtractorInstanceDetail crf_entity_extractor_vaporise(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Vaporise the named model.
    api_response = api_instance.crf_entity_extractor_vaporise(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrfEntityExtractorsApi->crf_entity_extractor_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**CrfEntityExtractorInstanceDetail**](CrfEntityExtractorInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

