# AggTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**AggParams**](AggParams.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the aggregation task. | [optional] [default to 'aggregation']

## Example

```python
from graalsystems.models.agg_task import AggTask

# TODO update the JSON string below
json = "{}"
# create an instance of AggTask from a JSON string
agg_task_instance = AggTask.from_json(json)
# print the JSON string representation of the object
print AggTask.to_json()

# convert the object into a dict
agg_task_dict = agg_task_instance.to_dict()
# create an instance of AggTask from a dict
agg_task_form_dict = agg_task.from_dict(agg_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


