# InstanceType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**generation** | **float** |  | [optional] 
**family** | **str** |  | [optional] 
**cpus** | **float** |  | [optional] 
**memory** | **str** |  | [optional] 
**storage** | **str** |  | [optional] 
**gpus** | **float** |  | [optional] 
**gpu_memory** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.instance_type import InstanceType

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceType from a JSON string
instance_type_instance = InstanceType.from_json(json)
# print the JSON string representation of the object
print InstanceType.to_json()

# convert the object into a dict
instance_type_dict = instance_type_instance.to_dict()
# create an instance of InstanceType from a dict
instance_type_form_dict = instance_type.from_dict(instance_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


