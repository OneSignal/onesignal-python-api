# JourneyValidationError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Stable, kebab-case error identifier. Always `invalid-payload` for validation failures. | [optional] 
**title** | **str** | Human-readable message. Wording may change between releases. | [optional] 
**meta** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Structured context. Always includes `attribute` (the field, or `base` for request-level errors); may also include `path`, `node_id`, or `client_node_id`. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](https://github.com/OneSignal/onesignal-python-api#full-api-reference) [[Back to README]](https://github.com/OneSignal/onesignal-python-api)


