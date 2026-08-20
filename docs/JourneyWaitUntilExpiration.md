# JourneyWaitUntilExpiration

Optional expiration timer. null waits indefinitely.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_seconds** | **int, none_type** | Seconds to wait before the timer fires. Minimum 60, maximum 31556952 (1 year). | [optional] 
**exits** | **bool, none_type** | When true, the user exits the journey when the timer fires; when false, the user continues to convergence. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


