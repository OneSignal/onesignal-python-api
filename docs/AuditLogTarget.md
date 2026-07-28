# AuditLogTarget

A resource the action was performed on.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID of the resource. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Additional resource-specific data. | [optional] 
**name** | **str** | Display name of the resource. Absent if unavailable. | [optional] 
**type** | **str** | Resource type (e.g. notification, segment, journey, app). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


