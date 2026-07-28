# AuditLogActor

The user or service that performed the action. Absent if the actor is unknown.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the actor. Absent if unavailable. | [optional] 
**id** | **str** | UUID of the actor. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Additional actor-specific data. | [optional] 
**name** | **str** | Display name of the actor. Absent if unavailable. | [optional] 
**type** | **str** | Actor type (e.g. member, api_key, system). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


