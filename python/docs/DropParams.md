# DropParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[str]** | List of columns to drop. | 

## Example

```python
from graalsystems.models.drop_params import DropParams

# TODO update the JSON string below
json = "{}"
# create an instance of DropParams from a JSON string
drop_params_instance = DropParams.from_json(json)
# print the JSON string representation of the object
print DropParams.to_json()

# convert the object into a dict
drop_params_dict = drop_params_instance.to_dict()
# create an instance of DropParams from a dict
drop_params_form_dict = drop_params.from_dict(drop_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


