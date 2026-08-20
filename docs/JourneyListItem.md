# JourneyListItem

Summary journey representation returned by the list endpoint. Excludes description, nodes, early-exit configuration, and concurrency_key.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Journey UUID. Read-only. | [optional] 
**app_id** | **str** | UUID of the app the journey belongs to. Read-only. | [optional] 
**name** | **str** | Journey name, up to 300 characters. | [optional] 
**state** | **str** | Journey state. New journeys are created as draft. processing is transient while activation is in progress. archived is a journey that has been stopped. Change it through the state field on Update journey. | [optional] 
**created_at** | **str** | ISO 8601 creation time. Read-only. | [optional] 
**updated_at** | **str** | ISO 8601 last-update time. Read-only. | [optional] 
**started_at** | **str, none_type** | ISO 8601 time the journey was activated, or null. Read-only. | [optional] 
**archived_at** | **str, none_type** | ISO 8601 time the journey was archived, or null. Read-only. | [optional] 
**created_source** | **str, none_type** | Origin of the journey, for example public_api or dashboard. Read-only. | [optional] 
**schedule** | [**JourneySchedule**](JourneySchedule.md) |  | [optional] 
**audience** | [**JourneyListAudience**](JourneyListAudience.md) |  | [optional] 
**reentry_rules** | [**JourneyReentryRules**](JourneyReentryRules.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


