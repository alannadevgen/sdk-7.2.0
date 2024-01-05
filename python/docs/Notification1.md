# Notification1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**infos** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from graalsystems.models.notification1 import Notification1

# TODO update the JSON string below
json = "{}"
# create an instance of Notification1 from a JSON string
notification1_instance = Notification1.from_json(json)
# print the JSON string representation of the object
print Notification1.to_json()

# convert the object into a dict
notification1_dict = notification1_instance.to_dict()
# create an instance of Notification1 from a dict
notification1_form_dict = notification1.from_dict(notification1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


