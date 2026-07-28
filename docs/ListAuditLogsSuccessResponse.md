# ListAuditLogsSuccessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_logs** | [**[AuditLogEvent]**](AuditLogEvent.md) | Array of audit log events, ordered by occurred_at ascending. | [optional] 
**has_more** | **bool** | True if additional events exist beyond this page. Use next_cursor to fetch the next page. | [optional] 
**next_cursor** | **str** | Opaque cursor to pass as cursor in the next request. Only present when has_more is true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


