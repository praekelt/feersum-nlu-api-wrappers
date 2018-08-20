# TrainDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **float** | There is typically some model dependent threshold to be set upon training which is possibly mutable post training. This is that threshold. | [optional] 
**immediate_mode** | **bool** | Set immediate_mode to True to do synchronous/blocking training. Might be forced to False in production. | [optional] 
**word_manifold** | **str** | The word manifold instance to use for training and later inference.  Rather use the word_manifold_list for supplying a language labelled list of word manifold instances to use in a multi-language system.  | [optional] 
**word_manifold_list** | [**list[LabeledWordManifold]**](LabeledWordManifold.md) | The list of labelled word manifolds to use for training. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


