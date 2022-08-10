# FilterNotificationTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_session** | **str** | relation = \">\" or \"<\" hours_ago = number of hours before or after the users last session. Example: \"1.1\"  | [optional] 
**first_session** | **str** | relation = \">\" or \"<\" hours_ago = number of hours before or after the users first session. Example: \"1.1\"  | [optional] 
**session_count** | **str** | relation = \">\", \"<\", \"=\" or \"!=\" value = number sessions. Example: \"1\"  | [optional] 
**session_time** | **str** | relation = \">\", \"<\", \"=\" or \"!=\" value = Time in seconds the user has been in your app. Example: \"3600\"  | [optional] 
**amount_spent** | **str** | relation = \">\", \"<\", or \"=\" value = Amount in USD a user has spent on IAP (In App Purchases). Example: \"0.99\"  | [optional] 
**bought_sku** | **str** | relation = \">\", \"<\" or \"=\" key = SKU purchased in your app as an IAP (In App Purchases). Example: \"com.domain.100coinpack\" value = value of SKU to compare to. Example: \"0.99\"  | [optional] 
**tag** | **str** | relation = \">\", \"<\", \"=\", \"!=\", \"exists\", \"not_exists\", \"time_elapsed_gt\" (paid plan only) or \"time_elapsed_lt\" (paid plan only) See Time Operators key = Tag key to compare. value = Tag value to compare. Not required for \"exists\" or \"not_exists\". Example: See Formatting Filters  | [optional] 
**language** | **str** | relation = \"=\" or \"!=\" value = 2 character language code. Example: \"en\". For a list of all language codes see Language & Localization.  | [optional] 
**app_version** | **str** | relation = \">\", \"<\", \"=\" or \"!=\" value = app version. Example: \"1.0.0\"  | [optional] 
**location** | **str** | radius = in meters lat = latitude long = longitude  | [optional] 
**email** | **str** | value = email address Only for sending Push Notifications Use this for targeting push subscribers associated with an email set with all SDK setEmail methods To send emails to specific email addresses use include_email_tokens parameter  | [optional] 
**country** | **str** | relation = \"=\" value = 2-digit Country code Example: \"field\": \"country\", \"relation\": \"=\", \"value\", \"US\"  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


