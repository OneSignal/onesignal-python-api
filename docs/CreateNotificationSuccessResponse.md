# CreateNotificationSuccessResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Notification identifier when the request created a notification. An empty string means no notification was created; read `errors` for details (HTTP may still be 200). | [optional] 
**external_id** | **str, none_type** | Optional correlation / idempotency-related value from the API response. This is not the end-user External ID used for targeting recipients (that lives under `include_aliases.external_id`). | [optional] 
**errors** | **bool, date, datetime, dict, float, int, list, str, none_type** | Polymorphic field: may be an array of human-readable strings and/or an object (for example with `invalid_aliases`, `invalid_external_user_ids`, or `invalid_player_ids`) depending on the API response; HTTP may still be 200 with partial success. Typed SDKs model this loosely so both shapes deserialize. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


