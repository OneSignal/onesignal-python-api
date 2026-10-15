# EmailProviderMetricsResponse

Email metrics for a sending domain, broken down by inbox provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**[EmailProviderMetrics]**](EmailProviderMetrics.md) | One entry per inbox provider that received email from the domain during the reporting window. Empty when the domain is not found for the app or is not currently active for sending. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


