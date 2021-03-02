# TextClassifierInstanceDetail

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
**training_cm** | **object** | The confusion matrix as measured on the training set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used. | [optional] 
**testing_accuracy** | **float** | The accuracy of the model as measured on the testing set. | [optional] 
**testing_f1** | **float** | The average F-score of the model as measured on the testing set. | [optional] 
**testing_cm** | **object** | The confusion matrix as measured on the testing set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used. | [optional] 
**training_sorted_cm_labels** | **object** | A list that, if present, proposes the order of the labels of the confusion matrix. | [optional] 
**testing_sorted_cm_labels** | **object** | A list that, if present, proposes the order of the labels of the confusion matrix. | [optional] 
**testing_weighted_avg_stats** | **object** | Some model performance stats. | [optional] 
**training_stamp** | **str** | The time when the training operation concluded. | [optional] 
**num_training_samples** | **int** | The model&#39;s number of training samples. | [optional] 
**num_testing_samples** | **int** | The model&#39;s number of testing samples. | [optional] 
**clsfr_algorithm** | **str** | The name of the algorithm that should be used for the classification. | [optional] 
**language_model_list** | [**list[LabelledLanguageModel]**](LabelledLanguageModel.md) | The list of labelled language models used as sentence encoders. | [optional] 
**threshold** | **float** | There is typically some model dependent threshold to be set upon training and which is possibly mutable post training. This is that threshold. | [optional] 
**temperature** | **float** | The softmax temperature. The lower the temperature the more pronounced the winning class&#39; probability will be. The default is 1.0. A lower temperature is useful in a many class problem when the probabilty might otherwise be diluted amongst the classes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


