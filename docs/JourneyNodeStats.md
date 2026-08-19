# JourneyNodeStats

Stats for a single node. Keyed in the response by the node's server-assigned id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Node kind, repeated here so stats can be read without joining against the journey definition. | [optional] 
**waiting** | **int** | Users currently held at this node. | [optional] 
**completed** | **int** | Users who advanced past this node normally. | [optional] 
**exited_early** | **int** | Users who left the journey from this node through an early exit rule. | [optional] 
**message_stats** | [**JourneyMessageStats**](JourneyMessageStats.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


