# EmailReputationWindow

Email reputation rates for a single time window. Each rate is a fraction of successfully delivered emails (for example, `0.02` means 2%). Both rates are `0` when no email was successfully delivered in the window.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounce_rate** | **float** | The fraction of successfully delivered emails that hard or soft bounced during the window. | [optional] 
**complaint_rate** | **float** | The fraction of successfully delivered emails that recipients reported as spam during the window. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


