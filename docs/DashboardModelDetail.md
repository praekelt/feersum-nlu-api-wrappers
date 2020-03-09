# DashboardModelDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sluggy-url-friendly-name of the instance. | 
**uuid** | **str** | A universally unique ID used to reference this revision of the instance. | [optional] 
**long_name** | **str** | The human-friendly-name of the instance. | [optional] 
**desc** | **str** | The longer existential description of this instance&#39;s purpose in life. | [optional] 
**model_type** | **str** | The type of this model. | 
**collection_uri** | **str** | The URI of the model type&#39;s collection resource e.g. /faq_matchers for the collection of faq_matcher models. | 
**has_labels** | **bool** | Whether or not the model returns a list of scored labels. Unknown if flag not present. | [optional] 
**trashed** | **bool** | Whether or not this model has been deleted. Deleted models can be reloaded using the create opeeration. | [optional] 
**history** | [**list[ModelRevision]**](ModelRevision.md) | The model&#39;s history. The history includes the current version of the model only if the last update was pushed to the history. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


