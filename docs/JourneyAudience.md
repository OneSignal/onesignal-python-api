# JourneyAudience

The journey entry audience. The kind field selects which other fields apply.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Audience kind. Selects which other fields apply. | 
**included_segment_ids** | **[str]** | segment audiences: Segment UUIDs whose users enter the journey. | [optional] 
**excluded_segment_ids** | **[str]** | segment audiences: Segment UUIDs whose users are excluded. | [optional] 
**future_additions_only** | **bool, none_type** | segment audiences: when true, only users who newly match the segment after activation enter the journey. Defaults to false. | [optional] 
**name** | **str** | event_trigger audiences: event name that triggers entry, up to 255 characters. | [optional] 
**attributes** | [**JourneyEventTriggerAttributes**](JourneyEventTriggerAttributes.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


