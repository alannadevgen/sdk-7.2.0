# Principal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**remote_identity_id** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**locked** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.principal import Principal

# TODO update the JSON string below
json = "{}"
# create an instance of Principal from a JSON string
principal_instance = Principal.from_json(json)
# print the JSON string representation of the object
print Principal.to_json()

# convert the object into a dict
principal_dict = principal_instance.to_dict()
# create an instance of Principal from a dict
principal_form_dict = principal.from_dict(principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


