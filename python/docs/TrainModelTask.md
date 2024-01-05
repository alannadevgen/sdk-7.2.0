# TrainModelTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | [**RandomForest**](RandomForest.md) |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the train model task. | [optional] [default to 'train_model']

## Example

```python
from graalsystems.models.train_model_task import TrainModelTask

# TODO update the JSON string below
json = "{}"
# create an instance of TrainModelTask from a JSON string
train_model_task_instance = TrainModelTask.from_json(json)
# print the JSON string representation of the object
print TrainModelTask.to_json()

# convert the object into a dict
train_model_task_dict = train_model_task_instance.to_dict()
# create an instance of TrainModelTask from a dict
train_model_task_form_dict = train_model_task.from_dict(train_model_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


