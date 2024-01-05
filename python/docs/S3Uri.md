# S3Uri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 's3']
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.s3_uri import S3Uri

# TODO update the JSON string below
json = "{}"
# create an instance of S3Uri from a JSON string
s3_uri_instance = S3Uri.from_json(json)
# print the JSON string representation of the object
print S3Uri.to_json()

# convert the object into a dict
s3_uri_dict = s3_uri_instance.to_dict()
# create an instance of S3Uri from a dict
s3_uri_form_dict = s3_uri.from_dict(s3_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


