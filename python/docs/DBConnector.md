# DBConnector

Connector for databases.  Attributes ---------- type : ConnectorType     Database type of connector. options : DBConnectorOptions     Options to connect to a database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connector type for a database connector like SQL | [optional] [default to 'DB']
**options** | **object** | Options to connect to a database. | [optional] 

## Example

```python
from graalsystems.models.db_connector import DBConnector

# TODO update the JSON string below
json = "{}"
# create an instance of DBConnector from a JSON string
db_connector_instance = DBConnector.from_json(json)
# print the JSON string representation of the object
print DBConnector.to_json()

# convert the object into a dict
db_connector_dict = db_connector_instance.to_dict()
# create an instance of DBConnector from a dict
db_connector_form_dict = db_connector.from_dict(db_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


