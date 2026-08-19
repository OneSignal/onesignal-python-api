# JourneyBranch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Server-assigned branch identifier. Read-only on create; echo it on update to keep the branch. | [optional] 
**condition** | [**JourneyCondition**](JourneyCondition.md) |  | [optional] 
**weight** | **float** | Branch weight for split_range nodes. Weights across a node's branches must sum to 100. | [optional] 
**nodes** | [**[JourneyNode]**](JourneyNode.md) | Nodes run when this branch is taken, before flow converges to the next sibling node. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


