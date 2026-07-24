# SegmentDetails

Segment details. Only included when the include-segment-detail query parameter is set to true.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the segment (UUID v4). | [optional] 
**name** | **str** | The segment name. | [optional] 
**description** | **str, none_type** | Human-readable description for the segment. `null` when unset. Maximum 255 characters. | [optional] 
**created_at** | **int** | Unix timestamp when the segment was created. | [optional] 
**source** | **str** | The source of the segment. | [optional] 
**filters** | [**[FilterExpression]**](FilterExpression.md) | Array of filter and operator objects defining the segment criteria. Uses the same format as the Create Segment API, so filters can be directly used to recreate or update the segment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


