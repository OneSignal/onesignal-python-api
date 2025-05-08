# Filter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Required. Name of the field to use as the first operand in the filter expression. | [optional] 
**key** | **str** | If `field` is `tag`, this field is *required* to specify `key` inside the tags. | [optional] 
**value** | **str** | Constant value to use as the second operand in the filter expression. This value is *required* when the relation operator is a binary operator. | [optional] 
**hours_ago** | **str** | If `field` is session-related, this is *required* to specify the number of hours before or after the user's session. | [optional] 
**radius** | **float** | If `field` is `location`, this will specify the radius in meters from a provided location point. Use with `lat` and `long`. | [optional] 
**lat** | **float** | If `field` is `location`, this is *required* to specify the user's latitude. | [optional] 
**long** | **float** | If `field` is `location`, this is *required* to specify the user's longitude. | [optional] 
**relation** | **str** | Required. Operator of a filter expression. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


