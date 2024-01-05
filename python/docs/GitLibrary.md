# GitLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'git']
**url** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.git_library import GitLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of GitLibrary from a JSON string
git_library_instance = GitLibrary.from_json(json)
# print the JSON string representation of the object
print GitLibrary.to_json()

# convert the object into a dict
git_library_dict = git_library_instance.to_dict()
# create an instance of GitLibrary from a dict
git_library_form_dict = git_library.from_dict(git_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


