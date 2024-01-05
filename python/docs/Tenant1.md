# Tenant1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.tenant1 import Tenant1

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant1 from a JSON string
tenant1_instance = Tenant1.from_json(json)
# print the JSON string representation of the object
print Tenant1.to_json()

# convert the object into a dict
tenant1_dict = tenant1_instance.to_dict()
# create an instance of Tenant1 from a dict
tenant1_form_dict = tenant1.from_dict(tenant1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


