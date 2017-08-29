# feersum_nlu.RegexEntityExtractorsApi

All URIs are relative to *http://127.0.0.1:8000/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regex_entity_extractor_create**](RegexEntityExtractorsApi.md#regex_entity_extractor_create) | **POST** /regex_entity_extractors | Create a regular expression entity extractor.
[**regex_entity_extractor_get_details**](RegexEntityExtractorsApi.md#regex_entity_extractor_get_details) | **GET** /regex_entity_extractors/{instance_name} | Get details of named instance.
[**regex_entity_extractor_get_details_all**](RegexEntityExtractorsApi.md#regex_entity_extractor_get_details_all) | **GET** /regex_entity_extractors | Get list of loaded regular expression entity extractors.
[**regex_entity_extractor_retrieve**](RegexEntityExtractorsApi.md#regex_entity_extractor_retrieve) | **POST** /regex_entity_extractors/{instance_name}/retrieve | Extract information based on the regular expression.


# **regex_entity_extractor_create**
> RegexInstanceDetail regex_entity_extractor_create(regex_ent_create_details)

Create a regular expression entity extractor.

Create a new regular expression entity extractor or load one from the store.

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
api_instance = feersum_nlu.RegexEntityExtractorsApi()
regex_ent_create_details = feersum_nlu.RegexEntCreateDetails() # RegexEntCreateDetails | The details of the instance to create.

try: 
    # Create a regular expression entity extractor.
    api_response = api_instance.regex_entity_extractor_create(regex_ent_create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegexEntityExtractorsApi->regex_entity_extractor_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regex_ent_create_details** | [**RegexEntCreateDetails**](RegexEntCreateDetails.md)| The details of the instance to create. | 

### Return type

[**RegexInstanceDetail**](RegexInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regex_entity_extractor_get_details**
> RegexInstanceDetail regex_entity_extractor_get_details(instance_name)

Get details of named instance.

Get the details of the named regular expression entity extractor instance.

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
api_instance = feersum_nlu.RegexEntityExtractorsApi()
instance_name = 'instance_name_example' # str | The name of the model instance.

try: 
    # Get details of named instance.
    api_response = api_instance.regex_entity_extractor_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegexEntityExtractorsApi->regex_entity_extractor_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**RegexInstanceDetail**](RegexInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regex_entity_extractor_get_details_all**
> RegexInstanceDetailList regex_entity_extractor_get_details_all()

Get list of loaded regular expression entity extractors.

Get the list of loaded regular expression entity extractors.

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
api_instance = feersum_nlu.RegexEntityExtractorsApi()

try: 
    # Get list of loaded regular expression entity extractors.
    api_response = api_instance.regex_entity_extractor_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegexEntityExtractorsApi->regex_entity_extractor_get_details_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegexInstanceDetailList**](RegexInstanceDetailList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regex_entity_extractor_retrieve**
> EntityList regex_entity_extractor_retrieve(instance_name, text_input)

Extract information based on the regular expression.

Extract the entities matching the regular expression.

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
api_instance = feersum_nlu.RegexEntityExtractorsApi()
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try: 
    # Extract information based on the regular expression.
    api_response = api_instance.regex_entity_extractor_retrieve(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegexEntityExtractorsApi->regex_entity_extractor_retrieve: %s\n" % e)
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

