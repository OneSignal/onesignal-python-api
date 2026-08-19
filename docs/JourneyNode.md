# JourneyNode

A journey node. The kind field selects which other fields apply. Branching nodes (split_range, yes_no, wait_until) nest their sub-graphs inline via branches[].nodes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Node kind. Selects which other fields apply. | 
**id** | **str** | Server-assigned node UUID. Returned on reads. Required on update to keep an existing node. Rejected on create with a 400 validation error. | [optional] 
**client_node_id** | **str** | Optional client-assigned identifier, unique within the journey. Use it to reference this node from elsewhere in the same request. Persisted and returned on reads. | [optional] 
**annotation** | **str** | Optional free-text label, up to 255 characters. Stored and returned as-is with no effect on journey behavior. | [optional] 
**duration_seconds** | **int, none_type** | wait nodes: seconds to hold the user. Minimum 60, maximum 31556952 (1 year). | [optional] 
**relative_to** | **str** | time_window nodes: schedule_in_timezone uses the configured windows; last_active_time holds relative to the user's last active time. | [optional] 
**windows** | [**[JourneyTimeWindow]**](JourneyTimeWindow.md) | time_window nodes: one or more time windows. A window with no day_of_week applies to every day. Required when relative_to is schedule_in_timezone; omit when it is last_active_time. | [optional] 
**time_zone** | **str** | time_window nodes: IANA timezone identifier used when the user's timezone is unavailable. | [optional] 
**use_user_time_zone** | **bool, none_type** | time_window nodes: when true, uses the user's timezone if available. | [optional] 
**template_id** | **str** | send_push, send_email, and send_sms nodes: UUID of the template to send. | [optional] 
**iam_id** | **str** | send_iam nodes: UUID of the in-app message to send. | [optional] 
**user_ttl_seconds** | **int, none_type** | send_iam nodes: optional time-to-live for the in-app message, in seconds. | [optional] 
**webhook_id** | **str** | send_webhook nodes: UUID of the webhook to send. | [optional] 
**assignments** | **{str: (str,)}** | tag nodes: tag key-value pairs to assign. An empty string value removes the tag. Keys are limited to 255 characters and values to 1024. | [optional] 
**randomize_on_entry** | **bool, none_type** | split_range nodes: when true, assigns each user to a branch at random on entry. Defaults to false. | [optional] 
**branches** | [**[JourneyBranch]**](JourneyBranch.md) | Branching nodes: nested branches. split_range requires 2-20 weighted branches that sum to 100. yes_no requires exactly 2 branches. wait_until requires 1-10 condition branches. | [optional] 
**expiration** | [**JourneyWaitUntilExpiration**](JourneyWaitUntilExpiration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


