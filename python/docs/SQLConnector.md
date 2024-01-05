# SQLConnector

Connect to a SQL server.  Attributes ---------- type : ConnectorType     SQL connector type. options : SQLConnectorOptions     Options to connect to a SQL server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connection to a SQL server. | [optional] [default to 'sql']
**options** | **object** | Options to connect to a SQL server. | [optional] 

## Example

```python
from graalsystems.models.sql_connector import SQLConnector

# TODO update the JSON string below
json = "{}"
# create an instance of SQLConnector from a JSON string
sql_connector_instance = SQLConnector.from_json(json)
# print the JSON string representation of the object
print SQLConnector.to_json()

# convert the object into a dict
sql_connector_dict = sql_connector_instance.to_dict()
# create an instance of SQLConnector from a dict
sql_connector_form_dict = sql_connector.from_dict(sql_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


