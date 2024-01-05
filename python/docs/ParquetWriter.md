# ParquetWriter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition_by** | **List[str]** | How to partition the dataset. | [optional] 
**mode** | [**SaveMode**](SaveMode.md) |  | [optional] 
**compression** | **str** | Type of on-the-fly compression to use. | [optional] 
**type** | **str** | Define file type for PARQUET. | [optional] [default to 'parquet']
**path** | **str** | Path to PARQUET file. | 

## Example

```python
from graalsystems.models.parquet_writer import ParquetWriter

# TODO update the JSON string below
json = "{}"
# create an instance of ParquetWriter from a JSON string
parquet_writer_instance = ParquetWriter.from_json(json)
# print the JSON string representation of the object
print ParquetWriter.to_json()

# convert the object into a dict
parquet_writer_dict = parquet_writer_instance.to_dict()
# create an instance of ParquetWriter from a dict
parquet_writer_form_dict = parquet_writer.from_dict(parquet_writer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


