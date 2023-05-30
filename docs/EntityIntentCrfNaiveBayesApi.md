# feersum_nlu.EntityIntentCrfNaiveBayesApi

All URIs are relative to *https://nlu.qa.feersum.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entity_intent_crf_naive_bayes_add_testing_samples**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_add_testing_samples) | **POST** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/testing_samples | Add testing samples.
[**entity_intent_crf_naive_bayes_add_training_samples**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_add_training_samples) | **POST** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/training_samples | Add training samples.
[**entity_intent_crf_naive_bayes_create**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_create) | **POST** /nlu/v2/entity_intent_crf_naive_bayes | Create an entity(CRF)_intent(Naive Bayes) model.
[**entity_intent_crf_naive_bayes_del**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_del) | **DELETE** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name} | Delete named instance.
[**entity_intent_crf_naive_bayes_del_testing_samples**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_del_testing_samples) | **DELETE** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/testing_samples | Delete testing samples.
[**entity_intent_crf_naive_bayes_del_testing_samples_all**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_del_testing_samples_all) | **DELETE** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/testing_samples_all | Delete all testing samples.
[**entity_intent_crf_naive_bayes_del_training_samples**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_del_training_samples) | **DELETE** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/training_samples | Delete training samples.
[**entity_intent_crf_naive_bayes_del_training_samples_all**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_del_training_samples_all) | **DELETE** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/training_samples_all | Delete all training samples.
[**entity_intent_crf_naive_bayes_get_details**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_get_details) | **GET** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name} | Get details of named instance.
[**entity_intent_crf_naive_bayes_get_details_all**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_get_details_all) | **GET** /nlu/v2/entity_intent_crf_naive_bayes | Get list of entity(CRF)_intent(Naive Bayes) models.
[**entity_intent_crf_naive_bayes_get_labels**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_get_labels) | **GET** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/labels | Get list of possible labels.
[**entity_intent_crf_naive_bayes_get_params**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_get_params) | **GET** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/params | Get the editable model parameters of named entity(CRF)_intent(Naive Bayes) model.
[**entity_intent_crf_naive_bayes_get_testing_samples**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_get_testing_samples) | **GET** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/testing_samples | Get testing samples.
[**entity_intent_crf_naive_bayes_get_training_samples**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_get_training_samples) | **GET** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/training_samples | Get training samples.
[**entity_intent_crf_naive_bayes_retrieve**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_retrieve) | **POST** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/retrieve | Classify crf_intent.
[**entity_intent_crf_naive_bayes_set_params**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_set_params) | **POST** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/params | Set the model parameters of named entity(CRF)_intent(Naive Bayes) model.
[**entity_intent_crf_naive_bayes_test**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_test) | **POST** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/test | Test the named entity(CRF)_intent(Naive Bayes) model.
[**entity_intent_crf_naive_bayes_train**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_train) | **POST** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/train | Train the named entity(CRF)_intent(Naive Bayes) model.
[**entity_intent_crf_naive_bayes_update_testing_samples**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_update_testing_samples) | **PUT** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/testing_samples | Update testning samples by UUID.
[**entity_intent_crf_naive_bayes_update_training_samples**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_update_training_samples) | **PUT** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/training_samples | Update training samples by UUID.
[**entity_intent_crf_naive_bayes_vaporise**](EntityIntentCrfNaiveBayesApi.md#entity_intent_crf_naive_bayes_vaporise) | **POST** /nlu/v2/entity_intent_crf_naive_bayes/{instance_name}/vaporise | Vaporise the named model.


# **entity_intent_crf_naive_bayes_add_testing_samples**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_add_testing_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)

Add testing samples.

Add testing samples to named entity(CRF)_intent(Naive Bayes) model. Returns the samples added to the instance.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
entity_intent_sample_list = [feersum_nlu.EntityIntentSample()] # list[EntityIntentSample] | List of entity_intent samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add testing samples.
    api_response = api_instance.entity_intent_crf_naive_bayes_add_testing_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_add_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **entity_intent_sample_list** | [**list[EntityIntentSample]**](EntityIntentSample.md)| List of entity_intent samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_add_training_samples**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_add_training_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)

Add training samples.

Add training samples to named entity(CRF)_intent(Naive Bayes) model. Returns the samples added to the instance.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
entity_intent_sample_list = [feersum_nlu.EntityIntentSample()] # list[EntityIntentSample] | List of entity_intent samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add training samples.
    api_response = api_instance.entity_intent_crf_naive_bayes_add_training_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_add_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **entity_intent_sample_list** | [**list[EntityIntentSample]**](EntityIntentSample.md)| List of entity_intent samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_create**
> EntityIntentCrfNaiveBayesInstanceDetail entity_intent_crf_naive_bayes_create(create_details, x_caller=x_caller)

Create an entity(CRF)_intent(Naive Bayes) model.

