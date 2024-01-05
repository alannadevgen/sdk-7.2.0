# WorkflowTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'workflow']
**ref** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.workflow_task import WorkflowTask

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTask from a JSON string
workflow_task_instance = WorkflowTask.from_json(json)
# print the JSON string representation of the object
print WorkflowTask.to_json()

# convert the object into a dict
workflow_task_dict = workflow_task_instance.to_dict()
# create an instance of WorkflowTask from a dict
workflow_task_form_dict = workflow_task.from_dict(workflow_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


