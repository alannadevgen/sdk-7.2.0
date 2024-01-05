# CranLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'cran']
**ref** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.cran_library import CranLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of CranLibrary from a JSON string
cran_library_instance = CranLibrary.from_json(json)
# print the JSON string representation of the object
print CranLibrary.to_json()

# convert the object into a dict
cran_library_dict = cran_library_instance.to_dict()
# create an instance of CranLibrary from a dict
cran_library_form_dict = cran_library.from_dict(cran_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


