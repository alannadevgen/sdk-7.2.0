# JoinTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**JoinParams**](JoinParams.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the join task. | [optional] [default to 'join']

## Example

```python
from graalsystems.models.join_task import JoinTask

# TODO update the JSON string below
json = "{}"
# create an instance of JoinTask from a JSON string
join_task_instance = JoinTask.from_json(json)
# print the JSON string representation of the object
print JoinTask.to_json()

# convert the object into a dict
join_task_dict = join_task_instance.to_dict()
# create an instance of JoinTask from a dict
join_task_form_dict = join_task.from_dict(join_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


