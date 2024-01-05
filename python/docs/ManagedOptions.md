# ManagedOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | **Dict[str, str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.managed_options import ManagedOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedOptions from a JSON string
managed_options_instance = ManagedOptions.from_json(json)
# print the JSON string representation of the object
print ManagedOptions.to_json()

# convert the object into a dict
managed_options_dict = managed_options_instance.to_dict()
# create an instance of ManagedOptions from a dict
managed_options_form_dict = managed_options.from_dict(managed_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


