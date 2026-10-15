# EmailMetrics

Email delivery and engagement counts for the reporting window.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **int** | The number of emails sent. | [optional] 
**delivered** | **int** | The number of emails successfully delivered. | [optional] 
**opened** | **int** | The total number of email opens, including repeat opens by the same recipient. | [optional] 
**clicked** | **int** | The total number of email link clicks, including repeat clicks by the same recipient. | [optional] 
**unique_opened** | **int** | The number of emails opened at least once. | [optional] 
**unique_clicked** | **int** | The number of emails with at least one link click. | [optional] 
**failed** | **int** | The number of emails that failed to send. | [optional] 
**bounced** | **int** | The number of emails that bounced. | [optional] 
**complained** | **int** | The number of emails that recipients reported as spam. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


