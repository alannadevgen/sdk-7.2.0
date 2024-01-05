# DaskOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dask']
**package_name** | **str** |  | [optional] 
**module_name** | **str** |  | [optional] 
**function_name** | **str** |  | [optional] 
**number_workers** | **float** |  | [optional] 
**number_workers_max** | **float** |  | [optional] 
**driver_instance_type** | **str** |  | [optional] 
**worker_instance_type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.dask_options import DaskOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DaskOptions from a JSON string
dask_options_instance = DaskOptions.from_json(json)
# print the JSON string representation of the object
print DaskOptions.to_json()

# convert the object into a dict
dask_options_dict = dask_options_instance.to_dict()
# create an instance of DaskOptions from a dict
dask_options_form_dict = dask_options.from_dict(dask_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


