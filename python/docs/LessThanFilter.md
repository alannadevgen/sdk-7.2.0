# LessThanFilter

Filter values that are smaller than a given value.  Attributes ---------- type : RelationalOperatorType     Type of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **str** | Right operator for filter. | 
**type** | **str** | Operator for LESS THAN filter. | [optional] [default to 'less']

## Example

```python
from graalsystems.models.less_than_filter import LessThanFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LessThanFilter from a JSON string
less_than_filter_instance = LessThanFilter.from_json(json)
# print the JSON string representation of the object
print LessThanFilter.to_json()

# convert the object into a dict
less_than_filter_dict = less_than_filter_instance.to_dict()
# create an instance of LessThanFilter from a dict
less_than_filter_form_dict = less_than_filter.from_dict(less_than_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


