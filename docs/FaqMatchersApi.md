# feersum_nlu.FaqMatchersApi

All URIs are relative to *https://nlu.qa.feersum.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**faq_matcher_add_testing_samples**](FaqMatchersApi.md#faq_matcher_add_testing_samples) | **POST** /nlu/v2/faq_matchers/{instance_name}/testing_samples | Add testing samples.
[**faq_matcher_add_training_samples**](FaqMatchersApi.md#faq_matcher_add_training_samples) | **POST** /nlu/v2/faq_matchers/{instance_name}/training_samples | Add training samples.
[**faq_matcher_create**](FaqMatchersApi.md#faq_matcher_create) | **POST** /nlu/v2/faq_matchers | Create an FAQ matcher.
[**faq_matcher_curate**](FaqMatchersApi.md#faq_matcher_curate) | **POST** /nlu/v2/faq_matchers/{instance_name}/curate | Endpoint to aid in the curation of an instance.
[**faq_matcher_del**](FaqMatchersApi.md#faq_matcher_del) | **DELETE** /nlu/v2/faq_matchers/{instance_name} | Delete named instance.
[**faq_matcher_del_testing_samples**](FaqMatchersApi.md#faq_matcher_del_testing_samples) | **DELETE** /nlu/v2/faq_matchers/{instance_name}/testing_samples | Delete testing samples.
[**faq_matcher_del_testing_samples_all**](FaqMatchersApi.md#faq_matcher_del_testing_samples_all) | **DELETE** /nlu/v2/faq_matchers/{instance_name}/testing_samples_all | Delete all testing samples.
[**faq_matcher_del_training_samples**](FaqMatchersApi.md#faq_matcher_del_training_samples) | **DELETE** /nlu/v2/faq_matchers/{instance_name}/training_samples | Delete training samples.
[**faq_matcher_del_training_samples_all**](FaqMatchersApi.md#faq_matcher_del_training_samples_all) | **DELETE** /nlu/v2/faq_matchers/{instance_name}/training_samples_all | Delete all training samples.
[**faq_matcher_get_details**](FaqMatchersApi.md#faq_matcher_get_details) | **GET** /nlu/v2/faq_matchers/{instance_name} | Get details of named instance.
[**faq_matcher_get_details_all**](FaqMatchersApi.md#faq_matcher_get_details_all) | **GET** /nlu/v2/faq_matchers | Get list of FAQ matchers.
[**faq_matcher_get_labels**](FaqMatchersApi.md#faq_matcher_get_labels) | **GET** /nlu/v2/faq_matchers/{instance_name}/labels | Get list of possible labels.
[**faq_matcher_get_params**](FaqMatchersApi.md#faq_matcher_get_params) | **GET** /nlu/v2/faq_matchers/{instance_name}/params | Get the editable model parameters of named FAQ matcher.
[**faq_matcher_get_testing_samples**](FaqMatchersApi.md#faq_matcher_get_testing_samples) | **GET** /nlu/v2/faq_matchers/{instance_name}/testing_samples | Get testing samples.
[**faq_matcher_get_training_samples**](FaqMatchersApi.md#faq_matcher_get_training_samples) | **GET** /nlu/v2/faq_matchers/{instance_name}/training_samples | Get training samples.
[**faq_matcher_retrieve**](FaqMatchersApi.md#faq_matcher_retrieve) | **POST** /nlu/v2/faq_matchers/{instance_name}/retrieve | Match retrieve and FAQ.
[**faq_matcher_set_params**](FaqMatchersApi.md#faq_matcher_set_params) | **POST** /nlu/v2/faq_matchers/{instance_name}/params | Set the model parameters of named FAQ matcher.
[**faq_matcher_test**](FaqMatchersApi.md#faq_matcher_test) | **POST** /nlu/v2/faq_matchers/{instance_name}/test | Test the named faq matcher.
[**faq_matcher_train**](FaqMatchersApi.md#faq_matcher_train) | **POST** /nlu/v2/faq_matchers/{instance_name}/train | Train the named FAQ matcher.
[**faq_matcher_tsne_get**](FaqMatchersApi.md#faq_matcher_tsne_get) | **GET** /nlu/v2/faq_matchers/{instance_name}/tsne | Get the latest results of TSNE.
[**faq_matcher_tsne_post**](FaqMatchersApi.md#faq_matcher_tsne_post) | **POST** /nlu/v2/faq_matchers/{instance_name}/tsne | Endpoint to start a TSNE process.
[**faq_matcher_update_testing_samples**](FaqMatchersApi.md#faq_matcher_update_testing_samples) | **PUT** /nlu/v2/faq_matchers/{instance_name}/testing_samples | Update testning samples by UUID.
[**faq_matcher_update_training_samples**](FaqMatchersApi.md#faq_matcher_update_training_samples) | **PUT** /nlu/v2/faq_matchers/{instance_name}/training_samples | Update training samples by UUID.
[**faq_matcher_vaporise**](FaqMatchersApi.md#faq_matcher_vaporise) | **POST** /nlu/v2/faq_matchers/{instance_name}/vaporise | Vaporise the named model.


# **faq_matcher_add_testing_samples**
> list[LabelledTextSample] faq_matcher_add_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Add testing samples.

Add testing samples to named faq matcher. Returns the samples added to the instance.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add testing samples.
    api_response = api_instance.faq_matcher_add_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_add_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
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

# **faq_matcher_add_training_samples**
> list[LabelledTextSample] faq_matcher_add_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Add training samples.

Add training samples to named faq matcher. Returns the samples added to the instance.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add training samples.
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_add_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
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

# **faq_matcher_create**
> FaqMatcherInstanceDetail faq_matcher_create(create_details, x_caller=x_caller)

Create an FAQ matcher.

Create a new faq matcher or reload one from the trash. Returns the details of the instance.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.FaqMatcherCreateDetails() # FaqMatcherCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create an FAQ matcher.
    api_response = api_instance.faq_matcher_create(create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**FaqMatcherCreateDetails**](FaqMatcherCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_curate**
> list[LabelledTextSample] faq_matcher_curate(instance_name, label_pair, x_caller=x_caller)

Endpoint to aid in the curation of an instance.

Returns the list of samples behind a cell of the confusion matrix of the training or testing samples.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
label_pair = feersum_nlu.ClassLabelPair() # ClassLabelPair | The true label, predicted label and matrix (train/test) to use.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Endpoint to aid in the curation of an instance.
    api_response = api_instance.faq_matcher_curate(instance_name, label_pair, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_curate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **label_pair** | [**ClassLabelPair**](ClassLabelPair.md)| The true label, predicted label and matrix (train/test) to use. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del**
> FaqMatcherInstanceDetail faq_matcher_del(instance_name, x_caller=x_caller)

Delete named instance.

Delete and return the details of the named FAQ matcher instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.faq_matcher_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del_testing_samples**
> list[LabelledTextSample] faq_matcher_del_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Delete testing samples.

Delete the listed testing samples of the named FAQ matcher. Returns the deleted samples.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete testing samples.
    api_response = api_instance.faq_matcher_del_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
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

# **faq_matcher_del_testing_samples_all**
> list[LabelledTextSample] faq_matcher_del_testing_samples_all(instance_name, x_caller=x_caller)

Delete all testing samples.

Delete all testing samples of the named FAQ matcher. Returns the deleted samples.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all testing samples.
    api_response = api_instance.faq_matcher_del_testing_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_testing_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del_training_samples**
> list[LabelledTextSample] faq_matcher_del_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Delete training samples.

Delete the listed training samples of the named FAQ matcher. Returns the deleted samples.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete training samples.
    api_response = api_instance.faq_matcher_del_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
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

# **faq_matcher_del_training_samples_all**
> list[LabelledTextSample] faq_matcher_del_training_samples_all(instance_name, x_caller=x_caller)

Delete all training samples.

Delete all training samples of the named FAQ matcher. Returns the deleted samples.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all training samples.
    api_response = api_instance.faq_matcher_del_training_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_training_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_details**
> FaqMatcherInstanceDetail faq_matcher_get_details(instance_name, x_caller=x_caller)

Get details of named instance.

Get the details of the named FAQ matcher instance.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.faq_matcher_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_details_all**
> list[FaqMatcherInstanceDetail] faq_matcher_get_details_all(x_caller=x_caller)

Get list of FAQ matchers.

Returns the list of faq matchers.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of FAQ matchers.
    api_response = api_instance.faq_matcher_get_details_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[FaqMatcherInstanceDetail]**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_labels**
> list[ClassLabel] faq_matcher_get_labels(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of possible labels.
    api_response = api_instance.faq_matcher_get_labels(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_labels: %s\n" % e)
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

# **faq_matcher_get_params**
> ModelParams faq_matcher_get_params(instance_name, x_caller=x_caller)

Get the editable model parameters of named FAQ matcher.

Get the editable model parameters of FAQ matcher.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the editable model parameters of named FAQ matcher.
    api_response = api_instance.faq_matcher_get_params(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_params: %s\n" % e)
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

# **faq_matcher_get_testing_samples**
> list[LabelledTextSample] faq_matcher_get_testing_samples(instance_name, x_caller=x_caller, index=index, len=len)

Get testing samples.

Returns the testing samples of the named faq matcher.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get testing samples.
    api_response = api_instance.faq_matcher_get_testing_samples(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 
 **index** | **int**| The sample index to start from. | [optional] 
 **len** | **int**| The number of samples to return. | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_training_samples**
> list[LabelledTextSample] faq_matcher_get_training_samples(instance_name, x_caller=x_caller, index=index, len=len)

Get training samples.

Returns the training samples of the named faq matcher.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get training samples.
    api_response = api_instance.faq_matcher_get_training_samples(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 
 **index** | **int**| The sample index to start from. | [optional] 
 **len** | **int**| The number of samples to return. | [optional] 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_retrieve**
> list[ScoredLabel] faq_matcher_retrieve(instance_name, text_input, x_caller=x_caller)

Match retrieve and FAQ.

Matchers the FAQ and returns a probability sorted list of answer labels.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Match retrieve and FAQ.
    api_response = api_instance.faq_matcher_retrieve(instance_name, text_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_retrieve: %s\n" % e)
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

# **faq_matcher_set_params**
> FaqMatcherInstanceDetail faq_matcher_set_params(instance_name, model_params, x_caller=x_caller)

Set the model parameters of named FAQ matcher.

Set the model parameters of FAQ matcher.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Set the model parameters of named FAQ matcher.
    api_response = api_instance.faq_matcher_set_params(instance_name, model_params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_test**
> FaqMatcherInstanceDetail faq_matcher_test(instance_name, test_details, x_caller=x_caller)

Test the named faq matcher.

Test the named faq matcher with the testing data already provided. Returns the details of the instance.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
test_details = feersum_nlu.TestDetails() # TestDetails | The arguments provided to the test operation.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Test the named faq matcher.
    api_response = api_instance.faq_matcher_test(instance_name, test_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **test_details** | [**TestDetails**](TestDetails.md)| The arguments provided to the test operation. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_train**
> FaqMatcherInstanceDetail faq_matcher_train(instance_name, train_details, x_caller=x_caller)

Train the named FAQ matcher.

Train the named FAQ matcher with the training and testing data already provided. Returns the updated instance detail.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Train the named FAQ matcher.
    api_response = api_instance.faq_matcher_train(instance_name, train_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **train_details** | [**TrainDetails**](TrainDetails.md)| The arguments provided to the train operation. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_tsne_get**
> list[TsneSample] faq_matcher_tsne_get(instance_name, x_caller=x_caller)

Get the latest results of TSNE.

Get the latest results of TSNE.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the latest results of TSNE.
    api_response = api_instance.faq_matcher_tsne_get(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_tsne_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[TsneSample]**](TsneSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_tsne_post**
> faq_matcher_tsne_post(instance_name, tsne_settings, x_caller=x_caller)

Endpoint to start a TSNE process.

Starts a TSNE process.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
tsne_settings = feersum_nlu.TsneSettings() # TsneSettings | The TSNE settings.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Endpoint to start a TSNE process.
    api_instance.faq_matcher_tsne_post(instance_name, tsne_settings, x_caller=x_caller)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_tsne_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **tsne_settings** | [**TsneSettings**](TsneSettings.md)| The TSNE settings. | 
 **x_caller** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_update_testing_samples**
> list[LabelledTextSample] faq_matcher_update_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Update testning samples by UUID.

Update training samples of the named faq matcher. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of text samples to update. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update testning samples by UUID.
    api_response = api_instance.faq_matcher_update_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_update_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
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

# **faq_matcher_update_training_samples**
> list[LabelledTextSample] faq_matcher_update_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Update training samples by UUID.

Update training samples of the named faq matcher. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of text samples to update. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update training samples by UUID.
    api_response = api_instance.faq_matcher_update_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_update_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
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

# **faq_matcher_vaporise**
> FaqMatcherInstanceDetail faq_matcher_vaporise(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named model.
    api_response = api_instance.faq_matcher_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

