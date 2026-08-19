# JourneyCondition

A branch condition. The kind field selects which other fields apply.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Condition kind. Selects which other fields apply. | 
**included_segment_ids** | **[str]** | segment_membership conditions: Segment UUIDs the user must belong to. | [optional] 
**excluded_segment_ids** | **[str]** | segment_membership conditions: Segment UUIDs the user must not belong to. | [optional] 
**action** | **str** | on_notification_action conditions: the notification action to branch on. Which actions apply depends on the sending node's channel. | [optional] 
**sending_node_id** | **str** | on_notification_action conditions: id of the sending node this action refers to. Returned on reads; accepted on write. | [optional] 
**client_node_id** | **str** | on_notification_action conditions: write-only alternative to sending_node_id. References the sending node by its client_node_id. | [optional] 
**name** | **str** | event_trigger conditions: event name, up to 255 characters. | [optional] 
**attributes** | [**JourneyEventTriggerAttributes**](JourneyEventTriggerAttributes.md) |  | [optional] 
**entry_event_match_attributes** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type** | event_trigger conditions: match incoming event properties against the journey's entry event. Only valid on event-triggered journeys. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


