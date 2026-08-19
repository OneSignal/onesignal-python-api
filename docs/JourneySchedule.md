# JourneySchedule

Optional future start and/or stop time. null means no scheduled activation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_at** | **str, none_type** | ISO 8601 start time. Use UTC (Z or +00:00). Must be at least 5 minutes in the future. | [optional] 
**stop_at** | **str, none_type** | ISO 8601 stop time. Use UTC (Z or +00:00). Must be in the future and later than start_at. | [optional] 
**error** | **str, none_type** | Read-only. Present when a scheduling error occurred. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


