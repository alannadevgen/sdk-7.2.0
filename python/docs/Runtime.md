# Runtime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**technical_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**icon_size** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**dockerfile** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.runtime import Runtime

# TODO update the JSON string below
json = "{}"
# create an instance of Runtime from a JSON string
runtime_instance = Runtime.from_json(json)
# print the JSON string representation of the object
print Runtime.to_json()

# convert the object into a dict
runtime_dict = runtime_instance.to_dict()
# create an instance of Runtime from a dict
runtime_form_dict = runtime.from_dict(runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


