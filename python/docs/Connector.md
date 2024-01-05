# Connector

Type of connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connection to a S3 bucket. | [optional] [default to 's3']
**options** | [**S3ConnectorOptions**](S3ConnectorOptions.md) |  | 

## Example

```python
from graalsystems.models.connector import Connector

# TODO update the JSON string below
json = "{}"
# create an instance of Connector from a JSON string
connector_instance = Connector.from_json(json)
# print the JSON string representation of the object
print Connector.to_json()

# convert the object into a dict
connector_dict = connector_instance.to_dict()
# create an instance of Connector from a dict
connector_form_dict = connector.from_dict(connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


