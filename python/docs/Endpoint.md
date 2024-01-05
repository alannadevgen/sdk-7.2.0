# Endpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**library** | [**FileLibrary**](FileLibrary.md) |  | [optional] 
**uri** | [**Uri**](Uri.md) |  | [optional] 
**instance_type** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**infrastructure_id** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.endpoint import Endpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoint from a JSON string
endpoint_instance = Endpoint.from_json(json)
# print the JSON string representation of the object
print Endpoint.to_json()

# convert the object into a dict
endpoint_dict = endpoint_instance.to_dict()
# create an instance of Endpoint from a dict
endpoint_form_dict = endpoint.from_dict(endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


