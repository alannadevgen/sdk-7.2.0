# Infrastructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**target** | [**Target**](Target.md) |  | [optional] 
**allowed_instance_types** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**locked** | **bool** |  | [optional] 

## Example

```python
from graalsystems.models.infrastructure import Infrastructure

# TODO update the JSON string below
json = "{}"
# create an instance of Infrastructure from a JSON string
infrastructure_instance = Infrastructure.from_json(json)
# print the JSON string representation of the object
print Infrastructure.to_json()

# convert the object into a dict
infrastructure_dict = infrastructure_instance.to_dict()
# create an instance of Infrastructure from a dict
infrastructure_form_dict = infrastructure.from_dict(infrastructure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


