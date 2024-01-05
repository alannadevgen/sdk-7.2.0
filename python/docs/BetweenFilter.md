# BetweenFilter

Filter values that are in a range/between two values.  Attributes ---------- type : RelationalOperatorType     Type of the filter. right : list     Values below and above.  Methods ------- get_value()     Get the value of the filter operator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **List[str]** |  | 
**type** | **str** | Operator for BETWEEN filter (range). | [optional] [default to 'between']

## Example

```python
from graalsystems.models.between_filter import BetweenFilter

# TODO update the JSON string below
json = "{}"
# create an instance of BetweenFilter from a JSON string
between_filter_instance = BetweenFilter.from_json(json)
# print the JSON string representation of the object
print BetweenFilter.to_json()

# convert the object into a dict
between_filter_dict = between_filter_instance.to_dict()
# create an instance of BetweenFilter from a dict
between_filter_form_dict = between_filter.from_dict(between_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


