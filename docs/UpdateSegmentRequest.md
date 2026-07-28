# UpdateSegmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. The segment name. Maximum 128 characters. | 
**description** | **str** | Optional human-readable description for the segment. Maximum 255 characters. Pass an empty string to clear; omit to leave unchanged. | [optional] 
**filters** | [**[FilterExpression]**](FilterExpression.md) | Optional. When provided, replaces all existing filters. Filters define the segment based on user properties like tags, activity, or location using flexible AND/OR logic. Limited to 200 total entries, including fields and OR operators. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


