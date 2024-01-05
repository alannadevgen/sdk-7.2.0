# AndFilter

Filter values that verify all conditions.  Attributes ---------- type : RelationalOperatorType     Type of the filter. conditions : union_filter     Union of all relational filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Operator for AND filter. | [optional] [default to 'and']
**conditions** | [**List[ANDConditionInner]**](ANDConditionInner.md) | Condition for AND filter. | 

## Example

```python
from graalsystems.models.and_filter import AndFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AndFilter from a JSON string
and_filter_instance = AndFilter.from_json(json)
# print the JSON string representation of the object
print AndFilter.to_json()

# convert the object into a dict
and_filter_dict = and_filter_instance.to_dict()
# create an instance of AndFilter from a dict
and_filter_form_dict = and_filter.from_dict(and_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


