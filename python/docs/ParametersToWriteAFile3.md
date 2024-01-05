# ParametersToWriteAFile3

Options for writing a file (header, file path, separator,         delimiter, ...).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**separator** | **str** | Delimiter to use between columns. | [optional] 
**header** | **bool** | Is the first row the header? | [optional] 
**delimiter** | **str** | Alias for separator. | [optional] 
**compression** | **str** | Type of on-the-fly compression to use. | [optional] 
**index** | **bool** | Is the first column an index? | [optional] 
**path** | **str** | Path to PARQUET file. | 
**type** | **str** | Define file type for CSV. | [optional] [default to 'csv']
**partition_by** | **List[str]** | How to partition the dataset. | [optional] 
**mode** | [**SaveMode**](SaveMode.md) |  | [optional] 

## Example

```python
from graalsystems.models.parameters_to_write_a_file3 import ParametersToWriteAFile3

# TODO update the JSON string below
json = "{}"
# create an instance of ParametersToWriteAFile3 from a JSON string
parameters_to_write_a_file3_instance = ParametersToWriteAFile3.from_json(json)
# print the JSON string representation of the object
print ParametersToWriteAFile3.to_json()

# convert the object into a dict
parameters_to_write_a_file3_dict = parameters_to_write_a_file3_instance.to_dict()
# create an instance of ParametersToWriteAFile3 from a dict
parameters_to_write_a_file3_form_dict = parameters_to_write_a_file3.from_dict(parameters_to_write_a_file3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


