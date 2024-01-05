# ReadTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**params** | [**ReadTaskParameters**](ReadTaskParameters.md) |  | 
**type** | **str** | Type of the read task. | [optional] [default to 'read']
**dependency** | **List[str]** | List of all dependencies of the task (optional). | [optional] [default to []]

## Example

```python
from graalsystems.models.read_task import ReadTask

# TODO update the JSON string below
json = "{}"
# create an instance of ReadTask from a JSON string
read_task_instance = ReadTask.from_json(json)
# print the JSON string representation of the object
print ReadTask.to_json()

# convert the object into a dict
read_task_dict = read_task_instance.to_dict()
# create an instance of ReadTask from a dict
read_task_form_dict = read_task.from_dict(read_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


