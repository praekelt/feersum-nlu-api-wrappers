# feersum_nlu.WordManifoldsApi

All URIs are relative to *https://nlu.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**word_manifold_add_similar_words**](WordManifoldsApi.md#word_manifold_add_similar_words) | **POST** /word_manifolds/{instance_name}/vocab | Add new words.
[**word_manifold_create**](WordManifoldsApi.md#word_manifold_create) | **POST** /word_manifolds | Create a word manifold model.
[**word_manifold_del**](WordManifoldsApi.md#word_manifold_del) | **DELETE** /word_manifolds/{instance_name} | Delete named instance.
[**word_manifold_get_details**](WordManifoldsApi.md#word_manifold_get_details) | **GET** /word_manifolds/{instance_name} | Get details of named instance.
[**word_manifold_vaporise**](WordManifoldsApi.md#word_manifold_vaporise) | **POST** /word_manifolds/{instance_name}/vaporise | Vaporise the named model.


# **word_manifold_add_similar_words**
> WordManifoldInstanceDetail word_manifold_add_similar_words(instance_name, new_word_list)

Add new words.

Add new words to the manifold that are similar to existing words and save the manifold. Warning! - Because this operation saves the updated word manifold to the store it could take a few seconds to complete. Returns the details of the updated instance.

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
api_instance = feersum_nlu.WordManifoldsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
new_word_list = [feersum_nlu.NewWord()] # list[NewWord] | List of new words.

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
 **new_word_list** | [**list[NewWord]**](NewWord.md)| List of new words. | 

### Return type

[**WordManifoldInstanceDetail**](WordManifoldInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **word_manifold_create**
> WordManifoldInstanceDetail word_manifold_create(create_details)

Create a word manifold model.

Create a new word manifold model using an input file or reload one from the trash. Warning! - These models are quite big and each takes a few seconds to load/create. Returns the details of the new or loaded instance.

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
api_instance = feersum_nlu.WordManifoldsApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.WordManifoldCreateDetails() # WordManifoldCreateDetails | The details of the word manifold instance to create.

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
 **create_details** | [**WordManifoldCreateDetails**](WordManifoldCreateDetails.md)| The details of the word manifold instance to create. | 

### Return type

[**WordManifoldInstanceDetail**](WordManifoldInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **word_manifold_del**
> WordManifoldInstanceDetail word_manifold_del(instance_name)

Delete named instance.

Delete and return the details of the word manifold instance. Deleted models can be reloaded from the trash with the create operation.

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
api_instance = feersum_nlu.WordManifoldsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete named instance.
    api_response = api_instance.word_manifold_del(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordManifoldsApi->word_manifold_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**WordManifoldInstanceDetail**](WordManifoldInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **word_manifold_get_details**
> WordManifoldInstanceDetail word_manifold_get_details(instance_name)

Get details of named instance.

Get the details of the named word manifold instance.

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
api_instance = feersum_nlu.WordManifoldsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get details of named instance.
    api_response = api_instance.word_manifold_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordManifoldsApi->word_manifold_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**WordManifoldInstanceDetail**](WordManifoldInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **word_manifold_vaporise**
> WordManifoldInstanceDetail word_manifold_vaporise(instance_name)

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
api_instance = feersum_nlu.WordManifoldsApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Vaporise the named model.
    api_response = api_instance.word_manifold_vaporise(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordManifoldsApi->word_manifold_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**WordManifoldInstanceDetail**](WordManifoldInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

