# SnowflakeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'snowflake']

## Example

```python
from graalsystems.models.snowflake_options import SnowflakeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeOptions from a JSON string
snowflake_options_instance = SnowflakeOptions.from_json(json)
# print the JSON string representation of the object
print SnowflakeOptions.to_json()

# convert the object into a dict
snowflake_options_dict = snowflake_options_instance.to_dict()
# create an instance of SnowflakeOptions from a dict
snowflake_options_form_dict = snowflake_options.from_dict(snowflake_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


