# CsvWriter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**separator** | **str** | Delimiter to use between columns. | [optional] 
**header** | **bool** | Is the first row the header? | [optional] 
**delimiter** | **str** | Alias for separator. | [optional] 
**compression** | **str** | Type of on-the-fly decompression to use. | [optional] 
**index** | **bool** | Is the first column an index? | [optional] 
**path** | **str** | Path to CSV file. | 
**type** | **str** | Define file type for CSV. | [optional] [default to 'csv']

## Example

```python
from graalsystems.models.csv_writer import CsvWriter

# TODO update the JSON string below
json = "{}"
# create an instance of CsvWriter from a JSON string
csv_writer_instance = CsvWriter.from_json(json)
# print the JSON string representation of the object
print CsvWriter.to_json()

# convert the object into a dict
csv_writer_dict = csv_writer_instance.to_dict()
# create an instance of CsvWriter from a dict
csv_writer_form_dict = csv_writer.from_dict(csv_writer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


