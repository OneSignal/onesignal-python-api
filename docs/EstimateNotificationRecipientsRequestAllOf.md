# EstimateNotificationRecipientsRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The OneSignal App ID for your app, which can be found in Keys & IDs. | [optional] 
**filters** | [**[FilterExpression], none_type**](FilterExpression.md) |  | [optional] 
**include_aliases** | [**IncludeAliases**](IncludeAliases.md) |  | [optional] 
**target_channel** | **str** | Which platforms to count recipients for. Selects the same default platforms Create notification would use for the channel. Individual platform flags (`isIos`, `isAndroid`, etc.) are not supported by this endpoint. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


