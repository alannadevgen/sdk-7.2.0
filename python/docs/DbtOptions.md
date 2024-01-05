# DbtOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dbt']
**profile** | **str** |  | [optional] 
**adapter** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.dbt_options import DbtOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DbtOptions from a JSON string
dbt_options_instance = DbtOptions.from_json(json)
# print the JSON string representation of the object
print DbtOptions.to_json()

# convert the object into a dict
dbt_options_dict = dbt_options_instance.to_dict()
# create an instance of DbtOptions from a dict
dbt_options_form_dict = dbt_options.from_dict(dbt_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


