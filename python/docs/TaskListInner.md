# TaskListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**PrintParams**](PrintParams.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the aggregation task. | [optional] [default to 'aggregation']

## Example

```python
from graalsystems.models.task_list_inner import TaskListInner

# TODO update the JSON string below
json = "{}"
# create an instance of TaskListInner from a JSON string
task_list_inner_instance = TaskListInner.from_json(json)
# print the JSON string representation of the object
print TaskListInner.to_json()

# convert the object into a dict
task_list_inner_dict = task_list_inner_instance.to_dict()
# create an instance of TaskListInner from a dict
task_list_inner_form_dict = task_list_inner.from_dict(task_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


