# FileLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'file']
**key** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.file_library import FileLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of FileLibrary from a JSON string
file_library_instance = FileLibrary.from_json(json)
# print the JSON string representation of the object
print FileLibrary.to_json()

# convert the object into a dict
file_library_dict = file_library_instance.to_dict()
# create an instance of FileLibrary from a dict
file_library_form_dict = file_library.from_dict(file_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


