# SynonymEntityExtractorInstanceDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sluggy-url-friendly-name of the instance. | 
**id** | **str** | The unique id of a specific version of the instance. | 
**long_name** | **str** | The human-friendly-name of the instance. | [optional] 
**desc** | **str** | The longer existential description of this instance&#39;s purpose in life. | [optional] 
**readonly** | **bool** | Indicates if the model is readonly and not editable. | [optional] 
**training_accuracy** | **float** | The accuracy of the model as measured on the training set. | [optional] 
**training_f1** | **float** | The average F-score of the model as measured on the training set. | [optional] 
**validation_accuracy** | **float** | The accuracy of the model as measured by cross validation on the training set. | [optional] 
**validation_f1** | **float** | The average F-score of the model as measured by cross validation on the training set. | [optional] 
**testing_accuracy** | **float** | The accuracy of the model as measured on the testing set. | [optional] 
**testing_f1** | **float** | The average F-score of the model as measured on the testing set. | [optional] 
**training_stamp** | **str** | The time when the training operation concluded. | [optional] 
**num_training_samples** | **int** | The model&#39;s number of training samples. | [optional] 
**num_testing_samples** | **int** | The model&#39;s number of testing samples. | [optional] 
**threshold** | **float** | There is typically some model dependent threshold to be set upon training and which is possibly mutable post training. This is that threshold. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


