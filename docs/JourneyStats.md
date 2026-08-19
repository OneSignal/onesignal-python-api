# JourneyStats

Journey-level counts plus flat, id-keyed maps of node and branch stats. Contains no definition detail; join it by id against the journey from View journey.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID of the journey these stats belong to. | [optional] 
**started** | **int** | Users who entered the journey. | [optional] 
**completed** | **int** | Users who reached the end of the journey normally. | [optional] 
**exited_early** | **int** | Users who left the journey through an early exit rule. | [optional] 
**nodes** | [**{str: (JourneyNodeStats,)}**](JourneyNodeStats.md) | Node stats keyed by node id. Includes every node in the graph, at any nesting depth. | [optional] 
**branches** | [**{str: (JourneyBranchStats,)}**](JourneyBranchStats.md) | Branch stats keyed by branch id. Empty for a journey with no branching nodes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


