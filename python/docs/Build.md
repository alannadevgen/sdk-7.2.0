# Build


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**initiator** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**parameters** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.build import Build

# TODO update the JSON string below
json = "{}"
# create an instance of Build from a JSON string
build_instance = Build.from_json(json)
# print the JSON string representation of the object
print Build.to_json()

# convert the object into a dict
build_dict = build_instance.to_dict()
# create an instance of Build from a dict
build_form_dict = build.from_dict(build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


