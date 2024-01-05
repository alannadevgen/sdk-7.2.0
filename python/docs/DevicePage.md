# DevicePage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Device]**](Device.md) |  | [optional] 

## Example

```python
from graalsystems.models.device_page import DevicePage

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePage from a JSON string
device_page_instance = DevicePage.from_json(json)
# print the JSON string representation of the object
print DevicePage.to_json()

# convert the object into a dict
device_page_dict = device_page_instance.to_dict()
# create an instance of DevicePage from a dict
device_page_form_dict = device_page.from_dict(device_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


