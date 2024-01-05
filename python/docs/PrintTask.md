# PrintTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**PrintParams**](PrintParams.md) |  | [optional] 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the printtask. | [optional] [default to 'print']

## Example

```python
from graalsystems.models.print_task import PrintTask

# TODO update the JSON string below
json = "{}"
# create an instance of PrintTask from a JSON string
print_task_instance = PrintTask.from_json(json)
# print the JSON string representation of the object
print PrintTask.to_json()

# convert the object into a dict
print_task_dict = print_task_instance.to_dict()
# create an instance of PrintTask from a dict
print_task_form_dict = print_task.from_dict(print_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


