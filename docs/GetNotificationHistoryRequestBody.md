# GetNotificationHistoryRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **str** | -> \"sent\" - All the devices by player_id that were sent the specified notification_id.  Notifications targeting under 1000 recipients will not have \"sent\" events recorded, but will show \"clicked\" events. \"clicked\" - All the devices by `player_id` that clicked the specified notification_id. | [optional] 
**email** | **str** | The email address you would like the report sent. | [optional] 
**app_id** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


