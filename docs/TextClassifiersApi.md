# feersum_nlu.TextClassifiersApi

All URIs are relative to *https://nlu.feersum.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_classifier_add_testing_samples**](TextClassifiersApi.md#text_classifier_add_testing_samples) | **POST** /nlu/v2/text_classifiers/{instance_name}/testing_samples | Add testing samples.
[**text_classifier_add_training_samples**](TextClassifiersApi.md#text_classifier_add_training_samples) | **POST** /nlu/v2/text_classifiers/{instance_name}/training_samples | Add training samples.
[**text_classifier_create**](TextClassifiersApi.md#text_classifier_create) | **POST** /nlu/v2/text_classifiers | Create a text classifier.
[**text_classifier_create_from_path**](TextClassifiersApi.md#text_classifier_create_from_path) | **POST** /nlu/v2/text_classifiers/{instance_name} | Create a text classifier.
[**text_classifier_curate**](TextClassifiersApi.md#text_classifier_curate) | **POST** /nlu/v2/text_classifiers/{instance_name}/curate | Endpoint to aid in the curation of an instance.
[**text_classifier_del**](TextClassifiersApi.md#text_classifier_del) | **DELETE** /nlu/v2/text_classifiers/{instance_name} | Delete named instance.
[**text_classifier_del_testing_samples**](TextClassifiersApi.md#text_classifier_del_testing_samples) | **DELETE** /nlu/v2/text_classifiers/{instance_name}/testing_samples | Delete testing samples.
[**text_classifier_del_testing_samples_all**](TextClassifiersApi.md#text_classifier_del_testing_samples_all) | **DELETE** /nlu/v2/text_classifiers/{instance_name}/testing_samples_all | Delete testing samples.
[**text_classifier_del_training_samples**](TextClassifiersApi.md#text_classifier_del_training_samples) | **DELETE** /nlu/v2/text_classifiers/{instance_name}/training_samples | Delete training samples.
[**text_classifier_del_training_samples_all**](TextClassifiersApi.md#text_classifier_del_training_samples_all) | **DELETE** /nlu/v2/text_classifiers/{instance_name}/training_samples_all | Delete all training samples.
[**text_classifier_get_details**](TextClassifiersApi.md#text_classifier_get_details) | **GET** /nlu/v2/text_classifiers/{instance_name} | Get details of named instance.
[**text_classifier_get_details_all**](TextClassifiersApi.md#text_classifier_get_details_all) | **GET** /nlu/v2/text_classifiers | Get list of text classifiers.
[**text_classifier_get_labels**](TextClassifiersApi.md#text_classifier_get_labels) | **GET** /nlu/v2/text_classifiers/{instance_name}/labels | Get list of possible labels.
[**text_classifier_get_params**](TextClassifiersApi.md#text_classifier_get_params) | **GET** /nlu/v2/text_classifiers/{instance_name}/params | Get the editable model parameters of named text classifier.
[**text_classifier_get_testing_samples**](TextClassifiersApi.md#text_classifier_get_testing_samples) | **GET** /nlu/v2/text_classifiers/{instance_name}/testing_samples | Get testing samples.
[**text_classifier_get_training_samples**](TextClassifiersApi.md#text_classifier_get_training_samples) | **GET** /nlu/v2/text_classifiers/{instance_name}/training_samples | Get training samples.
[**text_classifier_online_training_samples**](TextClassifiersApi.md#text_classifier_online_training_samples) | **POST** /nlu/v2/text_classifiers/{instance_name}/online_training_samples | Train/update the classifier online with the samples provided.
[**text_classifier_retrieve**](TextClassifiersApi.md#text_classifier_retrieve) | **POST** /nlu/v2/text_classifiers/{instance_name}/retrieve | Classify text.
[**text_classifier_set_params**](TextClassifiersApi.md#text_classifier_set_params) | **POST** /nlu/v2/text_classifiers/{instance_name}/params | Set the model parameters of named text classifier.
[**text_classifier_train**](TextClassifiersApi.md#text_classifier_train) | **POST** /nlu/v2/text_classifiers/{instance_name}/train | Train the named text classifier.
[**text_classifier_tsne_get**](TextClassifiersApi.md#text_classifier_tsne_get) | **GET** /nlu/v2/text_classifiers/{instance_name}/tsne | Get the latest results of TSNE.
[**text_classifier_tsne_post**](TextClassifiersApi.md#text_classifier_tsne_post) | **POST** /nlu/v2/text_classifiers/{instance_name}/tsne | Endpoint to start a TSNE process.
[**text_classifier_update_testing_samples**](TextClassifiersApi.md#text_classifier_update_testing_samples) | **PUT** /nlu/v2/text_classifiers/{instance_name}/testing_samples | Update testing samples by UUID.
[**text_classifier_update_training_samples**](TextClassifiersApi.md#text_classifier_update_training_samples) | **PUT** /nlu/v2/text_classifiers/{instance_name}/training_samples | Update training samples by UUID.
[**text_classifier_vaporise**](TextClassifiersApi.md#text_classifier_vaporise) | **POST** /nlu/v2/text_classifiers/{instance_name}/vaporise | Vaporise the named model.


# **text_classifier_add_testing_samples**
> list[LabelledTextSample] text_classifier_add_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Add testing samples.

Add testing samples to named text classifier. Returns the samples added to the instance.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add testing samples.
    api_response = api_instance.text_classifier_add_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_add_testing_samples: %s\n" % e)
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

# **text_classifier_add_training_samples**
> list[LabelledTextSample] text_classifier_add_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Add training samples.

Add training samples to named text classifier. Returns the samples added to the instance.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Add training samples.
    api_response = api_instance.text_classifier_add_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_add_training_samples: %s\n" % e)
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

# **text_classifier_create**
> TextClassifierInstanceDetail text_classifier_create(create_details, x_caller=x_caller)

Create a text classifier.

Create a new text classifier or reload one from the trash. Returns the details of the instance.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.TextClassifierCreateDetails() # TextClassifierCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create a text classifier.
    api_response = api_instance.text_classifier_create(create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**TextClassifierCreateDetails**](TextClassifierCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_create_from_path**
> TextClassifierInstanceDetail text_classifier_create_from_path(instance_name, create_details, x_caller=x_caller)

Create a text classifier.

Create a new text classifier or reload one from the trash. Returns the details of the instance.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
create_details = feersum_nlu.TextClassifierCreateDetails() # TextClassifierCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Create a text classifier.
    api_response = api_instance.text_classifier_create_from_path(instance_name, create_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_create_from_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **create_details** | [**TextClassifierCreateDetails**](TextClassifierCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_curate**
> list[LabelledTextSample] text_classifier_curate(instance_name, label_pair, x_caller=x_caller)

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
label_pair = feersum_nlu.ClassLabelPair() # ClassLabelPair | The true label, predicted label and matrix (train/test) to use.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Endpoint to aid in the curation of an instance.
    api_response = api_instance.text_classifier_curate(instance_name, label_pair, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_curate: %s\n" % e)
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

# **text_classifier_del**
> TextClassifierInstanceDetail text_classifier_del(instance_name, x_caller=x_caller)

Delete named instance.

Delete and return the details of the named text classifier instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.text_classifier_del(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_del_testing_samples**
> list[LabelledTextSample] text_classifier_del_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Delete testing samples.

Delete the listed testing samples of the named text classifier. Returns the deleted samples.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete testing samples.
    api_response = api_instance.text_classifier_del_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_testing_samples: %s\n" % e)
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

# **text_classifier_del_testing_samples_all**
> list[LabelledTextSample] text_classifier_del_testing_samples_all(instance_name, x_caller=x_caller)

Delete testing samples.

Delete all testing samples of the named text classifier. Returns the deleted samples.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete testing samples.
    api_response = api_instance.text_classifier_del_testing_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_testing_samples_all: %s\n" % e)
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

# **text_classifier_del_training_samples**
> list[LabelledTextSample] text_classifier_del_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Delete training samples.

Delete the listed training samples of the named text classifier. Returns the deleted samples.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete training samples.
    api_response = api_instance.text_classifier_del_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_training_samples: %s\n" % e)
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

# **text_classifier_del_training_samples_all**
> list[LabelledTextSample] text_classifier_del_training_samples_all(instance_name, x_caller=x_caller)

Delete all training samples.

Delete all training samples of the named text classifier. Returns the deleted samples.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Delete all training samples.
    api_response = api_instance.text_classifier_del_training_samples_all(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_training_samples_all: %s\n" % e)
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

# **text_classifier_get_details**
> TextClassifierInstanceDetail text_classifier_get_details(instance_name, x_caller=x_caller)

Get details of named instance.

Get the details of the named text classifier instance.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.text_classifier_get_details(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_details_all**
> list[TextClassifierInstanceDetail] text_classifier_get_details_all(x_caller=x_caller)

Get list of text classifiers.

Get the list of text classifiers.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of text classifiers.
    api_response = api_instance.text_classifier_get_details_all(x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 

### Return type

[**list[TextClassifierInstanceDetail]**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_labels**
> list[ClassLabel] text_classifier_get_labels(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get list of possible labels.
    api_response = api_instance.text_classifier_get_labels(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_labels: %s\n" % e)
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

# **text_classifier_get_params**
> ModelParams text_classifier_get_params(instance_name, x_caller=x_caller)

Get the editable model parameters of named text classifier.

Get the editable model parameters of named text classifier.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the editable model parameters of named text classifier.
    api_response = api_instance.text_classifier_get_params(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_params: %s\n" % e)
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

# **text_classifier_get_testing_samples**
> list[LabelledTextSample] text_classifier_get_testing_samples(instance_name, x_caller=x_caller, index=index, len=len)

Get testing samples.

Get the testing samples of the named text classifier.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get testing samples.
    api_response = api_instance.text_classifier_get_testing_samples(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_testing_samples: %s\n" % e)
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

# **text_classifier_get_training_samples**
> list[LabelledTextSample] text_classifier_get_training_samples(instance_name, x_caller=x_caller, index=index, len=len)

Get training samples.

Get the training samples of the named text classifier.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)
index = 56 # int | The sample index to start from. (optional)
len = 56 # int | The number of samples to return. (optional)

try:
    # Get training samples.
    api_response = api_instance.text_classifier_get_training_samples(instance_name, x_caller=x_caller, index=index, len=len)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_training_samples: %s\n" % e)
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

# **text_classifier_online_training_samples**
> list[LabelledTextSample] text_classifier_online_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Train/update the classifier online with the samples provided.

Train/update the classifier online with the samples provided. This operation is more efficient than a full re-train. Returns the samples added to the instance.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Train/update the classifier online with the samples provided.
    api_response = api_instance.text_classifier_online_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_online_training_samples: %s\n" % e)
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

# **text_classifier_retrieve**
> list[ScoredLabel] text_classifier_retrieve(instance_name, text_input, x_caller=x_caller)

Classify text.

Classifies the text and returns a probability sorted list of classes.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Classify text.
    api_response = api_instance.text_classifier_retrieve(instance_name, text_input, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_retrieve: %s\n" % e)
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

# **text_classifier_set_params**
> TextClassifierInstanceDetail text_classifier_set_params(instance_name, model_params, x_caller=x_caller)

Set the model parameters of named text classifier.

Set the model parameters of named text classifier.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Set the model parameters of named text classifier.
    api_response = api_instance.text_classifier_set_params(instance_name, model_params, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_train**
> TextClassifierInstanceDetail text_classifier_train(instance_name, train_details, x_caller=x_caller)

Train the named text classifier.

Train the named text classifier with the training and testing data already provided. Returns the details of the instance.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Train the named text classifier.
    api_response = api_instance.text_classifier_train(instance_name, train_details, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **train_details** | [**TrainDetails**](TrainDetails.md)| The arguments provided to the train operation. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_tsne_get**
> list[TsneSample] text_classifier_tsne_get(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Get the latest results of TSNE.
    api_response = api_instance.text_classifier_tsne_get(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_tsne_get: %s\n" % e)
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

# **text_classifier_tsne_post**
> text_classifier_tsne_post(instance_name, tsne_settings, x_caller=x_caller)

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
tsne_settings = feersum_nlu.TsneSettings() # TsneSettings | The TSNE settings.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Endpoint to start a TSNE process.
    api_instance.text_classifier_tsne_post(instance_name, tsne_settings, x_caller=x_caller)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_tsne_post: %s\n" % e)
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

# **text_classifier_update_testing_samples**
> list[LabelledTextSample] text_classifier_update_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Update testing samples by UUID.

Update training samples of the named text classifier. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of text samples to update. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update testing samples by UUID.
    api_response = api_instance.text_classifier_update_testing_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_update_testing_samples: %s\n" % e)
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

# **text_classifier_update_training_samples**
> list[LabelledTextSample] text_classifier_update_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)

Update training samples by UUID.

Update training samples of the named text classifier. A sample's UUIDs is used to uniquely identify it. Returns the samples that were updated.

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of text samples to update. A sample's UUIDs is used to uniquely identify it.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Update training samples by UUID.
    api_response = api_instance.text_classifier_update_training_samples(instance_name, labelled_text_sample_list, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_update_training_samples: %s\n" % e)
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

# **text_classifier_vaporise**
> TextClassifierInstanceDetail text_classifier_vaporise(instance_name, x_caller=x_caller)

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
api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the instance.
x_caller = 'x_caller_example' # str |  (optional)

try:
    # Vaporise the named model.
    api_response = api_instance.text_classifier_vaporise(instance_name, x_caller=x_caller)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the instance. | 
 **x_caller** | **str**|  | [optional] 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

