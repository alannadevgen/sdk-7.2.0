# PredictModelTask

Defines a task in a DAG.  Attributes ---------- id : str     Identifier of a task. params : Params     Parameters of a task.  Methods ------- accept(visitor)     Visit a task using a specified visitor. to_node()     Returns the information about the task (id and parameters). to_edge()     Gets all the dependencies of the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the task. | 
**params** | **object** |  | 
**dependency** | **List[str]** | List of all dependencies of the task. | 
**type** | **str** | Type of the predict model task. | [optional] [default to 'predict_model']

## Example

```python
from graalsystems.models.predict_model_task import PredictModelTask

# TODO update the JSON string below
json = "{}"
# create an instance of PredictModelTask from a JSON string
predict_model_task_instance = PredictModelTask.from_json(json)
# print the JSON string representation of the object
print PredictModelTask.to_json()

# convert the object into a dict
predict_model_task_dict = predict_model_task_instance.to_dict()
# create an instance of PredictModelTask from a dict
predict_model_task_form_dict = predict_model_task.from_dict(predict_model_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


