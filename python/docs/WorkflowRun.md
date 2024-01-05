# WorkflowRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**infrastructure_id** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.workflow_run import WorkflowRun

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRun from a JSON string
workflow_run_instance = WorkflowRun.from_json(json)
# print the JSON string representation of the object
print WorkflowRun.to_json()

# convert the object into a dict
workflow_run_dict = workflow_run_instance.to_dict()
# create an instance of WorkflowRun from a dict
workflow_run_form_dict = workflow_run.from_dict(workflow_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


