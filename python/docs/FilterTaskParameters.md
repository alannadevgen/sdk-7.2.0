# FilterTaskParameters

Parameters of the filter task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Left operator for filter. | 
**right** | [**Right**](Right.md) |  | 
**type** | **str** | Operator for GREATER OR EQUAL filter. | [optional] [default to 'greater_or_equal']
**condition** | **str** |  | 
**conditions** | [**List[ANDConditionInner]**](ANDConditionInner.md) | Condition for OR filter. | 

## Example

```python
from graalsystems.models.filter_task_parameters import FilterTaskParameters

# TODO update the JSON string below
json = "{}"
# create an instance of FilterTaskParameters from a JSON string
filter_task_parameters_instance = FilterTaskParameters.from_json(json)
# print the JSON string representation of the object
print FilterTaskParameters.to_json()

# convert the object into a dict
filter_task_parameters_dict = filter_task_parameters_instance.to_dict()
# create an instance of FilterTaskParameters from a dict
filter_task_parameters_form_dict = filter_task_parameters.from_dict(filter_task_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


