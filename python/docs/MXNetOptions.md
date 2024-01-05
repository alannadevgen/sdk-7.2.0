# MXNetOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'mxnet']
**module** | **str** |  | [optional] 
**number_replicas** | **float** |  | [optional] 
**server_instance_type** | **str** |  | [optional] 
**worker_instance_type** | **str** |  | [optional] 
**scheduler_instance_type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.mx_net_options import MXNetOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MXNetOptions from a JSON string
mx_net_options_instance = MXNetOptions.from_json(json)
# print the JSON string representation of the object
print MXNetOptions.to_json()

# convert the object into a dict
mx_net_options_dict = mx_net_options_instance.to_dict()
# create an instance of MXNetOptions from a dict
mx_net_options_form_dict = mx_net_options.from_dict(mx_net_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


