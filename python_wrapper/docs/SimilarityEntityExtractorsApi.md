# feersum_nlu.SimilarityEntityExtractorsApi

All URIs are relative to *http://127.0.0.1:8000/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similarity_entity_extractor_create**](SimilarityEntityExtractorsApi.md#similarity_entity_extractor_create) | **POST** /similarity_entity_extractors | Create a word similarity entity extractor.
[**similarity_entity_extractor_get_details**](SimilarityEntityExtractorsApi.md#similarity_entity_extractor_get_details) | **GET** /similarity_entity_extractors/{instance_name} | Get details of named instance.
[**similarity_entity_extractor_get_details_all**](SimilarityEntityExtractorsApi.md#similarity_entity_extractor_get_details_all) | **GET** /similarity_entity_extractors | Get list of loaded similarity entity extractors.
[**similarity_entity_extractor_retrieve**](SimilarityEntityExtractorsApi.md#similarity_entity_extractor_retrieve) | **POST** /similarity_entity_extractors/{instance_name}/retrieve | Extract information based on word similarity.


# **similarity_entity_extractor_create**
> InstanceDetail similarity_entity_extractor_create(similarity_ent_create_details)

Create a word similarity entity extractor.

Create a new word similarity entity extractor or load one from the store.

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
api_instance = feersum_nlu.SimilarityEntityExtractorsApi()
similarity_ent_create_details = feersum_nlu.SimilarityEntCreateDetails() # SimilarityEntCreateDetails | The details of the instance to create.

try: 
    # Create a word similarity entity extractor.
    api_response = api_instance.similarity_entity_extractor_create(similarity_ent_create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarityEntityExtractorsApi->similarity_entity_extractor_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **similarity_ent_create_details** | [**SimilarityEntCreateDetails**](SimilarityEntCreateDetails.md)| The details of the instance to create. | 

### Return type

[**InstanceDetail**](InstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similarity_entity_extractor_get_details**
> InstanceDetail similarity_entity_extractor_get_details(instance_name)

Get details of named instance.

Get the details of the named similarity entity extractor instance.

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
api_instance = feersum_nlu.SimilarityEntityExtractorsApi()
instance_name = 'instance_name_example' # str | The name of the model instance.

try: 
    # Get details of named instance.
    api_response = api_instance.similarity_entity_extractor_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarityEntityExtractorsApi->similarity_entity_extractor_get_details: %s\n" % e)
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

# **similarity_entity_extractor_get_details_all**
> InstanceDetailList similarity_entity_extractor_get_details_all()

Get list of loaded similarity entity extractors.

Get the list of loaded similarity entity extractors.

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
api_instance = feersum_nlu.SimilarityEntityExtractorsApi()

try: 
    # Get list of loaded similarity entity extractors.
    api_response = api_instance.similarity_entity_extractor_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarityEntityExtractorsApi->similarity_entity_extractor_get_details_all: %s\n" % e)
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

# **similarity_entity_extractor_retrieve**
> EntityList similarity_entity_extractor_retrieve(instance_name, text_input)

Extract information based on word similarity.

Extract the word entities that are similar to the list of words.

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
api_instance = feersum_nlu.SimilarityEntityExtractorsApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try: 
    # Extract information based on word similarity.
    api_response = api_instance.similarity_entity_extractor_retrieve(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarityEntityExtractorsApi->similarity_entity_extractor_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 

### Return type

[**EntityList**](EntityList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

