# LanguageRecogniserCreateDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sluggy-url-friendly-name of the instance to create. | 
**long_name** | **str** | The human-friendly-name of the instance. | [optional] 
**desc** | **str** | The longer existential description of this instance&#39;s purpose in life. | [optional] 
**lid_model_file** | **str** | The pre-trained LID model to load. | [optional] 
**load_from_store** | **bool** | Indicates if a pre-existing model with the specified name should be reloaded from the trash. Usually set to False in which case a new model is created with details as specified. | 
**revision_uuid** | **str** | If provided, the uuid of the revision of the instance to try and load from the history. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


