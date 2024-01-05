# WriteSQLParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type SQL server. | [optional] [default to 'sql']
**object** | [**SQLDataWriter**](SQLDataWriter.md) |  | 
**structure** | **List[Dict[str, str]]** | List of dictionaries representing the columns (name and type). For each dictionnary the         &#39;name&#39; represents the column name and the &#39;type&#39; their corresponding type. | [optional] 
**connector** | [**DatabaseConnector**](DatabaseConnector.md) |  | 

## Example

```python
from graalsystems.models.write_sql_params import WriteSQLParams

# TODO update the JSON string below
json = "{}"
# create an instance of WriteSQLParams from a JSON string
write_sql_params_instance = WriteSQLParams.from_json(json)
# print the JSON string representation of the object
print WriteSQLParams.to_json()

# convert the object into a dict
write_sql_params_dict = write_sql_params_instance.to_dict()
# create an instance of WriteSQLParams from a dict
write_sql_params_form_dict = write_sql_params.from_dict(write_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


