# WriteTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**params** | [**WriteTaskParameters**](WriteTaskParameters.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the write task. | [optional] [default to 'write']

## Example

```python
from graalsystems.models.write_task import WriteTask

# TODO update the JSON string below
json = "{}"
# create an instance of WriteTask from a JSON string
write_task_instance = WriteTask.from_json(json)
# print the JSON string representation of the object
print WriteTask.to_json()

# convert the object into a dict
write_task_dict = write_task_instance.to_dict()
# create an instance of WriteTask from a dict
write_task_form_dict = write_task.from_dict(write_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


