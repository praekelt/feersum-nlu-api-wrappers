# feersum_nlu.TextClassifiersApi

All URIs are relative to *http://nlu.playground.feersum.io:8100/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_classifier_add_training_samples**](TextClassifiersApi.md#text_classifier_add_training_samples) | **POST** /text_classifiers/{instance_name}/training_samples | Add training samples.
[**text_classifier_create**](TextClassifiersApi.md#text_classifier_create) | **POST** /text_classifiers | Create a text classifier.
[**text_classifier_del_training_samples**](TextClassifiersApi.md#text_classifier_del_training_samples) | **DELETE** /text_classifiers/{instance_name}/training_samples | Delete training samples.
[**text_classifier_get_details**](TextClassifiersApi.md#text_classifier_get_details) | **GET** /text_classifiers/{instance_name} | Get details of named instance.
[**text_classifier_get_details_all**](TextClassifiersApi.md#text_classifier_get_details_all) | **GET** /text_classifiers | Get list of loaded text classifiers.
[**text_classifier_get_training_samples**](TextClassifiersApi.md#text_classifier_get_training_samples) | **GET** /text_classifiers/{instance_name}/training_samples | Get training samples.
[**text_classifier_retrieve**](TextClassifiersApi.md#text_classifier_retrieve) | **POST** /text_classifiers/{instance_name}/retrieve | Classify text.
[**text_classifier_train**](TextClassifiersApi.md#text_classifier_train) | **POST** /text_classifiers/{instance_name}/train | Train the named text classifier.


# **text_classifier_add_training_samples**
> TotalSamples text_classifier_add_training_samples(instance_name, labelled_text_sample_list)

Add training samples.

Add training samples to named text classifier.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.TextClassifiersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = feersum_nlu.LabelledTextSampleList() # LabelledTextSampleList | List of labelled text samples.

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
 **labelled_text_sample_list** | [**LabelledTextSampleList**](LabelledTextSampleList.md)| List of labelled text samples. | 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_create**
> InstanceDetail text_classifier_create(create_details)

Create a text classifier.

Create a new text classifier or load one from the store.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.TextClassifiersApi()
create_details = feersum_nlu.CreateDetails() # CreateDetails | The details of the instance to create.

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
 **create_details** | [**CreateDetails**](CreateDetails.md)| The details of the instance to create. | 

### Return type

[**InstanceDetail**](InstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_del_training_samples**
> LabelledTextSampleList text_classifier_del_training_samples(instance_name)

Delete training samples.

Delete the training samples of the named text classifier.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.TextClassifiersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.

try: 
    # Delete training samples.
    api_response = api_instance.text_classifier_del_training_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextClassifiersApi->text_classifier_del_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**LabelledTextSampleList**](LabelledTextSampleList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_details**
> InstanceDetail text_classifier_get_details(instance_name)

Get details of named instance.

Get the details of the named text classifier instance.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.TextClassifiersApi()
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

[**InstanceDetail**](InstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_details_all**
> InstanceDetailList text_classifier_get_details_all()

Get list of loaded text classifiers.

Get the list of loaded text classifiers.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.TextClassifiersApi()

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

[**InstanceDetailList**](InstanceDetailList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_get_training_samples**
> LabelledTextSampleList text_classifier_get_training_samples(instance_name)

Get training samples.

Get the training samples of the named text classifier.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.TextClassifiersApi()
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

[**LabelledTextSampleList**](LabelledTextSampleList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_retrieve**
> ScoredLabelList text_classifier_retrieve(instance_name, text_input)

Classify text.

Classifies the text and returns a probability sorted list of classes.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.TextClassifiersApi()
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

[**ScoredLabelList**](ScoredLabelList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_classifier_train**
> InstanceDetail text_classifier_train(instance_name, train_details)

Train the named text classifier.

Train the named text classifier with the training and testing data already provided.

### Example 
```python
from __future__ import print_statement
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# feersum_nlu.configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.TextClassifiersApi()
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

[**InstanceDetail**](InstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

