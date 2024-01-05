# ParametersToWriteAFile2

Options for reading a file (header, file path, separator,         delimiter, ...).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Name of the path. | 
**type** | **str** | Define file type for Pickle. | [optional] [default to 'pickle']

## Example

```python
from graalsystems.models.parameters_to_write_a_file2 import ParametersToWriteAFile2

# TODO update the JSON string below
json = "{}"
# create an instance of ParametersToWriteAFile2 from a JSON string
parameters_to_write_a_file2_instance = ParametersToWriteAFile2.from_json(json)
# print the JSON string representation of the object
print ParametersToWriteAFile2.to_json()

# convert the object into a dict
parameters_to_write_a_file2_dict = parameters_to_write_a_file2_instance.to_dict()
# create an instance of ParametersToWriteAFile2 from a dict
parameters_to_write_a_file2_form_dict = parameters_to_write_a_file2.from_dict(parameters_to_write_a_file2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


