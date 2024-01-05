# ParquetReader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Define file type for PARQUET. | [optional] [default to 'parquet']
**path** | **str** | Path to PARQUET file. | 

## Example

```python
from graalsystems.models.parquet_reader import ParquetReader

# TODO update the JSON string below
json = "{}"
# create an instance of ParquetReader from a JSON string
parquet_reader_instance = ParquetReader.from_json(json)
# print the JSON string representation of the object
print ParquetReader.to_json()

# convert the object into a dict
parquet_reader_dict = parquet_reader_instance.to_dict()
# create an instance of ParquetReader from a dict
parquet_reader_form_dict = parquet_reader.from_dict(parquet_reader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


