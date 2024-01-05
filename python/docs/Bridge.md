# Bridge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**configuration** | **Dict[str, str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**locked** | **bool** |  | [optional] 

## Example

```python
from graalsystems.models.bridge import Bridge

# TODO update the JSON string below
json = "{}"
# create an instance of Bridge from a JSON string
bridge_instance = Bridge.from_json(json)
# print the JSON string representation of the object
print Bridge.to_json()

# convert the object into a dict
bridge_dict = bridge_instance.to_dict()
# create an instance of Bridge from a dict
bridge_form_dict = bridge.from_dict(bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


