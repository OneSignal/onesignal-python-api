# JourneyListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journeys** | [**[JourneyListItem]**](JourneyListItem.md) | Journeys ordered by creation time, newest first. | [optional] 
**has_more** | **bool** | true if more journeys exist beyond this page. | [optional] 
**next_cursor** | **str** | Cursor for the next page. Present only when has_more is true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


