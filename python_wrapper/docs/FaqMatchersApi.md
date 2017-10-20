# feersum_nlu.FaqMatchersApi

All URIs are relative to *http://nlu.playground.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**faq_matcher_add_training_samples**](FaqMatchersApi.md#faq_matcher_add_training_samples) | **POST** /faq_matchers/{instance_name}/training_samples | Add training samples.
[**faq_matcher_create**](FaqMatchersApi.md#faq_matcher_create) | **POST** /faq_matchers | Create an FAQ matcher.
[**faq_matcher_curate**](FaqMatchersApi.md#faq_matcher_curate) | **POST** /faq_matchers/{instance_name}/curate | Endpoint to aid in the curation of a model instance.
[**faq_matcher_del_training_samples**](FaqMatchersApi.md#faq_matcher_del_training_samples) | **DELETE** /faq_matchers/{instance_name}/training_samples | Delete training samples.
[**faq_matcher_get_details**](FaqMatchersApi.md#faq_matcher_get_details) | **GET** /faq_matchers/{instance_name} | Get details of named instance.
[**faq_matcher_get_details_all**](FaqMatchersApi.md#faq_matcher_get_details_all) | **GET** /faq_matchers | Get list of loaded FAQ matchers.
[**faq_matcher_get_labels**](FaqMatchersApi.md#faq_matcher_get_labels) | **GET** /faq_matchers/{instance_name}/get_labels | Get list of possible labels.
[**faq_matcher_get_training_samples**](FaqMatchersApi.md#faq_matcher_get_training_samples) | **GET** /faq_matchers/{instance_name}/training_samples | Get training samples.
[**faq_matcher_retrieve**](FaqMatchersApi.md#faq_matcher_retrieve) | **POST** /faq_matchers/{instance_name}/retrieve | Match retrieve and FAQ.
[**faq_matcher_train**](FaqMatchersApi.md#faq_matcher_train) | **POST** /faq_matchers/{instance_name}/train | Train the named FAQ matcher.


# **faq_matcher_add_training_samples**
> TotalSamples faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)

Add training samples.

Add training samples to named faq matcher.

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
api_instance = feersum_nlu.FaqMatchersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = feersum_nlu.LabelledTextSampleList() # LabelledTextSampleList | List of labelled text samples.

try: 
    # Add training samples.
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_add_training_samples: %s\n" % e)
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

# **faq_matcher_create**
> InstanceDetail faq_matcher_create(create_details)

Create an FAQ matcher.

Create a new faq matcher or load one from the store.

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
api_instance = feersum_nlu.FaqMatchersApi()
create_details = feersum_nlu.CreateDetails() # CreateDetails | The details of the instance to create.

try: 
    # Create an FAQ matcher.
    api_response = api_instance.faq_matcher_create(create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_create: %s\n" % e)
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

# **faq_matcher_curate**
> LabelledTextSampleList faq_matcher_curate(instance_name, label_pair)

Endpoint to aid in the curation of a model instance.

Access the list of samples behind a cell of the confusion matrix of the training or testing samples.

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
api_instance = feersum_nlu.FaqMatchersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
label_pair = feersum_nlu.ClassLabelPair() # ClassLabelPair | The true label, predicted label and matrix (train/test) to use.

try: 
    # Endpoint to aid in the curation of a model instance.
    api_response = api_instance.faq_matcher_curate(instance_name, label_pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_curate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **label_pair** | [**ClassLabelPair**](ClassLabelPair.md)| The true label, predicted label and matrix (train/test) to use. | 

### Return type

[**LabelledTextSampleList**](LabelledTextSampleList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del_training_samples**
> LabelledTextSampleList faq_matcher_del_training_samples(instance_name)

Delete training samples.

Delete the training samples of the named FAQ matcher.

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
api_instance = feersum_nlu.FaqMatchersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.

try: 
    # Delete training samples.
    api_response = api_instance.faq_matcher_del_training_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_training_samples: %s\n" % e)
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

# **faq_matcher_get_details**
> InstanceDetail faq_matcher_get_details(instance_name)

Get details of named instance.

Get the details of the named FAQ matcher instance.

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
api_instance = feersum_nlu.FaqMatchersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.

try: 
    # Get details of named instance.
    api_response = api_instance.faq_matcher_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_details: %s\n" % e)
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

# **faq_matcher_get_details_all**
> InstanceDetailList faq_matcher_get_details_all()

Get list of loaded FAQ matchers.

Get the list of loaded faq matchers.

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
api_instance = feersum_nlu.FaqMatchersApi()

try: 
    # Get list of loaded FAQ matchers.
    api_response = api_instance.faq_matcher_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_details_all: %s\n" % e)
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

# **faq_matcher_get_labels**
> ClassLabelList faq_matcher_get_labels(instance_name)

Get list of possible labels.

Returns the classifier's list of possible class labels.

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
api_instance = feersum_nlu.FaqMatchersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.

try: 
    # Get list of possible labels.
    api_response = api_instance.faq_matcher_get_labels(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**ClassLabelList**](ClassLabelList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_training_samples**
> LabelledTextSampleList faq_matcher_get_training_samples(instance_name)

Get training samples.

Get the training samples of the named faq matcher.

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
api_instance = feersum_nlu.FaqMatchersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.

try: 
    # Get training samples.
    api_response = api_instance.faq_matcher_get_training_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_training_samples: %s\n" % e)
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

# **faq_matcher_retrieve**
> ScoredLabelList faq_matcher_retrieve(instance_name, text_input)

Match retrieve and FAQ.

Matchers the FAQ and returns a probability sorted list of answer labels.

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
api_instance = feersum_nlu.FaqMatchersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try: 
    # Match retrieve and FAQ.
    api_response = api_instance.faq_matcher_retrieve(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_retrieve: %s\n" % e)
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

# **faq_matcher_train**
> InstanceDetail faq_matcher_train(instance_name, train_details)

Train the named FAQ matcher.

Train the named FAQ matcher with the training and testing data already provided.

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
api_instance = feersum_nlu.FaqMatchersApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.

try: 
    # Train the named FAQ matcher.
    api_response = api_instance.faq_matcher_train(instance_name, train_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_train: %s\n" % e)
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

