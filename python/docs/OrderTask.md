# OrderTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**OrderParams**](OrderParams.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the order task. | [optional] [default to 'order']

## Example

```python
from graalsystems.models.order_task import OrderTask

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTask from a JSON string
order_task_instance = OrderTask.from_json(json)
# print the JSON string representation of the object
print OrderTask.to_json()

# convert the object into a dict
order_task_dict = order_task_instance.to_dict()
# create an instance of OrderTask from a dict
order_task_form_dict = order_task.from_dict(order_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


