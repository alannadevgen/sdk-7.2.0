# MavenLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'maven']
**repo** | **str** |  | [optional] 
**dependency** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.maven_library import MavenLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of MavenLibrary from a JSON string
maven_library_instance = MavenLibrary.from_json(json)
# print the JSON string representation of the object
print MavenLibrary.to_json()

# convert the object into a dict
maven_library_dict = maven_library_instance.to_dict()
# create an instance of MavenLibrary from a dict
maven_library_form_dict = maven_library.from_dict(maven_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


