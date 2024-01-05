# GenericUri


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'generic']

## Example

```python
from graalsystems.models.generic_uri import GenericUri

# TODO update the JSON string below
json = "{}"
# create an instance of GenericUri from a JSON string
generic_uri_instance = GenericUri.from_json(json)
# print the JSON string representation of the object
print GenericUri.to_json()

# convert the object into a dict
generic_uri_dict = generic_uri_instance.to_dict()
# create an instance of GenericUri from a dict
generic_uri_form_dict = generic_uri.from_dict(generic_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


