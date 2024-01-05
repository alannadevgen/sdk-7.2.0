# FileOrDirectory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**metadata** | [**BlobMetadata**](BlobMetadata.md) |  | [optional] 

## Example

```python
from graalsystems.models.file_or_directory import FileOrDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of FileOrDirectory from a JSON string
file_or_directory_instance = FileOrDirectory.from_json(json)
# print the JSON string representation of the object
print FileOrDirectory.to_json()

# convert the object into a dict
file_or_directory_dict = file_or_directory_instance.to_dict()
# create an instance of FileOrDirectory from a dict
file_or_directory_form_dict = file_or_directory.from_dict(file_or_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


