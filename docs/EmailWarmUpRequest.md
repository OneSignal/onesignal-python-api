# EmailWarmUpRequest

Channel: Email Required when `kind` is \"warmup\". The gradual sending schedule for the Auto Warm Up campaign.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stages** | [**[EmailWarmUpStage]**](EmailWarmUpStage.md) | Required. The ordered stages that make up the campaign's sending schedule. | 
**strategy** | **str, none_type** | How the stage schedule should be treated:   * `recommended` - (Default) OneSignal may adjust the provided stages based on past delivery volumes, scheduled Auto Warm Up emails, and the size of the current audience.   * `custom` - The stages provided are sent as-is.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


