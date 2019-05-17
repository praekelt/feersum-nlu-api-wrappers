# SynonymEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | The entity label/class/type. | 
**value** | **str** | The value of the entity as extracted from the input text. Not used during training! | [optional] 
**syn_set** | **list[str]** | The list of synonyms associated with this entity label. One should either provide a synset OR an index and len of a specific synonym in the associated utterance. | [optional] 
**index** | **int** | The first character of the entity in the associated utterance. One should either provide a synset OR an index and len of a specific synonym in the associated utterance. | [optional] 
**len** | **int** | The length of the extracted entity in the associated utterance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


