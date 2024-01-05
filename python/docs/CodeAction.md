# CodeAction

Code generation Request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'code']
**language** | [**EtlDagSchemasEnumsLanguageType**](EtlDagSchemasEnumsLanguageType.md) |  | 
**dag** | [**Dag**](Dag.md) |  | 

## Example

```python
from graalsystems.models.code_action import CodeAction

# TODO update the JSON string below
json = "{}"
# create an instance of CodeAction from a JSON string
code_action_instance = CodeAction.from_json(json)
# print the JSON string representation of the object
print CodeAction.to_json()

# convert the object into a dict
code_action_dict = code_action_instance.to_dict()
# create an instance of CodeAction from a dict
code_action_form_dict = code_action.from_dict(code_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


