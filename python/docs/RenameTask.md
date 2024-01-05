# RenameTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**RenameParams**](RenameParams.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the rename task. | [optional] [default to 'rename']

## Example

```python
from graalsystems.models.rename_task import RenameTask

# TODO update the JSON string below
json = "{}"
# create an instance of RenameTask from a JSON string
rename_task_instance = RenameTask.from_json(json)
# print the JSON string representation of the object
print RenameTask.to_json()

# convert the object into a dict
rename_task_dict = rename_task_instance.to_dict()
# create an instance of RenameTask from a dict
rename_task_form_dict = rename_task.from_dict(rename_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


