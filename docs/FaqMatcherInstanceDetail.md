# FaqMatcherInstanceDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sluggy-url-friendly-name of the instance. | 
**id** | **str** | The unique id of a specific version of the model instance. | 
**long_name** | **str** | The human-friendly-name of the instance. | [optional] 
**desc** | **str** | The longer existential description of this instance&#39;s purpose in life. | [optional] 
**training_accuracy** | **float** | The accuracy of the model as measured on the training set. | [optional] 
**training_f1** | **float** | The average F-score of the model as measured on the training set. | [optional] 
**training_cm** | **object** | The confusion matrix as measured on the training set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used. | [optional] 
**testing_accuracy** | **float** | The accuracy of the model as measured on the testing set. | [optional] 
**testing_f1** | **float** | The average F-score of the model as measured on the testing set. | [optional] 
**testing_cm** | **object** | The confusion matrix as measured on the testing set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used. | [optional] 
**cm_labels** | **object** | A dict that, if present, maps from the confusion matrix row and column labels to longer more descriptive labels. For example, if present it maps an FAQ answer ID to the string answer which may be either a label or the full text answer. | [optional] 
**training_stamp** | **str** | The time when the training operation concluded. | [optional] 
**word_manifold_list** | [**list[LabeledWordManifold]**](LabeledWordManifold.md) | The list of labelled word manifolds used for training. | [optional] 
**threshold** | **float** | There is typically some model dependent threshold to be set upon training and which is possibly mutable post training. This is that threshold. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


