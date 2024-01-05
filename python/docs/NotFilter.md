# NotFilter

Filter values that are not equal to a given value.  Attributes ---------- type : RelationalOperatorType     Type of the filter. condition : union_filter     Union of all relational filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Operator for NOT filter. | [optional] [default to 'not']
**condition** | **str** |  | 

## Example

```python
from graalsystems.models.not_filter import NotFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NotFilter from a JSON string
not_filter_instance = NotFilter.from_json(json)
# print the JSON string representation of the object
print NotFilter.to_json()

# convert the object into a dict
not_filter_dict = not_filter_instance.to_dict()
# create an instance of NotFilter from a dict
not_filter_form_dict = not_filter.from_dict(not_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


