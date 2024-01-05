# RoleAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**principal_type** | **str** |  | [optional] 
**principal_id** | **str** |  | [optional] 
**role_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.role_assignment import RoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignment from a JSON string
role_assignment_instance = RoleAssignment.from_json(json)
# print the JSON string representation of the object
print RoleAssignment.to_json()

# convert the object into a dict
role_assignment_dict = role_assignment_instance.to_dict()
# create an instance of RoleAssignment from a dict
role_assignment_form_dict = role_assignment.from_dict(role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


