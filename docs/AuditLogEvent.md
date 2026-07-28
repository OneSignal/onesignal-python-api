# AuditLogEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action that was performed (e.g. notification.sent, segment.created, member.invited). | [optional] 
**actor** | [**AuditLogActor**](AuditLogActor.md) |  | [optional] 
**app_id** | **str** | UUID of the app the event is associated with. Absent for org-level events. | [optional] 
**context** | [**AuditLogContext**](AuditLogContext.md) |  | [optional] 
**id** | **str** | UUID of the audit log event. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Additional event-specific data that does not fit into the standard fields. | [optional] 
**occurred_at** | **str** | RFC 3339 timestamp of when the event occurred (e.g. 2026-02-18T12:34:56Z). | [optional] 
**organization_id** | **str** | UUID of the organization the event belongs to. | [optional] 
**targets** | [**[AuditLogTarget]**](AuditLogTarget.md) | The resources the action was performed on. May be empty for org-level events. | [optional] 
**version** | **int** | Schema version of the event payload. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


