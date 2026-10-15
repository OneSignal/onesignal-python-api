# EmailProviderMetricsEvent

Email metrics for a single time bucket, totaled across the requested inbox providers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **datetime** | The start of the time bucket, aligned to the hour, day, or month in UTC. | [optional] 
**metrics** | [**EmailMetrics**](EmailMetrics.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


