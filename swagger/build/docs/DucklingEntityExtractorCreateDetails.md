# DucklingEntityExtractorCreateDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sluggy-url-friendly-name of the instance to create. | 
**long_name** | **str** | The human-friendly-name of the instance. | [optional] 
**desc** | **str** | The longer existential description of this instance&#39;s purpose in life. | [optional] 
**reference_time** | **str** | The reference time of the date parser. Uses international standard date notation &#39;YYYY-MM-DD hh:mm+hh:mm&#39; e.g. &#39;2017-12-01&#39;, &#39;2017-12-01 10:00&#39; (server local zone), &#39;2017-12-01 10:00+02:00&#39; | [optional] [default to '']
**load_from_store** | **bool** | Indicates if a pre-existing model with the specified name should be reloaded from the trash. Usually set to False in which case a new model is created with details as specified. | 
**revision_uuid** | **str** | If provided, the uuid of the revision of the instance to try and load from the history. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


