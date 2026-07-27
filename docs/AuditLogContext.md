# AuditLogContext

Request context at the time of the event. Absent if context was not captured.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country code derived from the request IP. | [optional] 
**ip** | **str** | IP address the request originated from. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Additional context-specific data. | [optional] 
**user_agent** | **str** | User agent of the client that made the request. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


