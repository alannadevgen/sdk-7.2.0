# DatabaseConnector

Type of connector (SQL or database connector)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connection to a SQL server. | [optional] [default to 'sql']
**options** | **object** | Options to connect to a database. | [optional] 

## Example

```python
from graalsystems.models.database_connector import DatabaseConnector

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConnector from a JSON string
database_connector_instance = DatabaseConnector.from_json(json)
# print the JSON string representation of the object
print DatabaseConnector.to_json()

# convert the object into a dict
database_connector_dict = database_connector_instance.to_dict()
# create an instance of DatabaseConnector from a dict
database_connector_form_dict = database_connector.from_dict(database_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


