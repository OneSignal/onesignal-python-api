# StartLiveActivityRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An internal name to assist with your campaign organization. This does not get displayed in the message itself. | 
**activity_id** | **str** | Set a unique activity_id to track and manage the Live Activity. | 
**event_attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Default/static data to initialize the Live Activity upon start. | 
**event_updates** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Dynamic content used to update the running Live Activity at start. Must match the ContentState interface defined in your app. | 
**contents** | [**LanguageStringMap**](LanguageStringMap.md) |  | 
**headings** | [**LanguageStringMap**](LanguageStringMap.md) |  | 
**event** | **str** |  | defaults to "start"
**stale_date** | **int** | Accepts Unix timestamp in seconds. When time reaches the configured stale date, the system considers the Live Activity out of date, and the ActivityState of the Live Activity changes to ActivityState.stale. | [optional] 
**priority** | **int** | Delivery priority through the push provider (APNs). Pass 10 for higher priority notifications, or 5 for lower priority notifications. Lower priority notifications are sent based on the power considerations of the end user's device. If not set, defaults to 10. | [optional] 
**ios_relevance_score** | **float, none_type** | iOS 15+. A score to indicate how a notification should be displayed when grouped. Use a float between 0-1. | [optional] 
**idempotency_key** | **str, none_type** | Correlation and idempotency key. A request received with this parameter will first look for another notification with the same idempotency key. If one exists, a notification will not be sent, and result of the previous operation will instead be returned. Therefore, if you plan on using this feature, it's important to use a good source of randomness to generate the UUID passed here. This key is only idempotent for 30 days. After 30 days, the notification could be removed from our system and a notification with the same idempotency key will be sent again.   See Idempotent Notification Requests for more details writeOnly: true  | [optional] 
**include_aliases** | [**IncludeAliases**](IncludeAliases.md) |  | [optional] 
**include_subscription_ids** | **[str], none_type** | Specific subscription ids to target. Not compatible with other targeting parameters. | [optional] 
**included_segments** | **[str], none_type** | Segment names to include. Only compatible with excluded_segments. | [optional] 
**excluded_segments** | **[str], none_type** | Segment names to exclude. Only compatible with included_segments. | [optional] 
**filters** | [**[FilterExpression], none_type**](FilterExpression.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


