# LikeFilter

Filter values that contain a sub-string.  Attributes ---------- type : RelationalOperatorType     Type of the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | **str** | Right operator for filter. | 
**type** | **str** | Operator for LIKE filter. | [optional] [default to 'like']

## Example

```python
from graalsystems.models.like_filter import LikeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LikeFilter from a JSON string
like_filter_instance = LikeFilter.from_json(json)
# print the JSON string representation of the object
print LikeFilter.to_json()

# convert the object into a dict
like_filter_dict = like_filter_instance.to_dict()
# create an instance of LikeFilter from a dict
like_filter_form_dict = like_filter.from_dict(like_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


