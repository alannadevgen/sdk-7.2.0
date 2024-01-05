# S3ConnectorOptions

Options to connect to a S3 bucket.  Attributes ---------- bucket : str     Bucket name. access_key : str     Access key for S3. secret_key : str     Secret key for S3. session_token : str     Session token for S3. endpoint : str     URL endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | The bucket to be connected to. | 
**access_key** | **str** | S3 access key to access to AWS. | 
**secret_key** | **str** | S3 secret key to access to AWS. | 
**session_token** | **str** | S3 session token to access to AWS. | [optional] 
**endpoint** | **str** | The endpoint to be connected to. | [optional] 
**region_name** | **str** | The region of the endpoint. | [optional] 

## Example

```python
from graalsystems.models.s3_connector_options import S3ConnectorOptions

# TODO update the JSON string below
json = "{}"
# create an instance of S3ConnectorOptions from a JSON string
s3_connector_options_instance = S3ConnectorOptions.from_json(json)
# print the JSON string representation of the object
print S3ConnectorOptions.to_json()

# convert the object into a dict
s3_connector_options_dict = s3_connector_options_instance.to_dict()
# create an instance of S3ConnectorOptions from a dict
s3_connector_options_form_dict = s3_connector_options.from_dict(s3_connector_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


