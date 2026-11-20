# JourneySchemaResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The requested operation. | 
**document** | **str** | The document that the schema describes. For update_node, merged_node is the complete node after applying the patch. | 
**schema** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A self-contained JSON Schema Draft 6 document with local $defs references. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


