# ChangePage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Change]**](Change.md) |  | [optional] 

## Example

```python
from graalsystems.models.change_page import ChangePage

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePage from a JSON string
change_page_instance = ChangePage.from_json(json)
# print the JSON string representation of the object
print ChangePage.to_json()

# convert the object into a dict
change_page_dict = change_page_instance.to_dict()
# create an instance of ChangePage from a dict
change_page_form_dict = change_page.from_dict(change_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


