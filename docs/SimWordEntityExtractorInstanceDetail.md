# SimWordEntityExtractorInstanceDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sluggy-url-friendly-name of the instance. | 
**id** | **str** | The unique id of a specific version of the model instance. | 
**long_name** | **str** | The human-friendly-name of the instance. | [optional] 
**desc** | **str** | The longer existential description of this instance&#39;s purpose in life. | [optional] 
**readonly** | **bool** | Indicates if the model is readonly and not editable. | [optional] 
**similar_words** | **list[str]** | The list of similar words to test against. | 
**threshold** | **float** | The threshold below which words are not similar. | 
**word_manifold** | **str** | The word manifold used to measure word similarity. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


