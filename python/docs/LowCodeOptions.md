# LowCodeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'lowcode']
**mode** | **str** |  | [optional] 
**executor_instance_type** | **str** |  | [optional] 
**number_executors** | **float** |  | [optional] 
**definition** | **object** |  | [optional] 

## Example

```python
from graalsystems.models.low_code_options import LowCodeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LowCodeOptions from a JSON string
low_code_options_instance = LowCodeOptions.from_json(json)
# print the JSON string representation of the object
print LowCodeOptions.to_json()

# convert the object into a dict
low_code_options_dict = low_code_options_instance.to_dict()
# create an instance of LowCodeOptions from a dict
low_code_options_form_dict = low_code_options.from_dict(low_code_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


