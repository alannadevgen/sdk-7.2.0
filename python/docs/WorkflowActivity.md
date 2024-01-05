# WorkflowActivity

Object JobActivity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**reaction_count** | [**List[Reaction]**](Reaction.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'workflow']
**actor** | [**User1**](User1.md) |  | 
**target** | [**Workflow1**](Workflow1.md) |  | 
**verb** | **str** |  | 

## Example

```python
from graalsystems.models.workflow_activity import WorkflowActivity

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowActivity from a JSON string
workflow_activity_instance = WorkflowActivity.from_json(json)
# print the JSON string representation of the object
print WorkflowActivity.to_json()

# convert the object into a dict
workflow_activity_dict = workflow_activity_instance.to_dict()
# create an instance of WorkflowActivity from a dict
workflow_activity_form_dict = workflow_activity.from_dict(workflow_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


