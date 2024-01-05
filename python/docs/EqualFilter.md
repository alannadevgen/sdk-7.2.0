# EqualFilter

Filter values that are exactly equal to a given value.  Attributes ---------- type : RelationalOperatorType     Type of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **str** | Right operator for filter. | 
**type** | **str** | Operator for EQUAL filter. | [optional] [default to 'equal']

## Example

```python
from graalsystems.models.equal_filter import EqualFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EqualFilter from a JSON string
equal_filter_instance = EqualFilter.from_json(json)
# print the JSON string representation of the object
print EqualFilter.to_json()

# convert the object into a dict
equal_filter_dict = equal_filter_instance.to_dict()
# create an instance of EqualFilter from a dict
equal_filter_form_dict = equal_filter.from_dict(equal_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


