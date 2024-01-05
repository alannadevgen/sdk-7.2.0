# StartTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'start']

## Example

```python
from graalsystems.models.start_task import StartTask

# TODO update the JSON string below
json = "{}"
# create an instance of StartTask from a JSON string
start_task_instance = StartTask.from_json(json)
# print the JSON string representation of the object
print StartTask.to_json()

# convert the object into a dict
start_task_dict = start_task_instance.to_dict()
# create an instance of StartTask from a dict
start_task_form_dict = start_task.from_dict(start_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


