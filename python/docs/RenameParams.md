# RenameParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | Name of the column to rename. | 
**new_name** | **str** | Replacement name for the column. | 

## Example

```python
from graalsystems.models.rename_params import RenameParams

# TODO update the JSON string below
json = "{}"
# create an instance of RenameParams from a JSON string
rename_params_instance = RenameParams.from_json(json)
# print the JSON string representation of the object
print RenameParams.to_json()

# convert the object into a dict
rename_params_dict = rename_params_instance.to_dict()
# create an instance of RenameParams from a dict
rename_params_form_dict = rename_params.from_dict(rename_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


