# NotNullFilter

Filter values that are not null.  Attributes ---------- type : RelationalOperatorType     Type of the filter. right : str     Optional value for right side of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **str** |  | [optional] 
**type** | **str** | Operator for NOT NULL filter. | [optional] [default to 'not_null']

## Example

```python
from graalsystems.models.not_null_filter import NotNullFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NotNullFilter from a JSON string
not_null_filter_instance = NotNullFilter.from_json(json)
# print the JSON string representation of the object
print NotNullFilter.to_json()

# convert the object into a dict
not_null_filter_dict = not_null_filter_instance.to_dict()
# create an instance of NotNullFilter from a dict
not_null_filter_form_dict = not_null_filter.from_dict(not_null_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


