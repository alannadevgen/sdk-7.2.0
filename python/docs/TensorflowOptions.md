# TensorflowOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'tensorflow']
**number_replicas** | **float** |  | [optional] 
**module** | **str** |  | [optional] 
**replica_instance_type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.tensorflow_options import TensorflowOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TensorflowOptions from a JSON string
tensorflow_options_instance = TensorflowOptions.from_json(json)
# print the JSON string representation of the object
print TensorflowOptions.to_json()

# convert the object into a dict
tensorflow_options_dict = tensorflow_options_instance.to_dict()
# create an instance of TensorflowOptions from a dict
tensorflow_options_form_dict = tensorflow_options.from_dict(tensorflow_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


