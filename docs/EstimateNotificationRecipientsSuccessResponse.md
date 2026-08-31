# EstimateNotificationRecipientsSuccessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The estimated audience size based on the user targeting method you've set on the message, and the specific platforms the message is targeted to send to. | [optional] 
**uncapped_count** | **int, none_type** | The estimated audience size before the plan's web push subscriber cap is applied. Present only when `cap_applied` is `true`; `null` otherwise. | [optional] 
**cap_applied** | **bool** | Whether `count` was reduced because the app is on a plan that caps the number of web push subscribers it can send to. | [optional] 
**mobile_suppressed** | **bool** | The mobile equivalent of `cap_applied`. Whether mobile push deliveries will be dropped for this send because the org is over its plan's mobile push subscriber cap. `false` when the notification doesn't target any mobile push platforms. | [optional] 
**mobile_excluded_count** | **int** | How many mobile push recipients the `count` excludes due to the plan's mobile push subscriber cap. `0` when `mobile_suppressed` is `false`. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


