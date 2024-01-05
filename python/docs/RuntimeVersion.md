# RuntimeVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**technical_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.runtime_version import RuntimeVersion

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeVersion from a JSON string
runtime_version_instance = RuntimeVersion.from_json(json)
# print the JSON string representation of the object
print RuntimeVersion.to_json()

# convert the object into a dict
runtime_version_dict = runtime_version_instance.to_dict()
# create an instance of RuntimeVersion from a dict
runtime_version_form_dict = runtime_version.from_dict(runtime_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


