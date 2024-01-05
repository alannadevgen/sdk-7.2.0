# AzureUri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'azure']
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.azure_uri import AzureUri

# TODO update the JSON string below
json = "{}"
# create an instance of AzureUri from a JSON string
azure_uri_instance = AzureUri.from_json(json)
# print the JSON string representation of the object
print AzureUri.to_json()

# convert the object into a dict
azure_uri_dict = azure_uri_instance.to_dict()
# create an instance of AzureUri from a dict
azure_uri_form_dict = azure_uri.from_dict(azure_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


