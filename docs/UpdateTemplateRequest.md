# UpdateTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated name of the template. | [optional] 
**contents** | [**LanguageStringMap**](LanguageStringMap.md) |  | [optional] 
**is_email** | **bool** | Set true for an Email template. | [optional] 
**email_subject** | **str, none_type** | Subject of the email. | [optional] 
**email_body** | **str, none_type** | Body of the email (HTML supported). | [optional] 
**is_sms** | **bool** | Set true for an SMS template. | [optional] 
**dynamic_content** | **str, none_type** | JSON string for dynamic content personalization. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


