# FilterExpressions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | If `field` is `tag`, this field is *required* to specify `key` inside the tags. | [optional] 
**value** | **str** | Constant value to use as the second operand in the filter expression.  This value is *required* when the relation operator is a binary operator. | [optional] 
**operator** | **str** | Strictly, this must be either `\"OR\"`, or `\"AND\"`.  It can be used to compose Filters as part of a Filters object. | [optional] 
**field** | **str** | Name of the field to use as the first operand in the filter expression. | [optional] 
**relation** | **str** | Operator of a filter expression. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


