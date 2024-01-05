# RayOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'ray']
**package_name** | **str** |  | [optional] 
**module_name** | **str** |  | [optional] 
**function_name** | **str** |  | [optional] 
**number_workers** | **float** |  | [optional] 
**number_workers_max** | **float** |  | [optional] 
**driver_instance_type** | **str** |  | [optional] 
**worker_instance_type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.ray_options import RayOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RayOptions from a JSON string
ray_options_instance = RayOptions.from_json(json)
# print the JSON string representation of the object
print RayOptions.to_json()

# convert the object into a dict
ray_options_dict = ray_options_instance.to_dict()
# create an instance of RayOptions from a dict
ray_options_form_dict = ray_options.from_dict(ray_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


