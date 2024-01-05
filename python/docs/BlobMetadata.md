# BlobMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 
**content_type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.blob_metadata import BlobMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BlobMetadata from a JSON string
blob_metadata_instance = BlobMetadata.from_json(json)
# print the JSON string representation of the object
print BlobMetadata.to_json()

# convert the object into a dict
blob_metadata_dict = blob_metadata_instance.to_dict()
# create an instance of BlobMetadata from a dict
blob_metadata_form_dict = blob_metadata.from_dict(blob_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


