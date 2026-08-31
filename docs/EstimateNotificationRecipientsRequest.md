# EstimateNotificationRecipientsRequest

The targeting subset of notification fields this endpoint honors. `included_segments` (or its `\"All\"` shorthand) is required. `excluded_segments`, `filters`, `include_aliases`, and `target_channel` narrow that segment-based audience further when present. Use `target_channel` to select which platforms to count. Other notification targeting fields (`include_subscription_ids` and the other raw subscription id/token fields, and the individual `isIos` / `isAndroid` / etc. platform flags) are not read by this endpoint. All non-targeting notification fields (content, delivery options, and so on) are accepted, but ignored. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The OneSignal App ID for your app, which can be found in Keys & IDs. | 
**included_segments** | **[str]** | The segment names you want to target. Users in these segments will receive a notification. This targeting parameter is only compatible with excluded_segments. Example: [\"Active Users\", \"Inactive Users\"] `\"All\"` is a shorthand for every subscribed user: if the array includes the string `\"All\"` and the app has no segment actually named `All`, it targets all subscribers instead of a literal segment lookup.  | [optional] 
**excluded_segments** | **[str]** | Segment that will be excluded when sending. Users in these segments will not receive a notification, even if they were included in included_segments. This targeting parameter is only compatible with included_segments. Example: [\"Active Users\", \"Inactive Users\"]  | [optional] 
**filters** | [**[FilterExpression], none_type**](FilterExpression.md) |  | [optional] 
**include_aliases** | [**IncludeAliases**](IncludeAliases.md) |  | [optional] 
**target_channel** | **str** | Which platforms to count recipients for. Selects the same default platforms Create notification would use for the channel. Individual platform flags (`isIos`, `isAndroid`, etc.) are not supported by this endpoint. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


