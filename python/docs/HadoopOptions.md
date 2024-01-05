# HadoopOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'hadoop']
**application_type** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**job_id** | **str** |  | [optional] 
**command** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.hadoop_options import HadoopOptions

# TODO update the JSON string below
json = "{}"
# create an instance of HadoopOptions from a JSON string
hadoop_options_instance = HadoopOptions.from_json(json)
# print the JSON string representation of the object
print HadoopOptions.to_json()

# convert the object into a dict
hadoop_options_dict = hadoop_options_instance.to_dict()
# create an instance of HadoopOptions from a dict
hadoop_options_form_dict = hadoop_options.from_dict(hadoop_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


