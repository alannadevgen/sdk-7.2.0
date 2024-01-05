# IdentityProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.identity_provider import IdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProvider from a JSON string
identity_provider_instance = IdentityProvider.from_json(json)
# print the JSON string representation of the object
print IdentityProvider.to_json()

# convert the object into a dict
identity_provider_dict = identity_provider_instance.to_dict()
# create an instance of IdentityProvider from a dict
identity_provider_form_dict = identity_provider.from_dict(identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


