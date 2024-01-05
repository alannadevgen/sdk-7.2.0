# RunOnceSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'once']

## Example

```python
from graalsystems.models.run_once_schedule import RunOnceSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of RunOnceSchedule from a JSON string
run_once_schedule_instance = RunOnceSchedule.from_json(json)
# print the JSON string representation of the object
print RunOnceSchedule.to_json()

# convert the object into a dict
run_once_schedule_dict = run_once_schedule_instance.to_dict()
# create an instance of RunOnceSchedule from a dict
run_once_schedule_form_dict = run_once_schedule.from_dict(run_once_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


