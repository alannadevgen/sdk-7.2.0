# PostgreSQLOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'postgresql']

## Example

```python
from graalsystems.models.postgre_sql_options import PostgreSQLOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PostgreSQLOptions from a JSON string
postgre_sql_options_instance = PostgreSQLOptions.from_json(json)
# print the JSON string representation of the object
print PostgreSQLOptions.to_json()

# convert the object into a dict
postgre_sql_options_dict = postgre_sql_options_instance.to_dict()
# create an instance of PostgreSQLOptions from a dict
postgre_sql_options_form_dict = postgre_sql_options.from_dict(postgre_sql_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


