# FilterTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**FilterTaskParameters**](FilterTaskParameters.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the filter task. | [optional] [default to 'filter']

## Example

```python
from graalsystems.models.filter_task import FilterTask

# TODO update the JSON string below
json = "{}"
# create an instance of FilterTask from a JSON string
filter_task_instance = FilterTask.from_json(json)
# print the JSON string representation of the object
print FilterTask.to_json()

# convert the object into a dict
filter_task_dict = filter_task_instance.to_dict()
# create an instance of FilterTask from a dict
filter_task_form_dict = filter_task.from_dict(filter_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


