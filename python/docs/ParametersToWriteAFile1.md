# ParametersToWriteAFile1

Options for reading a file (header, file path, separator,         delimiter, ...).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to PARQUET file. | 
**separator** | **str** | Delimiter to use between columns. | [optional] 
**header** | **bool** | Is the first row the header? | [optional] 
**delimiter** | **str** | Alias for separator. | [optional] 
**type** | **str** | Define file type for CSV. | [optional] [default to 'csv']

## Example

```python
from graalsystems.models.parameters_to_write_a_file1 import ParametersToWriteAFile1

# TODO update the JSON string below
json = "{}"
# create an instance of ParametersToWriteAFile1 from a JSON string
parameters_to_write_a_file1_instance = ParametersToWriteAFile1.from_json(json)
# print the JSON string representation of the object
print ParametersToWriteAFile1.to_json()

# convert the object into a dict
parameters_to_write_a_file1_dict = parameters_to_write_a_file1_instance.to_dict()
# create an instance of ParametersToWriteAFile1 from a dict
parameters_to_write_a_file1_form_dict = parameters_to_write_a_file1.from_dict(parameters_to_write_a_file1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


