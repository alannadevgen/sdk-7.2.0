# ScriptTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'script']
**script** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.script_task import ScriptTask

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptTask from a JSON string
script_task_instance = ScriptTask.from_json(json)
# print the JSON string representation of the object
print ScriptTask.to_json()

# convert the object into a dict
script_task_dict = script_task_instance.to_dict()
# create an instance of ScriptTask from a dict
script_task_form_dict = script_task.from_dict(script_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


