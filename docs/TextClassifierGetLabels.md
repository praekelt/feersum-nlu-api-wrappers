# TextClassifierGetLabels

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sluggy-url-friendly-name of the instance. | [optional] 
**long_name** | **str** | The human-friendly-name of the instance. | [optional] 
**desc** | **str** | The longer existential description of this instance&#39;s purpose in life. | [optional] 
**load_from_store** | **bool** | Indicates if a pre-existing model with the specified name should be reloaded from the trash. Usually set to False in which case a new model is created with details as specified. | [optional] 
**revision_uuid** | **str** | If provided, the uuid of the revision of the instance to try and load from the history. | [optional] 
**labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md) | List of labelled text samples. | [optional] 
**score** | **float** | The quality metric to track the performance of active labelling. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


