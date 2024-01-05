# AzureConnector

Connect to an Azure Blob Storage.  Attributes ---------- type : ConnectorType     Azure Blob Storage connector type. options : SQLConnectorOptions     Options to connect to an Azure Blob Storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connect to an Azure Blob Storage. | [optional] [default to 'azure']
**options** | [**AzureConnectorOptions**](AzureConnectorOptions.md) |  | 

## Example

```python
from graalsystems.models.azure_connector import AzureConnector

# TODO update the JSON string below
json = "{}"
# create an instance of AzureConnector from a JSON string
azure_connector_instance = AzureConnector.from_json(json)
# print the JSON string representation of the object
print AzureConnector.to_json()

# convert the object into a dict
azure_connector_dict = azure_connector_instance.to_dict()
# create an instance of AzureConnector from a dict
azure_connector_form_dict = azure_connector.from_dict(azure_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


