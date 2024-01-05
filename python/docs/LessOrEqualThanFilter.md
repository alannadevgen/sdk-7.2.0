# LessOrEqualThanFilter

Filter values that are smaller or equal to a given value.  Attributes ---------- type : RelationalOperatorType     Type of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **str** | Right operator for filter. | 
**type** | **str** | Operator for LESS OR EQUAL filter. | [optional] [default to 'less_or_equal']

## Example

```python
from graalsystems.models.less_or_equal_than_filter import LessOrEqualThanFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LessOrEqualThanFilter from a JSON string
less_or_equal_than_filter_instance = LessOrEqualThanFilter.from_json(json)
# print the JSON string representation of the object
print LessOrEqualThanFilter.to_json()

# convert the object into a dict
less_or_equal_than_filter_dict = less_or_equal_than_filter_instance.to_dict()
# create an instance of LessOrEqualThanFilter from a dict
less_or_equal_than_filter_form_dict = less_or_equal_than_filter.from_dict(less_or_equal_than_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


