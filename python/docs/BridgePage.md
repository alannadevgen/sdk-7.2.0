# BridgePage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Bridge]**](Bridge.md) |  | [optional] 

## Example

```python
from graalsystems.models.bridge_page import BridgePage

# TODO update the JSON string below
json = "{}"
# create an instance of BridgePage from a JSON string
bridge_page_instance = BridgePage.from_json(json)
# print the JSON string representation of the object
print BridgePage.to_json()

# convert the object into a dict
bridge_page_dict = bridge_page_instance.to_dict()
# create an instance of BridgePage from a dict
bridge_page_form_dict = bridge_page.from_dict(bridge_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


