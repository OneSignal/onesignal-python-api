# CreateJourneyRequest

Writable fields for Create journey. Journeys are always created in the draft state. Server-controlled fields such as state or id are rejected.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Journey name, up to 300 characters. | 
**description** | **str, none_type** | Optional journey description, up to 1024 characters. | [optional] 
**audience** | [**JourneyAudience**](JourneyAudience.md) |  | [optional] 
**early_exit** | [**JourneyEarlyExit**](JourneyEarlyExit.md) |  | [optional] 
**reentry_rules** | [**JourneyReentryRules**](JourneyReentryRules.md) |  | [optional] 
**schedule** | [**JourneySchedule**](JourneySchedule.md) |  | [optional] 
**nodes** | [**[JourneyNode]**](JourneyNode.md) | Ordered list of journey nodes. Server-assigned id fields are rejected on create. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


