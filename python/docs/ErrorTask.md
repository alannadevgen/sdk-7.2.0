# ErrorTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'error']

## Example

```python
from graalsystems.models.error_task import ErrorTask

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTask from a JSON string
error_task_instance = ErrorTask.from_json(json)
# print the JSON string representation of the object
print ErrorTask.to_json()

# convert the object into a dict
error_task_dict = error_task_instance.to_dict()
# create an instance of ErrorTask from a dict
error_task_form_dict = error_task.from_dict(error_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


