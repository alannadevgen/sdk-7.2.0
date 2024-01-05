# Workflow1

Object Workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | [optional] [default to 'workflow']
**parent** | [**Project1**](Project1.md) |  | [optional] 

## Example

```python
from graalsystems.models.workflow1 import Workflow1

# TODO update the JSON string below
json = "{}"
# create an instance of Workflow1 from a JSON string
workflow1_instance = Workflow1.from_json(json)
# print the JSON string representation of the object
print Workflow1.to_json()

# convert the object into a dict
workflow1_dict = workflow1_instance.to_dict()
# create an instance of Workflow1 from a dict
workflow1_form_dict = workflow1.from_dict(workflow1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


