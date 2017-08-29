# feersum_nlu.DucklingEntityExtractorsApi

All URIs are relative to *http://127.0.0.1:8000/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**duckling_entity_extractor_create**](DucklingEntityExtractorsApi.md#duckling_entity_extractor_create) | **POST** /duckling_entity_extractors | Create a duckling entity extractor.
[**duckling_entity_extractor_get_details**](DucklingEntityExtractorsApi.md#duckling_entity_extractor_get_details) | **GET** /duckling_entity_extractors/{instance_name} | Get details of named instance.
[**duckling_entity_extractor_get_details_all**](DucklingEntityExtractorsApi.md#duckling_entity_extractor_get_details_all) | **GET** /duckling_entity_extractors | Get list of loaded regular expression entity extractors.
[**duckling_entity_extractor_retrieve**](DucklingEntityExtractorsApi.md#duckling_entity_extractor_retrieve) | **POST** /duckling_entity_extractors/{instance_name}/retrieve | Extract information based on the regular expression.


# **duckling_entity_extractor_create**
> DucklingInstanceDetail duckling_entity_extractor_create(duckling_ent_create_details)

Create a duckling entity extractor.

Create a new duckling entity extractor or load one from the store.

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
api_instance = feersum_nlu.DucklingEntityExtractorsApi()
duckling_ent_create_details = feersum_nlu.DucklingEntCreateDetails() # DucklingEntCreateDetails | The details of the instance to create.

try: 
    # Create a duckling entity extractor.
    api_response = api_instance.duckling_entity_extractor_create(duckling_ent_create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DucklingEntityExtractorsApi->duckling_entity_extractor_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duckling_ent_create_details** | [**DucklingEntCreateDetails**](DucklingEntCreateDetails.md)| The details of the instance to create. | 

### Return type

[**DucklingInstanceDetail**](DucklingInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duckling_entity_extractor_get_details**
> DucklingInstanceDetail duckling_entity_extractor_get_details(instance_name)

Get details of named instance.

Get the details of the named duckling entity extractor instance.

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
api_instance = feersum_nlu.DucklingEntityExtractorsApi()
instance_name = 'instance_name_example' # str | The name of the model instance.

try: 
    # Get details of named instance.
    api_response = api_instance.duckling_entity_extractor_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DucklingEntityExtractorsApi->duckling_entity_extractor_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**DucklingInstanceDetail**](DucklingInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duckling_entity_extractor_get_details_all**
> DucklingInstanceDetailList duckling_entity_extractor_get_details_all()

Get list of loaded regular expression entity extractors.

Get the list of loaded duckling entity extractors.

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
api_instance = feersum_nlu.DucklingEntityExtractorsApi()

try: 
    # Get list of loaded regular expression entity extractors.
    api_response = api_instance.duckling_entity_extractor_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DucklingEntityExtractorsApi->duckling_entity_extractor_get_details_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DucklingInstanceDetailList**](DucklingInstanceDetailList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duckling_entity_extractor_retrieve**
> EntityList duckling_entity_extractor_retrieve(instance_name, text_input)

Extract information based on the regular expression.

Extract the entities parsed by duckling.

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
api_instance = feersum_nlu.DucklingEntityExtractorsApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try: 
    # Extract information based on the regular expression.
    api_response = api_instance.duckling_entity_extractor_retrieve(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DucklingEntityExtractorsApi->duckling_entity_extractor_retrieve: %s\n" % e)
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

