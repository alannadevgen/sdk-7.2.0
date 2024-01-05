# FlinkOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'flink']
**main_library** | [**Library**](Library.md) |  | [optional] 
**main_class_name** | **str** |  | [optional] 
**loggers** | **List[str]** |  | [optional] 
**job_manager_instance_type** | **str** |  | [optional] 
**task_manager_instance_type** | **str** |  | [optional] 
**number_task_managers** | **float** |  | [optional] 

## Example

```python
from graalsystems.models.flink_options import FlinkOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FlinkOptions from a JSON string
flink_options_instance = FlinkOptions.from_json(json)
# print the JSON string representation of the object
print FlinkOptions.to_json()

# convert the object into a dict
flink_options_dict = flink_options_instance.to_dict()
# create an instance of FlinkOptions from a dict
flink_options_form_dict = flink_options.from_dict(flink_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


