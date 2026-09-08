# EmailReputationResponse

App-wide email bounce and spam complaint rates, broken out by time window. `last_24_hours`, `last_7_days`, and `last_30_days` each hold the bounce and complaint rates for email delivered in that window.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_24_hours** | [**EmailReputationWindow**](EmailReputationWindow.md) |  | [optional] 
**last_7_days** | [**EmailReputationWindow**](EmailReputationWindow.md) |  | [optional] 
**last_30_days** | [**EmailReputationWindow**](EmailReputationWindow.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


