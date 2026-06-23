# NotificationSlice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**time_offset** | **str** | The time_offset cursor specified in the request, if any. | [optional] 
**next_time_offset** | **str** | An opaque Base64 cursor token representing the next page of messages to fetch.  Present when time_offset was provided in the request.  Pass this value as time_offset on the next request to continue paginating. | [optional] 
**notifications** | [**[NotificationWithMeta]**](NotificationWithMeta.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


