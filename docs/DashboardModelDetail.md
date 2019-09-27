# DashboardModelDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sluggy-url-friendly-name of the instance. | 
**long_name** | **str** | The human-friendly-name of the instance. | [optional] 
**desc** | **str** | The longer existential description of this instance&#39;s purpose in life. | [optional] 
**model_type** | **str** | The type of this model. | 
**collection_uri** | **str** | The URI of the model type&#39;s collection resource e.g. /faq_matchers for the collection of faq_matcher models. | 
**trashed** | **bool** | Whether or not this model has been deleted. Deleted models need to be loaded to be used again. | [optional] 
**history** | [**list[ModelRevision]**](ModelRevision.md) | The model&#39;s history. The history includes the current version of the model only if the last update was pushed to the history. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


