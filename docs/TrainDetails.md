# TrainDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **float** | There is typically some model dependent threshold to be set upon training which is possibly mutable post training. This is that threshold. | [optional] 
**temperature** | **float** | The softmax temperature. The lower the temperature the more pronounced the winning class&#39; probability will be. The default is 1.0. A lower temperature is useful in a many class problem when the probabilty might otherwise be diluted amongst the classes. | [optional] 
**immediate_mode** | **bool** | Set immediate_mode to True to do synchronous/blocking training. Might be forced to False in production. | [optional] 
**word_manifold** | **str** | The word manifold instance to use for training and later inference.  Rather use the word_manifold_list for supplying a language labelled list of word manifold instances to use in a multi-language system.  | [optional] 
**word_manifold_list** | [**list[LabelledWordManifold]**](LabelledWordManifold.md) | The list of labelled word manifolds to use for training. | [optional] 
**clsfr_algorithm** | **str** | The name of the algorithm that should be used for the classification. | [optional] 
**num_epochs** | **int** | The number of epochs to train the model for. | [optional] 
**language_model_list** | [**list[LabelledLanguageModel]**](LabelledLanguageModel.md) | The list of labelled language models used as sentence encoders. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


