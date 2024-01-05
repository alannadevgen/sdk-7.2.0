# AdminTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'admin']

## Example

```python
from graalsystems.models.admin_target import AdminTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AdminTarget from a JSON string
admin_target_instance = AdminTarget.from_json(json)
# print the JSON string representation of the object
print AdminTarget.to_json()

# convert the object into a dict
admin_target_dict = admin_target_instance.to_dict()
# create an instance of AdminTarget from a dict
admin_target_form_dict = admin_target.from_dict(admin_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


