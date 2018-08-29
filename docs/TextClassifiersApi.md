# feersum_nlu.TextClassifiersApi

All URIs are relative to *https://nlu.dev.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_classifier_add_testing_samples**](TextClassifiersApi.md#text_classifier_add_testing_samples) | **POST** /text_classifiers/{instance_name}/testing_samples | Add testing samples.
[**text_classifier_add_training_samples**](TextClassifiersApi.md#text_classifier_add_training_samples) | **POST** /text_classifiers/{instance_name}/training_samples | Add training samples.
[**text_classifier_create**](TextClassifiersApi.md#text_classifier_create) | **POST** /text_classifiers | Create a text classifier.
[**text_classifier_curate**](TextClassifiersApi.md#text_classifier_curate) | **POST** /text_classifiers/{instance_name}/curate | Endpoint to aid in the curation of a model instance.
[**text_classifier_del**](TextClassifiersApi.md#text_classifier_del) | **DELETE** /text_classifiers/{instance_name} | Delete named instance.
[**text_classifier_del_testing_samples**](TextClassifiersApi.md#text_classifier_del_testing_samples) | **DELETE** /text_classifiers/{instance_name}/testing_samples | Delete testing samples.
[**text_classifier_del_testing_samples_all**](TextClassifiersApi.md#text_classifier_del_testing_samples_all) | **DELETE** /text_classifiers/{instance_name}/testing_samples_all | Delete testing samples.
[**text_classifier_del_training_samples**](TextClassifiersApi.md#text_classifier_del_training_samples) | **DELETE** /text_classifiers/{instance_name}/training_samples | Delete training samples.
[**text_classifier_del_training_samples_all**](TextClassifiersApi.md#text_classifier_del_training_samples_all) | **DELETE** /text_classifiers/{instance_name}/training_samples_all | Delete all training samples.
[**text_classifier_get_details**](TextClassifiersApi.md#text_classifier_get_details) | **GET** /text_classifiers/{instance_name} | Get details of named instance.
[**text_classifier_get_details_all**](TextClassifiersApi.md#text_classifier_get_details_all) | **GET** /text_classifiers | Get list of loaded text classifiers.
[**text_classifier_get_labels**](TextClassifiersApi.md#text_classifier_get_labels) | **GET** /text_classifiers/{instance_name}/get_labels | Get list of possible labels.
[**text_classifier_get_testing_samples**](TextClassifiersApi.md#text_classifier_get_testing_samples) | **GET** /text_classifiers/{instance_name}/testing_samples | Get testing samples.
[**text_classifier_get_training_samples**](TextClassifiersApi.md#text_classifier_get_training_samples) | **GET** /text_classifiers/{instance_name}/training_samples | Get training samples.
[**text_classifier_retrieve**](TextClassifiersApi.md#text_classifier_retrieve) | **POST** /text_classifiers/{instance_name}/retrieve | Classify text.
[**text_classifier_set_params**](TextClassifiersApi.md#text_classifier_set_params) | **POST** /text_classifiers/{instance_name}/params | Set the model parameters of named text classifier.
[**text_classifier_train**](TextClassifiersApi.md#text_classifier_train) | **POST** /text_classifiers/{instance_name}/train | Train the named text classifier.
[**text_classifier_vaporise**](TextClassifiersApi.md#text_classifier_vaporise) | **POST** /text_classifiers/{instance_name}/vaporise | Vaporise the named model.


# **text_classifier_add_testing_samples**
> TotalSamples text_classifier_add_testing_samples(instance_name, labelled_text_sample_list)

Add testing samples.

Add testing samples to named text classifier. Returns the classifier's updated number of testing samples.

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
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Add testing samples.
    api_response = api_instance.text_classifier_add_testing_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_add_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_add_training_samples**
> TotalSamples text_classifier_add_training_samples(instance_name, labelled_text_sample_list)

Add training samples.

Add training samples to named text classifier. Returns the classifier's updated number of training samples.

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
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Add training samples.
    api_response = api_instance.text_classifier_add_training_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_add_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_create**
> TextClassifierInstanceDetail text_classifier_create(create_details)

Create a text classifier.

Create a new text classifier or reload one from the trash. Returns the details of the new or loaded instance.

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

try:
    # Create a text classifier.
    api_response = api_instance.text_classifier_create(create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**TextClassifierCreateDetails**](TextClassifierCreateDetails.md)| The details of the instance to create. | 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_curate**
> list[LabelledTextSample] text_classifier_curate(instance_name, label_pair)

Endpoint to aid in the curation of a model instance.

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
instance_name = 'instance_name_example' # str | The name of the model instance.
label_pair = feersum_nlu.ClassLabelPair() # ClassLabelPair | The true label, predicted label and matrix (train/test) to use.

try:
    # Endpoint to aid in the curation of a model instance.
    api_response = api_instance.text_classifier_curate(instance_name, label_pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_curate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **label_pair** | [**ClassLabelPair**](ClassLabelPair.md)| The true label, predicted label and matrix (train/test) to use. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_del**
> TextClassifierInstanceDetail text_classifier_del(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete named instance.
    api_response = api_instance.text_classifier_del(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_del_testing_samples**
> list[LabelledTextSample] text_classifier_del_testing_samples(instance_name, labelled_text_sample_list)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Delete testing samples.
    api_response = api_instance.text_classifier_del_testing_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_del_testing_samples_all**
> list[LabelledTextSample] text_classifier_del_testing_samples_all(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete testing samples.
    api_response = api_instance.text_classifier_del_testing_samples_all(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_testing_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_del_training_samples**
> list[LabelledTextSample] text_classifier_del_training_samples(instance_name, labelled_text_sample_list)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Delete training samples.
    api_response = api_instance.text_classifier_del_training_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_del_training_samples_all**
> list[LabelledTextSample] text_classifier_del_training_samples_all(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete all training samples.
    api_response = api_instance.text_classifier_del_training_samples_all(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_training_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_details**
> TextClassifierInstanceDetail text_classifier_get_details(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get details of named instance.
    api_response = api_instance.text_classifier_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_details_all**
> list[TextClassifierInstanceDetail] text_classifier_get_details_all()

Get list of loaded text classifiers.

Get the list of loaded text classifiers.

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

try:
    # Get list of loaded text classifiers.
    api_response = api_instance.text_classifier_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_details_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TextClassifierInstanceDetail]**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_labels**
> list[ClassLabel] text_classifier_get_labels(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get list of possible labels.
    api_response = api_instance.text_classifier_get_labels(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_labels: %s\n" % e)
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

# **text_classifier_get_testing_samples**
> list[LabelledTextSample] text_classifier_get_testing_samples(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get testing samples.
    api_response = api_instance.text_classifier_get_testing_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_training_samples**
> list[LabelledTextSample] text_classifier_get_training_samples(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get training samples.
    api_response = api_instance.text_classifier_get_training_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_get_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_retrieve**
> list[ScoredLabel] text_classifier_retrieve(instance_name, text_input)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try:
    # Classify text.
    api_response = api_instance.text_classifier_retrieve(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 

### Return type

[**list[ScoredLabel]**](ScoredLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_set_params**
> TextClassifierInstanceDetail text_classifier_set_params(instance_name, model_params)

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
instance_name = 'instance_name_example' # str | The name of the model instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.

try:
    # Set the model parameters of named text classifier.
    api_response = api_instance.text_classifier_set_params(instance_name, model_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_train**
> TextClassifierInstanceDetail text_classifier_train(instance_name, train_details)

Train the named text classifier.

Train the named text classifier with the training and testing data already provided. Returns the details of the model instance.

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
instance_name = 'instance_name_example' # str | The name of the model instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.

try:
    # Train the named text classifier.
    api_response = api_instance.text_classifier_train(instance_name, train_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **train_details** | [**TrainDetails**](TrainDetails.md)| The arguments provided to the train operation. | 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_vaporise**
> TextClassifierInstanceDetail text_classifier_vaporise(instance_name)

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
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Vaporise the named model.
    api_response = api_instance.text_classifier_vaporise(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**TextClassifierInstanceDetail**](TextClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

