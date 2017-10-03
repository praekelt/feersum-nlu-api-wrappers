# feersum_nlu.WordManifoldsApi

All URIs are relative to *http://nlu.playground.feersum.io:8100/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**word_manifold_add_similar_words**](WordManifoldsApi.md#word_manifold_add_similar_words) | **POST** /word_manifolds/{instance_name}/vocab | Add new words.
[**word_manifold_create**](WordManifoldsApi.md#word_manifold_create) | **POST** /word_manifolds | Create a word manifold model.


# **word_manifold_add_similar_words**
> InstanceDetail word_manifold_add_similar_words(instance_name, new_word_list)

Add new words.

Add new words to the manifold that are similar to existing words and save the manifold. Warning! - Because this operation saves the updated word manifold to the store it could take a few seconds to complete.

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
api_instance = feersum_nlu.WordManifoldsApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
new_word_list = feersum_nlu.NewWordList() # NewWordList | List of new words.

try: 
    # Add new words.
    api_response = api_instance.word_manifold_add_similar_words(instance_name, new_word_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordManifoldsApi->word_manifold_add_similar_words: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **new_word_list** | [**NewWordList**](NewWordList.md)| List of new words. | 

### Return type

[**InstanceDetail**](InstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **word_manifold_create**
> InstanceDetail word_manifold_create(create_details)

Create a word manifold model.

Create a new word manifold model using an input file or load a model from the store. Warning! - These models are quite big and each takes a few seconds to load/create.

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
api_instance = feersum_nlu.WordManifoldsApi()
create_details = feersum_nlu.CreateDetails() # CreateDetails | The details of the instance to create.

try: 
    # Create a word manifold model.
    api_response = api_instance.word_manifold_create(create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordManifoldsApi->word_manifold_create: %s\n" % e)
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

