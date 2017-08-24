# InstanceDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the model instance. | 
**id** | **str** | The unique id of a specific version of the model instance. | 
**desc** | **str** | A longer description of the model instances purpose in life. | [optional] 
**training_accuracy** | **float** | The accuracy of the model as measured on the training set. | [optional] 
**training_stamp** | **str** | The time when the training operation concluded. | [optional] 
**training_cm** | **object** | The confusion matrix as measured on the training set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


