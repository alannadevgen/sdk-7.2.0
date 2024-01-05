# NotEqualFilter

Filter values that are not equal to a given value.  Attributes ---------- type : RelationalOperatorType     Type of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **str** | Right operator for filter. | 
**type** | **str** | Operator for NOT EQUAL filter. | [optional] [default to 'not_equal']

## Example

```python
from graalsystems.models.not_equal_filter import NotEqualFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NotEqualFilter from a JSON string
not_equal_filter_instance = NotEqualFilter.from_json(json)
# print the JSON string representation of the object
print NotEqualFilter.to_json()

# convert the object into a dict
not_equal_filter_dict = not_equal_filter_instance.to_dict()
# create an instance of NotEqualFilter from a dict
not_equal_filter_form_dict = not_equal_filter.from_dict(not_equal_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


