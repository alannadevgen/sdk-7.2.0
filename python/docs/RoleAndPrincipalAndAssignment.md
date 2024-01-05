# RoleAndPrincipalAndAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role**](Role.md) |  | [optional] 
**assignment** | [**RoleAssignment**](RoleAssignment.md) |  | [optional] 
**principal** | [**Principal**](Principal.md) |  | [optional] 

## Example

```python
from graalsystems.models.role_and_principal_and_assignment import RoleAndPrincipalAndAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAndPrincipalAndAssignment from a JSON string
role_and_principal_and_assignment_instance = RoleAndPrincipalAndAssignment.from_json(json)
# print the JSON string representation of the object
print RoleAndPrincipalAndAssignment.to_json()

# convert the object into a dict
role_and_principal_and_assignment_dict = role_and_principal_and_assignment_instance.to_dict()
# create an instance of RoleAndPrincipalAndAssignment from a dict
role_and_principal_and_assignment_form_dict = role_and_principal_and_assignment.from_dict(role_and_principal_and_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


