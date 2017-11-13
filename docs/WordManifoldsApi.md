# feersum_nlu.WordManifoldsApi

All URIs are relative to *https://nlu.playground.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**word_manifold_add_similar_words**](WordManifoldsApi.md#word_manifold_add_similar_words) | **POST** /word_manifolds/{instance_name}/vocab | Add new words.
[**word_manifold_create**](WordManifoldsApi.md#word_manifold_create) | **POST** /word_manifolds | Create a word manifold model.
[**word_manifold_get_similar_words**](WordManifoldsApi.md#word_manifold_get_similar_words) | **POST** /word_manifolds/{instance_name}/similar_words | Find similar words.
[**word_manifold_spell_correct**](WordManifoldsApi.md#word_manifold_spell_correct) | **POST** /word_manifolds/{instance_name}/spell_correct | Spell correct a word.


# **word_manifold_add_similar_words**
> InstanceDetail word_manifold_add_similar_words(instance_name, new_word_list)

Add new words.

Add new words to the manifold that are similar to existing words and save the manifold. Warning! - Because this operation saves the updated word manifold to the store it could take a few seconds to complete. Returns the details of the updated instance.

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

Create a new word manifold model using an input file or load a model from the store. Warning! - These models are quite big and each takes a few seconds to load/create. Returns the details of the new or loaded instance.

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

# **word_manifold_get_similar_words**
> WordAndDistanceList word_manifold_get_similar_words(instance_name, word_and_threshold)

Find similar words.

Returns words from the manifold that are similar to the parameter word.

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
word_and_threshold = feersum_nlu.WordAndThreshold() # WordAndThreshold | A word token and an accompanying threshold.

try: 
    # Find similar words.
    api_response = api_instance.word_manifold_get_similar_words(instance_name, word_and_threshold)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordManifoldsApi->word_manifold_get_similar_words: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **word_and_threshold** | [**WordAndThreshold**](WordAndThreshold.md)| A word token and an accompanying threshold. | 

### Return type

[**WordAndDistanceList**](WordAndDistanceList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **word_manifold_spell_correct**
> WordAndDistanceList word_manifold_spell_correct(instance_name, text_input)

Spell correct a word.

Spell correct a word replacing it with the most likely word from the manifold. Returns one or more scored candidate words.

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
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try: 
    # Spell correct a word.
    api_response = api_instance.word_manifold_spell_correct(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordManifoldsApi->word_manifold_spell_correct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 

### Return type

[**WordAndDistanceList**](WordAndDistanceList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
