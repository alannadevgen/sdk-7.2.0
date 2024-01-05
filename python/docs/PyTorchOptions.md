# PyTorchOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'python']
**module** | **str** |  | [optional] 
**number_replicas** | **float** |  | [optional] 
**master_instance_type** | **str** |  | [optional] 
**worker_instance_type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.py_torch_options import PyTorchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PyTorchOptions from a JSON string
py_torch_options_instance = PyTorchOptions.from_json(json)
# print the JSON string representation of the object
print PyTorchOptions.to_json()

# convert the object into a dict
py_torch_options_dict = py_torch_options_instance.to_dict()
# create an instance of PyTorchOptions from a dict
py_torch_options_form_dict = py_torch_options.from_dict(py_torch_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


