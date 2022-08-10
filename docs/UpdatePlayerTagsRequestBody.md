# UpdatePlayerTagsRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Custom tags for the device record.  Only support string key value pairs.  Does not support arrays or other nested objects.  Example `{\"foo\":\"bar\",\"this\":\"that\"}`. Limitations: - 100 tags per call - Android SDK users: tags cannot be removed or changed via API if set through SDK sendTag methods. Recommended to only tag devices with 1 kilobyte of ata Please consider using your own Database to save more than 1 kilobyte of data.  See: Internal Database & CRM  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


