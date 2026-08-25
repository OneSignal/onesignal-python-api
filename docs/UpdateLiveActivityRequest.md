# UpdateLiveActivityRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An internal name to assist with your campaign organization. This does not get displayed in the message itself. | 
**event** | **str** |  | 
**event_updates** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | This must match the ContentState interface you have defined within your Live Activity in your app. | 
**contents** | [**LanguageStringMap**](LanguageStringMap.md) |  | [optional] 
**headings** | [**LanguageStringMap**](LanguageStringMap.md) |  | [optional] 
**sound** | **str** | Deprecated. The API ignores this field. Use `ios_sound`. | [optional] 
**ios_sound** | **str** | Sound file that is included in your app to play instead of the default device notification sound. Omit to disable vibration and sound for the notification. Requires `headings` on the same request: ActivityKit ignores an update whose alert has no title, which silently drops the sound. Supersedes the deprecated `sound` field.  | [optional] 
**stale_date** | **int** | Accepts Unix timestamp in seconds. When time reaches the configured stale date, the system considers the Live Activity out of date, and the ActivityState of the Live Activity changes to ActivityState.stale. | [optional] 
**dismissal_date** | **int** | Accepts Unix timestamp in seconds; only allowed if event is \"end\" | [optional] 
**priority** | **int** | Delivery priority through the push provider (APNs). Pass 10 for higher priority notifications, or 5 for lower priority notifications. Lower priority notifications are sent based on the power considerations of the end user's device. If not set, defaults to 10. Some providers (APNs) allow for a limited budget of high priority notifications per hour, and if that budget is exceeded, the provider may throttle notification delivery. | [optional] 
**ios_relevance_score** | **float, none_type** | A value between 0 and 1. When more than one Live Activity is active for your app, the one with the highest relevance score shows in the Dynamic Island. If the scores are equal, the system shows the Live Activity that started first. The score also sets the order of Live Activities on the Lock Screen. Only available on iOS 16.2 and later. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


