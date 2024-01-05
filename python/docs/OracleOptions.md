# OracleOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'oracle']

## Example

```python
from graalsystems.models.oracle_options import OracleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of OracleOptions from a JSON string
oracle_options_instance = OracleOptions.from_json(json)
# print the JSON string representation of the object
print OracleOptions.to_json()

# convert the object into a dict
oracle_options_dict = oracle_options_instance.to_dict()
# create an instance of OracleOptions from a dict
oracle_options_form_dict = oracle_options.from_dict(oracle_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


