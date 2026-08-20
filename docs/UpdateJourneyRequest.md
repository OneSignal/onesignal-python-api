# UpdateJourneyRequest

Partial update applied with JSON Merge Patch (RFC 7396). Send only the fields you want to change. A null value clears a nullable field. Arrays such as nodes are replaced wholesale.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Journey name. | [optional] 
**description** | **str, none_type** | Journey description. Send null to clear it. | [optional] 
**audience** | [**JourneyAudience**](JourneyAudience.md) |  | [optional] 
**early_exit** | [**JourneyEarlyExit**](JourneyEarlyExit.md) |  | [optional] 
**reentry_rules** | [**JourneyReentryRules**](JourneyReentryRules.md) |  | [optional] 
**schedule** | [**JourneySchedule**](JourneySchedule.md) |  | [optional] 
**nodes** | [**[JourneyNode]**](JourneyNode.md) | Full ordered list of nodes, which replaces the existing graph wholesale. Preserve each node's server-assigned id from a prior fetch to keep in-flight users on that node; omit id to add a new node. | [optional] 
**state** | **str** | Target state. Set active to activate a draft journey, or scheduled together with a future schedule.start_at to activate it later. Set archived to stop a running journey; archiving is permanent. Only scheduled and processing journeys can return to draft. | [optional] 
**concurrency_key** | **str, none_type** | Optional optimistic-concurrency token. Pass the concurrency_key from a prior fetch to reject the update with 409 if the journey changed. Omit to skip the check. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


