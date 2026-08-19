# JourneyEarlyExit

Conditions that remove a user from the journey before it completes. At least one rule must be set under rules. Send null to remove early exit entirely.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**JourneyEarlyExitRules**](JourneyEarlyExitRules.md) |  | [optional] 
**tag_on_early_exit** | **{str: (str,)}** | Tag key-value pairs applied when a user exits early. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


