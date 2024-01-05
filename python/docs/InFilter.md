# InFilter

Filter values that are in a list or a string.  Attributes ---------- type : RelationalOperatorType     Type of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | [**Right**](Right.md) |  | 
**type** | **str** | Operator for IN list/range filter. | [optional] [default to 'in']

## Example

```python
from graalsystems.models.in_filter import InFilter

# TODO update the JSON string below
json = "{}"
# create an instance of InFilter from a JSON string
in_filter_instance = InFilter.from_json(json)
# print the JSON string representation of the object
print InFilter.to_json()

# convert the object into a dict
in_filter_dict = in_filter_instance.to_dict()
# create an instance of InFilter from a dict
in_filter_form_dict = in_filter.from_dict(in_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


