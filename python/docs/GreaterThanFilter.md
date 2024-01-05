# GreaterThanFilter

Filter values that are greater than a given value.  Attributes ---------- type : RelationalOperatorType     Type of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **str** | Right operator for filter. | 
**type** | **str** | Operator for GREATER THAN filter. | [optional] [default to 'greater']

## Example

```python
from graalsystems.models.greater_than_filter import GreaterThanFilter

# TODO update the JSON string below
json = "{}"
# create an instance of GreaterThanFilter from a JSON string
greater_than_filter_instance = GreaterThanFilter.from_json(json)
# print the JSON string representation of the object
print GreaterThanFilter.to_json()

# convert the object into a dict
greater_than_filter_dict = greater_than_filter_instance.to_dict()
# create an instance of GreaterThanFilter from a dict
greater_than_filter_form_dict = greater_than_filter.from_dict(greater_than_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


