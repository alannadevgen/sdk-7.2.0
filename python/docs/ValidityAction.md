# ValidityAction

Validity Request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'verify']
**language** | [**EtlDagSchemasEnumsLanguageType**](EtlDagSchemasEnumsLanguageType.md) |  | [optional] 
**dag** | [**Dag**](Dag.md) |  | 

## Example

```python
from graalsystems.models.validity_action import ValidityAction

# TODO update the JSON string below
json = "{}"
# create an instance of ValidityAction from a JSON string
validity_action_instance = ValidityAction.from_json(json)
# print the JSON string representation of the object
print ValidityAction.to_json()

# convert the object into a dict
validity_action_dict = validity_action_instance.to_dict()
# create an instance of ValidityAction from a dict
validity_action_form_dict = validity_action.from_dict(validity_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


