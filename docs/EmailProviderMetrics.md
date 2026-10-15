# EmailProviderMetrics

Email metrics for a single inbox provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The inbox provider. Known values include `apple`, `att`, `canadian`, `chinese`, `comcast`, `free_fr`, `french`, `german`, `gmail`, `google_workspace`, `googlers`, `inbox_lv`, `italian`, `japanese`, `outlook_365`, `outlook_eu`, `outlook_us`, `proton`, `rackspace`, `russian`, `uk`, `united_online`, `yahoo_eu`, `yahoo_us`, `other_eu`, `other_us`, and `other`. New providers may be added over time. | [optional] 
**metrics** | [**EmailMetrics**](EmailMetrics.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


