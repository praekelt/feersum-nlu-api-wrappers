# feersum_nlu.ImageClassifiersApi

All URIs are relative to *https://nlu.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_classifier_add_testing_samples**](ImageClassifiersApi.md#image_classifier_add_testing_samples) | **POST** /image_classifiers/{instance_name}/testing_samples | Add testing samples. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.
[**image_classifier_add_training_samples**](ImageClassifiersApi.md#image_classifier_add_training_samples) | **POST** /image_classifiers/{instance_name}/training_samples | Add training samples. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.
[**image_classifier_create**](ImageClassifiersApi.md#image_classifier_create) | **POST** /image_classifiers | Create an image classifier.
[**image_classifier_curate**](ImageClassifiersApi.md#image_classifier_curate) | **POST** /image_classifiers/{instance_name}/curate | Endpoint to aid in the curation of a model instance.
[**image_classifier_del**](ImageClassifiersApi.md#image_classifier_del) | **DELETE** /image_classifiers/{instance_name} | Delete named instance.
[**image_classifier_del_testing_samples**](ImageClassifiersApi.md#image_classifier_del_testing_samples) | **DELETE** /image_classifiers/{instance_name}/testing_samples | Delete testing samples.
[**image_classifier_del_testing_samples_all**](ImageClassifiersApi.md#image_classifier_del_testing_samples_all) | **DELETE** /image_classifiers/{instance_name}/testing_samples_all | Delete testing samples.
[**image_classifier_del_training_samples**](ImageClassifiersApi.md#image_classifier_del_training_samples) | **DELETE** /image_classifiers/{instance_name}/training_samples | Delete training samples.
[**image_classifier_del_training_samples_all**](ImageClassifiersApi.md#image_classifier_del_training_samples_all) | **DELETE** /image_classifiers/{instance_name}/training_samples_all | Delete all training samples.
[**image_classifier_get_details**](ImageClassifiersApi.md#image_classifier_get_details) | **GET** /image_classifiers/{instance_name} | Get details of named instance.
[**image_classifier_get_details_all**](ImageClassifiersApi.md#image_classifier_get_details_all) | **GET** /image_classifiers | Get list of loaded image classifiers.
[**image_classifier_get_labels**](ImageClassifiersApi.md#image_classifier_get_labels) | **GET** /image_classifiers/{instance_name}/get_labels | Get list of possible labels.
[**image_classifier_get_params**](ImageClassifiersApi.md#image_classifier_get_params) | **GET** /image_classifiers/{instance_name}/params | Get the editable model parameters of named image classifier.
[**image_classifier_get_testing_samples**](ImageClassifiersApi.md#image_classifier_get_testing_samples) | **GET** /image_classifiers/{instance_name}/testing_samples | Get testing samples. Image format is 256x256 RGB.
[**image_classifier_get_training_samples**](ImageClassifiersApi.md#image_classifier_get_training_samples) | **GET** /image_classifiers/{instance_name}/training_samples | Get training samples. Image format is 256x256 RGB.
[**image_classifier_online_training_samples**](ImageClassifiersApi.md#image_classifier_online_training_samples) | **POST** /image_classifiers/{instance_name}/online_training_samples | Train/update the classifier online with the samples provided. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.
[**image_classifier_retrieve**](ImageClassifiersApi.md#image_classifier_retrieve) | **POST** /image_classifiers/{instance_name}/retrieve | Classify image; Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.
[**image_classifier_set_params**](ImageClassifiersApi.md#image_classifier_set_params) | **POST** /image_classifiers/{instance_name}/params | Set the model parameters of named image classifier.
[**image_classifier_train**](ImageClassifiersApi.md#image_classifier_train) | **POST** /image_classifiers/{instance_name}/train | Train the named image classifier.
[**image_classifier_vaporise**](ImageClassifiersApi.md#image_classifier_vaporise) | **POST** /image_classifiers/{instance_name}/vaporise | Vaporise the named model.


# **image_classifier_add_testing_samples**
> TotalSamples image_classifier_add_testing_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)

Add testing samples. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.

Add testing samples to named image classifier. Returns the classifier's updated number of testing samples.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_image_sample_list = [feersum_nlu.LabelledImageSample()] # list[LabelledImageSample] | List of labelled image samples.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Add testing samples. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.
    api_response = api_instance.image_classifier_add_testing_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_add_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_image_sample_list** | [**list[LabelledImageSample]**](LabelledImageSample.md)| List of labelled image samples. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_add_training_samples**
> TotalSamples image_classifier_add_training_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)

Add training samples. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.

Add training samples to named image classifier. Returns the classifier's updated number of training samples.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_image_sample_list = [feersum_nlu.LabelledImageSample()] # list[LabelledImageSample] | List of labelled image samples.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Add training samples. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.
    api_response = api_instance.image_classifier_add_training_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_add_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_image_sample_list** | [**list[LabelledImageSample]**](LabelledImageSample.md)| List of labelled image samples. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_create**
> ImageClassifierInstanceDetail image_classifier_create(create_details, x_caller=x_caller, origin=origin)

Create an image classifier.

Create a new image classifier or reload one from the trash. Returns the details of the new or loaded instance.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.ImageClassifierCreateDetails() # ImageClassifierCreateDetails | The details of the instance to create.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Create an image classifier.
    api_response = api_instance.image_classifier_create(create_details, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**ImageClassifierCreateDetails**](ImageClassifierCreateDetails.md)| The details of the instance to create. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**ImageClassifierInstanceDetail**](ImageClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_curate**
> list[LabelledImageSample] image_classifier_curate(instance_name, label_pair, x_caller=x_caller, origin=origin)

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
label_pair = feersum_nlu.ClassLabelPair() # ClassLabelPair | The true label, predicted label and matrix (train/test) to use.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Endpoint to aid in the curation of a model instance.
    api_response = api_instance.image_classifier_curate(instance_name, label_pair, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_curate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **label_pair** | [**ClassLabelPair**](ClassLabelPair.md)| The true label, predicted label and matrix (train/test) to use. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[LabelledImageSample]**](LabelledImageSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_del**
> ImageClassifierInstanceDetail image_classifier_del(instance_name, x_caller=x_caller, origin=origin)

Delete named instance.

Delete and return the details of the named image classifier instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Delete named instance.
    api_response = api_instance.image_classifier_del(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**ImageClassifierInstanceDetail**](ImageClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_del_testing_samples**
> list[LabelledImageSample] image_classifier_del_testing_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)

Delete testing samples.

Delete the listed testing samples of the named image classifier. Returns the deleted samples.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_image_sample_list = [feersum_nlu.LabelledImageSample()] # list[LabelledImageSample] | List of labelled image samples.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Delete testing samples.
    api_response = api_instance.image_classifier_del_testing_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_del_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_image_sample_list** | [**list[LabelledImageSample]**](LabelledImageSample.md)| List of labelled image samples. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[LabelledImageSample]**](LabelledImageSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_del_testing_samples_all**
> list[LabelledImageSample] image_classifier_del_testing_samples_all(instance_name, x_caller=x_caller, origin=origin)

Delete testing samples.

Delete all testing samples of the named image classifier. Returns the deleted samples.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Delete testing samples.
    api_response = api_instance.image_classifier_del_testing_samples_all(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_del_testing_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[LabelledImageSample]**](LabelledImageSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_del_training_samples**
> list[LabelledImageSample] image_classifier_del_training_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)

Delete training samples.

Delete the listed training samples of the named image classifier. Returns the deleted samples.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_image_sample_list = [feersum_nlu.LabelledImageSample()] # list[LabelledImageSample] | List of labelled image samples.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Delete training samples.
    api_response = api_instance.image_classifier_del_training_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_del_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_image_sample_list** | [**list[LabelledImageSample]**](LabelledImageSample.md)| List of labelled image samples. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[LabelledImageSample]**](LabelledImageSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_del_training_samples_all**
> list[LabelledImageSample] image_classifier_del_training_samples_all(instance_name, x_caller=x_caller, origin=origin)

Delete all training samples.

Delete all training samples of the named image classifier. Returns the deleted samples.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Delete all training samples.
    api_response = api_instance.image_classifier_del_training_samples_all(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_del_training_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[LabelledImageSample]**](LabelledImageSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_get_details**
> ImageClassifierInstanceDetail image_classifier_get_details(instance_name, x_caller=x_caller, origin=origin)

Get details of named instance.

Get the details of the named image classifier instance.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Get details of named instance.
    api_response = api_instance.image_classifier_get_details(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**ImageClassifierInstanceDetail**](ImageClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_get_details_all**
> list[ImageClassifierInstanceDetail] image_classifier_get_details_all(x_caller=x_caller, origin=origin)

Get list of loaded image classifiers.

Get the list of loaded image classifiers.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Get list of loaded image classifiers.
    api_response = api_instance.image_classifier_get_details_all(x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_get_details_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[ImageClassifierInstanceDetail]**](ImageClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_get_labels**
> list[ClassLabel] image_classifier_get_labels(instance_name, x_caller=x_caller, origin=origin)

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Get list of possible labels.
    api_response = api_instance.image_classifier_get_labels(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[ClassLabel]**](ClassLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_get_params**
> ModelParams image_classifier_get_params(instance_name, x_caller=x_caller, origin=origin)

Get the editable model parameters of named image classifier.

Get the editable model parameters of named image classifier.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Get the editable model parameters of named image classifier.
    api_response = api_instance.image_classifier_get_params(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_get_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**ModelParams**](ModelParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_get_testing_samples**
> list[LabelledImageSample] image_classifier_get_testing_samples(instance_name, x_caller=x_caller, origin=origin)

Get testing samples. Image format is 256x256 RGB.

Get the testing samples of the named image classifier.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Get testing samples. Image format is 256x256 RGB.
    api_response = api_instance.image_classifier_get_testing_samples(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_get_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[LabelledImageSample]**](LabelledImageSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_get_training_samples**
> list[LabelledImageSample] image_classifier_get_training_samples(instance_name, x_caller=x_caller, origin=origin)

Get training samples. Image format is 256x256 RGB.

Get the training samples of the named image classifier.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Get training samples. Image format is 256x256 RGB.
    api_response = api_instance.image_classifier_get_training_samples(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_get_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[LabelledImageSample]**](LabelledImageSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_online_training_samples**
> TotalSamples image_classifier_online_training_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)

Train/update the classifier online with the samples provided. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.

Train/update the classifier online with the samples provided. This operation is more efficient than a full re-train. Returns the classifier's updated number of training samples.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_image_sample_list = [feersum_nlu.LabelledImageSample()] # list[LabelledImageSample] | List of labelled image samples.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Train/update the classifier online with the samples provided. Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.
    api_response = api_instance.image_classifier_online_training_samples(instance_name, labelled_image_sample_list, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_online_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_image_sample_list** | [**list[LabelledImageSample]**](LabelledImageSample.md)| List of labelled image samples. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_retrieve**
> list[ScoredLabel] image_classifier_retrieve(instance_name, image_input, x_caller=x_caller, origin=origin)

Classify image; Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.

Classifies the image and returns a probability sorted list of classes.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
image_input = feersum_nlu.ImageInput() # ImageInput | The input image.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Classify image; Image format is 256x256 RGB; jpeg encoding at quality 50 is suggested.
    api_response = api_instance.image_classifier_retrieve(instance_name, image_input, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **image_input** | [**ImageInput**](ImageInput.md)| The input image. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**list[ScoredLabel]**](ScoredLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_set_params**
> ImageClassifierInstanceDetail image_classifier_set_params(instance_name, model_params, x_caller=x_caller, origin=origin)

Set the model parameters of named image classifier.

Set the model parameters of named image classifier.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Set the model parameters of named image classifier.
    api_response = api_instance.image_classifier_set_params(instance_name, model_params, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**ImageClassifierInstanceDetail**](ImageClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_train**
> ImageClassifierInstanceDetail image_classifier_train(instance_name, train_details, x_caller=x_caller, origin=origin)

Train the named image classifier.

Train the named image classifier with the training and testing data already provided. Returns the details of the model instance.

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Train the named image classifier.
    api_response = api_instance.image_classifier_train(instance_name, train_details, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **train_details** | [**TrainDetails**](TrainDetails.md)| The arguments provided to the train operation. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**ImageClassifierInstanceDetail**](ImageClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_classifier_vaporise**
> ImageClassifierInstanceDetail image_classifier_vaporise(instance_name, x_caller=x_caller, origin=origin)

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
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
x_caller = 'x_caller_example' # str |  (optional)
origin = 'origin_example' # str |  (optional)

try:
    # Vaporise the named model.
    api_response = api_instance.image_classifier_vaporise(instance_name, x_caller=x_caller, origin=origin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageClassifiersApi->image_classifier_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **x_caller** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 

### Return type

[**ImageClassifierInstanceDetail**](ImageClassifierInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

