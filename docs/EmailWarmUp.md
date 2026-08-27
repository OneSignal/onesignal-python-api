# EmailWarmUp

Channel: Email Present only when this notification's `kind` is \"warmup\". The Auto Warm Up campaign's stage schedule, scheduling strategy, and live status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stages** | [**[EmailWarmUpStage]**](EmailWarmUpStage.md) | The campaign's sending schedule, stage by stage. | [optional] 
**strategy** | **str** | How the stage schedule was produced:   * `recommended` - OneSignal generated (and may still adjust) the schedule based on past delivery volumes, scheduled Auto Warm Up emails, and the size of the current audience.   * `custom` - The stages were provided as-is in the create request.  | [optional] 
**status** | **str** | Current status of the campaign:   * `initializing` - The stages have been submitted and the schedule is being set up.   * `draft` - The campaign has been created but has not started sending.   * `active` - The campaign is currently working through its stages.   * `finished` - All stages have completed.   * `canceled` - The campaign was canceled before finishing.  | [optional] 
**is_live** | **bool** | Whether the campaign is currently live (actively sending). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


