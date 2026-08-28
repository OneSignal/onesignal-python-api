# EmailWarmUpStage

Channel: Email One stage of an Auto Warm Up campaign's sending schedule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | ISO 8601 timestamp for the start of this stage. Sending for this stage will not begin before this time. | 
**end** | **datetime** | ISO 8601 timestamp for the end of this stage. This stage's quota is expected to be sent by this time. | 
**quota** | **int** | Number of emails to send during this stage. | 
**acked** | **bool** | Whether this stage has been picked up and acknowledged by the warm-up scheduler. Not accepted on create. This is only present when reading back a campaign. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


