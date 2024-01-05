# GreaterOrEqualThanFilter

Filter values that are greater or equal to a given value.  Attributes ---------- type : RelationalOperatorType     Type of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **str** | Right operator for filter. | 
**type** | **str** | Operator for GREATER OR EQUAL filter. | [optional] [default to 'greater_or_equal']

## Example

```python
from graalsystems.models.greater_or_equal_than_filter import GreaterOrEqualThanFilter

# TODO update the JSON string below
json = "{}"
# create an instance of GreaterOrEqualThanFilter from a JSON string
greater_or_equal_than_filter_instance = GreaterOrEqualThanFilter.from_json(json)
# print the JSON string representation of the object
print GreaterOrEqualThanFilter.to_json()

# convert the object into a dict
greater_or_equal_than_filter_dict = greater_or_equal_than_filter_instance.to_dict()
# create an instance of GreaterOrEqualThanFilter from a dict
greater_or_equal_than_filter_form_dict = greater_or_equal_than_filter.from_dict(greater_or_equal_than_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


