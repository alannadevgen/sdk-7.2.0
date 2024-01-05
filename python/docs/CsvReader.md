# CsvReader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to CSV file. | 
**separator** | **str** | Delimiter to use between columns. | [optional] 
**header** | **bool** | Is the first row the header? | [optional] 
**delimiter** | **str** | Alias for separator. | [optional] 
**type** | **str** | Define file type for CSV. | [optional] [default to 'csv']

## Example

```python
from graalsystems.models.csv_reader import CsvReader

# TODO update the JSON string below
json = "{}"
# create an instance of CsvReader from a JSON string
csv_reader_instance = CsvReader.from_json(json)
# print the JSON string representation of the object
print CsvReader.to_json()

# convert the object into a dict
csv_reader_dict = csv_reader_instance.to_dict()
# create an instance of CsvReader from a dict
csv_reader_form_dict = csv_reader.from_dict(csv_reader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


