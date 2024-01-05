# DropTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**DropParams**](DropParams.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the drop task. | [optional] [default to 'drop']

## Example

```python
from graalsystems.models.drop_task import DropTask

# TODO update the JSON string below
json = "{}"
# create an instance of DropTask from a JSON string
drop_task_instance = DropTask.from_json(json)
# print the JSON string representation of the object
print DropTask.to_json()

# convert the object into a dict
drop_task_dict = drop_task_instance.to_dict()
# create an instance of DropTask from a dict
drop_task_form_dict = drop_task.from_dict(drop_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


