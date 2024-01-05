# PythonOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'python']
**module** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.python_options import PythonOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PythonOptions from a JSON string
python_options_instance = PythonOptions.from_json(json)
# print the JSON string representation of the object
print PythonOptions.to_json()

# convert the object into a dict
python_options_dict = python_options_instance.to_dict()
# create an instance of PythonOptions from a dict
python_options_form_dict = python_options.from_dict(python_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


