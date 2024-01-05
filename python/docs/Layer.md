# Layer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**technical_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.layer import Layer

# TODO update the JSON string below
json = "{}"
# create an instance of Layer from a JSON string
layer_instance = Layer.from_json(json)
# print the JSON string representation of the object
print Layer.to_json()

# convert the object into a dict
layer_dict = layer_instance.to_dict()
# create an instance of Layer from a dict
layer_form_dict = layer.from_dict(layer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


