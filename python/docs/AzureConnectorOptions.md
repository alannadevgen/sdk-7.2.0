# AzureConnectorOptions

Options to connect to an Azure bucket.  Attributes ---------- storage_name : str     Name of the Azure storage. sas_token : str     SAS token to connect to Azure. container : str     Name of the container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_name** | **str** | Name of the Azure Blob Storage. | 
**sas_token** | **str** | SAS token for Azure Blob Storage connection. | 
**container** | **str** | Name of the Azure Blob Storage container. | 

## Example

```python
from graalsystems.models.azure_connector_options import AzureConnectorOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AzureConnectorOptions from a JSON string
azure_connector_options_instance = AzureConnectorOptions.from_json(json)
# print the JSON string representation of the object
print AzureConnectorOptions.to_json()

# convert the object into a dict
azure_connector_options_dict = azure_connector_options_instance.to_dict()
# create an instance of AzureConnectorOptions from a dict
azure_connector_options_form_dict = azure_connector_options.from_dict(azure_connector_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


