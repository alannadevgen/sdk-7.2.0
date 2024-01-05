# DistinctTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**DistinctParams**](DistinctParams.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the distinct task. | [optional] [default to 'distinct']

## Example

```python
from graalsystems.models.distinct_task import DistinctTask

# TODO update the JSON string below
json = "{}"
# create an instance of DistinctTask from a JSON string
distinct_task_instance = DistinctTask.from_json(json)
# print the JSON string representation of the object
print DistinctTask.to_json()

# convert the object into a dict
distinct_task_dict = distinct_task_instance.to_dict()
# create an instance of DistinctTask from a dict
distinct_task_form_dict = distinct_task.from_dict(distinct_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


