# InstanceDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the model instance. | 
**id** | **str** | The unique id of a specific version of the model instance. | [optional] 
**desc** | **str** | A longer description of the model instance&#39;s purpose in life. | [optional] 
**training_accuracy** | **float** | The accuracy of the model as measured on the training set. | [optional] 
**peak_api_hit_rate** | **float** | The peak api hit rate (hits/s) over the last couple of window periods. A window period is in the order of 5 minutes. | [optional] 
**training_stamp** | **str** | The time when the training operation concluded. | [optional] 
**training_cm** | **object** | The confusion matrix as measured on the training set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used. | [optional] 
**cm_labels** | **object** | A dict that, if present, maps from the confusion matrix row and column labels to longer more descriptive labels. For example, if present it maps an FAQ answer ID to the string answer which may be either a label or the full text answer. | [optional] 
**model_type** | **str** | The type of this model. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


