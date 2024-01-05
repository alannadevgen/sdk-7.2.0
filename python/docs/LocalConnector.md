# LocalConnector

Connect to a local folder.  Attributes ---------- type : ConnectorType     Local type of connector. _prefix : str     Prefix to access the folder (default: empty string).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connection to a local folder. | [optional] [default to 'local']

## Example

```python
from graalsystems.models.local_connector import LocalConnector

# TODO update the JSON string below
json = "{}"
# create an instance of LocalConnector from a JSON string
local_connector_instance = LocalConnector.from_json(json)
# print the JSON string representation of the object
print LocalConnector.to_json()

# convert the object into a dict
local_connector_dict = local_connector_instance.to_dict()
# create an instance of LocalConnector from a dict
local_connector_form_dict = local_connector.from_dict(local_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


