# EmailProviderMetricsTimeseriesResponse

Email metrics for a sending domain over time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**[EmailProviderMetricsEvent]**](EmailProviderMetricsEvent.md) | One entry for every time bucket in the reporting window, oldest first. Buckets with no email activity are included with all metrics set to `0`. Empty when the domain is not found for the app or is not currently active for sending. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


