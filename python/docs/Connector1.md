# Connector1

Type of connector (local, S3, Azure).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connection to a S3 bucket. | [optional] [default to 's3']
**options** | [**AzureConnectorOptions**](AzureConnectorOptions.md) |  | 

## Example

```python
from graalsystems.models.connector1 import Connector1

# TODO update the JSON string below
json = "{}"
# create an instance of Connector1 from a JSON string
connector1_instance = Connector1.from_json(json)
# print the JSON string representation of the object
print Connector1.to_json()

# convert the object into a dict
connector1_dict = connector1_instance.to_dict()
# create an instance of Connector1 from a dict
connector1_form_dict = connector1.from_dict(connector1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


