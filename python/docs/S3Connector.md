# S3Connector

Connect to a S3 bucket.  Attributes ---------- type : ConnectorType     S3 connector type. options : S3ConnectorOptions     Options to connect to a S3 bucket (i.e. credentials). _prefix : str     Prefix of the S3 bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connection to a S3 bucket. | [optional] [default to 's3']
**options** | [**S3ConnectorOptions**](S3ConnectorOptions.md) |  | 

## Example

```python
from graalsystems.models.s3_connector import S3Connector

# TODO update the JSON string below
json = "{}"
# create an instance of S3Connector from a JSON string
s3_connector_instance = S3Connector.from_json(json)
# print the JSON string representation of the object
print S3Connector.to_json()

# convert the object into a dict
s3_connector_dict = s3_connector_instance.to_dict()
# create an instance of S3Connector from a dict
s3_connector_form_dict = s3_connector.from_dict(s3_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


