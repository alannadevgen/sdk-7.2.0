# OrFilter

Filter values that verify at least one condition.  Attributes ---------- type : RelationalOperatorType     Type of the filter. conditions : union_filter     Union of all relational filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Operator for OR filter. | [optional] [default to 'or']
**conditions** | [**List[ANDConditionInner]**](ANDConditionInner.md) | Condition for OR filter. | 

## Example

```python
from graalsystems.models.or_filter import OrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OrFilter from a JSON string
or_filter_instance = OrFilter.from_json(json)
# print the JSON string representation of the object
print OrFilter.to_json()

# convert the object into a dict
or_filter_dict = or_filter_instance.to_dict()
# create an instance of OrFilter from a dict
or_filter_form_dict = or_filter.from_dict(or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


