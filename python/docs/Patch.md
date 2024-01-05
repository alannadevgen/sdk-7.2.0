# Patch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from graalsystems.models.patch import Patch

# TODO update the JSON string below
json = "{}"
# create an instance of Patch from a JSON string
patch_instance = Patch.from_json(json)
# print the JSON string representation of the object
print Patch.to_json()

# convert the object into a dict
patch_dict = patch_instance.to_dict()
# create an instance of Patch from a dict
patch_form_dict = patch.from_dict(patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


