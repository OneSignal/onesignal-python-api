# ExportSubscriptionsRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_fields** | **[str]** | Additional fields that you wish to include. Currently supports location, country, rooted, notification_types, ip, external_user_id, web_auth, and web_p256. | [optional] 
**last_active_since** | **str** | Export all devices with a last_active timestamp greater than this time.  Unixtime in seconds. | [optional] 
**segment_name** | **str** | Export all devices belonging to the segment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


