# SQLDataReader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to connect to the SQL server. | 
**port** | **str** | Port to connect to the SQL server. | [optional] [default to '5432']
**db** | **str** | Name of the database in the SQL server. | 
**schema_db** | **str** | Logical structure defining the organization,         relationships, and attributes of the database. The public schema is the         default schema where all the new tables are created. | [optional] [default to 'public']
**table** | **str** | Name of the table in the database. | 
**user** | **str** | Username to connect to the SQL server. | 
**password** | **str** | Password to connect to the SQL server. | 
**type** | **str** | Type of database connection | [optional] [default to 'jdbc']

## Example

```python
from graalsystems.models.sql_data_reader import SQLDataReader

# TODO update the JSON string below
json = "{}"
# create an instance of SQLDataReader from a JSON string
sql_data_reader_instance = SQLDataReader.from_json(json)
# print the JSON string representation of the object
print SQLDataReader.to_json()

# convert the object into a dict
sql_data_reader_dict = sql_data_reader_instance.to_dict()
# create an instance of SQLDataReader from a dict
sql_data_reader_form_dict = sql_data_reader.from_dict(sql_data_reader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