Create a new entity(CRF)_intent(Naive Bayes) model or reload one from the trash. Returns the details of the instance.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.EntityIntentCrfNaiveBayesCreateDetails() # EntityIntentCrfNaiveBayesCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create an entity(CRF)_intent(Naive Bayes) model.
    api_response = api_instance.entity_intent_crf_naive_bayes_create(create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**EntityIntentCrfNaiveBayesCreateDetails**](EntityIntentCrfNaiveBayesCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**EntityIntentCrfNaiveBayesInstanceDetail**](EntityIntentCrfNaiveBayesInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_del**
> EntityIntentCrfNaiveBayesInstanceDetail entity_intent_crf_naive_bayes_del(instance_name, x_caller=x_caller)

Delete named instance.

Delete and return the details of the named entity(CRF)_intent(Naive Bayes) model instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.entity_intent_crf_naive_bayes_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**EntityIntentCrfNaiveBayesInstanceDetail**](EntityIntentCrfNaiveBayesInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_del_testing_samples**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_del_testing_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)

Delete testing samples.

Delete the listed testing samples of the named entity(CRF)_intent(Naive Bayes) model. Returns the deleted samples.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
entity_intent_sample_list = [feersum_nlu.EntityIntentSample()] # list[EntityIntentSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete testing samples.
    api_response = api_instance.entity_intent_crf_naive_bayes_del_testing_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_del_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **entity_intent_sample_list** | [**list[EntityIntentSample]**](EntityIntentSample.md)| List of labelled text samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_del_testing_samples_all**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_del_testing_samples_all(instance_name, x_caller=x_caller)

Delete all testing samples.

Delete all testing samples of the named entity(CRF)_intent(Naive Bayes) model. Returns the deleted samples.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all testing samples.
    api_response = api_instance.entity_intent_crf_naive_bayes_del_testing_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_del_testing_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_del_training_samples**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_del_training_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)

Delete training samples.

Delete the listed training samples of the named entity(CRF)_intent(Naive Bayes) model. Returns the deleted samples.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
entity_intent_sample_list = [feersum_nlu.EntityIntentSample()] # list[EntityIntentSample] | List of entity_intent samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete training samples.
    api_response = api_instance.entity_intent_crf_naive_bayes_del_training_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_del_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **entity_intent_sample_list** | [**list[EntityIntentSample]**](EntityIntentSample.md)| List of entity_intent samples. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_del_training_samples_all**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_del_training_samples_all(instance_name, x_caller=x_caller)

Delete all training samples.

Delete the listed training samples of the named entity(CRF)_intent(Naive Bayes) model. Returns the deleted samples.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all training samples.
    api_response = api_instance.entity_intent_crf_naive_bayes_del_training_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_del_training_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_get_details**
> EntityIntentCrfNaiveBayesInstanceDetail entity_intent_crf_naive_bayes_get_details(instance_name, x_caller=x_caller)

Get details of named instance.

