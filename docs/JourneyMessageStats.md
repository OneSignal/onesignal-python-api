# JourneyMessageStats

Delivery stats for a message-sending node. Present only on send_push, send_email, send_sms, send_iam, and send_webhook nodes. The keys inside totals depend on the node's channel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals** | **{str: (float,)}** | All-time totals for this node, keyed by channel-specific stat name. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


