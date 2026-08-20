# Journey

Full journey representation returned by the detail, create, and update endpoints.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Journey UUID. Read-only. | [optional] 
**app_id** | **str** | UUID of the app the journey belongs to. Read-only. | [optional] 
**name** | **str** | Journey name, up to 300 characters. | [optional] 
**description** | **str, none_type** | Journey description, up to 1024 characters. Defaults to an empty string. | [optional] 
**state** | **str** | Journey state. New journeys are created as draft. processing is transient while activation is in progress. archived is a journey that has been stopped. Change it through the state field on Update journey. | [optional] 
**created_at** | **str** | ISO 8601 creation time. Read-only. | [optional] 
**updated_at** | **str** | ISO 8601 last-update time. Read-only. | [optional] 
**started_at** | **str, none_type** | ISO 8601 time the journey was activated, or null. Read-only. May stay null briefly after you set state to active: activation is enqueued, and started_at populates once the journey finishes processing. | [optional] 
**archived_at** | **str, none_type** | ISO 8601 time the journey was archived, or null. Read-only. | [optional] 
**created_source** | **str, none_type** | Origin of the journey, for example public_api or dashboard. Read-only. | [optional] 
**audience** | [**JourneyAudience**](JourneyAudience.md) |  | [optional] 
**early_exit** | [**JourneyEarlyExit**](JourneyEarlyExit.md) |  | [optional] 
**reentry_rules** | [**JourneyReentryRules**](JourneyReentryRules.md) |  | [optional] 
**schedule** | [**JourneySchedule**](JourneySchedule.md) |  | [optional] 
**nodes** | [**[JourneyNode]**](JourneyNode.md) | Ordered list of journey nodes. | [optional] 
**concurrency_key** | **str** | Opaque optimistic-concurrency token. Read-only. Pass it back on update to guard against overwriting a concurrent change (409). Send it back exactly as read; do not construct or parse it. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


