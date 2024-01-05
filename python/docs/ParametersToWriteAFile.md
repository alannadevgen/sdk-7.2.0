# ParametersToWriteAFile

Options for reading a file (header, file path, separator,         delimiter, ...).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Name of the path. | 
**type** | **str** | Define file type for Pickle. | [optional] [default to 'pickle']

## Example

```python
from graalsystems.models.parameters_to_write_a_file import ParametersToWriteAFile

# TODO update the JSON string below
json = "{}"
# create an instance of ParametersToWriteAFile from a JSON string
parameters_to_write_a_file_instance = ParametersToWriteAFile.from_json(json)
# print the JSON string representation of the object
print ParametersToWriteAFile.to_json()

# convert the object into a dict
parameters_to_write_a_file_dict = parameters_to_write_a_file_instance.to_dict()
# create an instance of ParametersToWriteAFile from a dict
parameters_to_write_a_file_form_dict = parameters_to_write_a_file.from_dict(parameters_to_write_a_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


