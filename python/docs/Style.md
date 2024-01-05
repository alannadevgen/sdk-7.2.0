# Style


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.style import Style

# TODO update the JSON string below
json = "{}"
# create an instance of Style from a JSON string
style_instance = Style.from_json(json)
# print the JSON string representation of the object
print Style.to_json()

# convert the object into a dict
style_dict = style_instance.to_dict()
# create an instance of Style from a dict
style_form_dict = style.from_dict(style_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