Returns the details of the named entity(CRF)_intent(Naive Bayes) model instance.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.entity_intent_crf_naive_bayes_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**EntityIntentCrfNaiveBayesInstanceDetail**](EntityIntentCrfNaiveBayesInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_get_details_all**
> list[EntityIntentCrfNaiveBayesInstanceDetail] entity_intent_crf_naive_bayes_get_details_all(x_caller=x_caller)

Get list of entity(CRF)_intent(Naive Bayes) models.

Returns the list of entity(CRF)_intent(Naive Bayes) models.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of entity(CRF)_intent(Naive Bayes) models.
    api_response = api_instance.entity_intent_crf_naive_bayes_get_details_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentCrfNaiveBayesInstanceDetail]**](EntityIntentCrfNaiveBayesInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_get_labels**
> list[ClassLabel] entity_intent_crf_naive_bayes_get_labels(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of possible labels.
    api_response = api_instance.entity_intent_crf_naive_bayes_get_labels(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_get_labels: %s\n" % e)
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

# **entity_intent_crf_naive_bayes_get_params**
> ModelParams entity_intent_crf_naive_bayes_get_params(instance_name, x_caller=x_caller)

Get the editable model parameters of named entity(CRF)_intent(Naive Bayes) model.

Get the editable model parameters of named entity(CRF)_intent(Naive Bayes) model.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the editable model parameters of named entity(CRF)_intent(Naive Bayes) model.
    api_response = api_instance.entity_intent_crf_naive_bayes_get_params(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_get_params: %s\n" % e)
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

# **entity_intent_crf_naive_bayes_get_testing_samples**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_get_testing_samples(instance_name, x_caller=x_caller, index=index, len=len)

Get testing samples.

Returns the testing samples of the named entity(CRF)_intent(Naive Bayes) model.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get testing samples.
    api_response = api_instance.entity_intent_crf_naive_bayes_get_testing_samples(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_get_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 
 **index** | **int**| The sample index to start from. | [optional] 
 **len** | **int**| The number of samples to return. | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_get_training_samples**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_get_training_samples(instance_name, x_caller=x_caller, index=index, len=len)

Get training samples.

Returns the training samples of the named entity(CRF)_intent(Naive Bayes) model.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get training samples.
    api_response = api_instance.entity_intent_crf_naive_bayes_get_training_samples(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_get_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 
 **index** | **int**| The sample index to start from. | [optional] 
 **len** | **int**| The number of samples to return. | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_retrieve**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_retrieve(instance_name, text_input, x_caller=x_caller)

Classify crf_intent.

Classifies the crf_intent and returns a probability sorted list of classes.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Classify crf_intent.
    api_response = api_instance.entity_intent_crf_naive_bayes_retrieve(instance_name, text_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_set_params**
> EntityIntentCrfNaiveBayesInstanceDetail entity_intent_crf_naive_bayes_set_params(instance_name, model_params, x_caller=x_caller)

Set the model parameters of named entity(CRF)_intent(Naive Bayes) model.

Set the model parameters of named entity(CRF)_intent(Naive Bayes) model.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Set the model parameters of named entity(CRF)_intent(Naive Bayes) model.
    api_response = api_instance.entity_intent_crf_naive_bayes_set_params(instance_name, model_params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**EntityIntentCrfNaiveBayesInstanceDetail**](EntityIntentCrfNaiveBayesInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_test**
> EntityIntentCrfNaiveBayesInstanceDetail entity_intent_crf_naive_bayes_test(instance_name, test_details, x_caller=x_caller)

Test the named entity(CRF)_intent(Naive Bayes) model.

Test the named entity(CRF)_intent(Naive Bayes) model with the testing data already provided. Returns the details of the instance.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
test_details = feersum_nlu.TestDetails() # TestDetails | The arguments provided to the test operation.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Test the named entity(CRF)_intent(Naive Bayes) model.
    api_response = api_instance.entity_intent_crf_naive_bayes_test(instance_name, test_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **test_details** | [**TestDetails**](TestDetails.md)| The arguments provided to the test operation. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**EntityIntentCrfNaiveBayesInstanceDetail**](EntityIntentCrfNaiveBayesInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_train**
> EntityIntentCrfNaiveBayesInstanceDetail entity_intent_crf_naive_bayes_train(instance_name, train_details, x_caller=x_caller)

Train the named entity(CRF)_intent(Naive Bayes) model.

Train the named entity(CRF)_intent(Naive Bayes) model with the training and testing data already provided. Returns the updated instance details.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Train the named entity(CRF)_intent(Naive Bayes) model.
    api_response = api_instance.entity_intent_crf_naive_bayes_train(instance_name, train_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **train_details** | [**TrainDetails**](TrainDetails.md)| The arguments provided to the train operation. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**EntityIntentCrfNaiveBayesInstanceDetail**](EntityIntentCrfNaiveBayesInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_update_testing_samples**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_update_testing_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)

Update testning samples by UUID.

Update training samples of the named entity(CRF)_intent(Naive Bayes) model. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
entity_intent_sample_list = [feersum_nlu.EntityIntentSample()] # list[EntityIntentSample] | List of text samples to update. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update testning samples by UUID.
    api_response = api_instance.entity_intent_crf_naive_bayes_update_testing_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_update_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **entity_intent_sample_list** | [**list[EntityIntentSample]**](EntityIntentSample.md)| List of text samples to update. A sample&#39;s UUIDs is used to uniquely identify it. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_update_training_samples**
> list[EntityIntentSample] entity_intent_crf_naive_bayes_update_training_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)

Update training samples by UUID.

Update training samples of the named entity(CRF)_intent(Naive Bayes) model. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
entity_intent_sample_list = [feersum_nlu.EntityIntentSample()] # list[EntityIntentSample] | List of entity_intent samples. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update training samples by UUID.
    api_response = api_instance.entity_intent_crf_naive_bayes_update_training_samples(instance_name, entity_intent_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_update_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **entity_intent_sample_list** | [**list[EntityIntentSample]**](EntityIntentSample.md)| List of entity_intent samples. A sample&#39;s UUIDs is used to uniquely identify it. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[EntityIntentSample]**](EntityIntentSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_intent_crf_naive_bayes_vaporise**
> EntityIntentCrfNaiveBayesInstanceDetail entity_intent_crf_naive_bayes_vaporise(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.EntityIntentCrfNaiveBayesApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named model.
    api_response = api_instance.entity_intent_crf_naive_bayes_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityIntentCrfNaiveBayesApi->entity_intent_crf_naive_bayes_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**EntityIntentCrfNaiveBayesInstanceDetail**](EntityIntentCrfNaiveBayesInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

