# RoleAndAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role**](Role.md) |  | [optional] 
**assignment** | [**RoleAssignment**](RoleAssignment.md) |  | [optional] 

## Example

```python
from graalsystems.models.role_and_assignment import RoleAndAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAndAssignment from a JSON string
role_and_assignment_instance = RoleAndAssignment.from_json(json)
# print the JSON string representation of the object
print RoleAndAssignment.to_json()

# convert the object into a dict
role_and_assignment_dict = role_and_assignment_instance.to_dict()
# create an instance of RoleAndAssignment from a dict
role_and_assignment_form_dict = role_and_assignment.from_dict(role_and_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


