# Uri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.uri import Uri

# TODO update the JSON string below
json = "{}"
# create an instance of Uri from a JSON string
uri_instance = Uri.from_json(json)
# print the JSON string representation of the object
print Uri.to_json()

# convert the object into a dict
uri_dict = uri_instance.to_dict()
# create an instance of Uri from a dict
uri_form_dict = uri.from_dict(uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


