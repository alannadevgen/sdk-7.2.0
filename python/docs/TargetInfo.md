# TargetInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_nodes** | [**Capacity**](Capacity.md) |  | [optional] 
**total_cpus** | [**Capacity**](Capacity.md) |  | [optional] 
**total_memory** | [**ByteCapacity**](ByteCapacity.md) |  | [optional] 
**availability_zones** | **List[str]** |  | [optional] 

## Example

```python
from graalsystems.models.target_info import TargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TargetInfo from a JSON string
target_info_instance = TargetInfo.from_json(json)
# print the JSON string representation of the object
print TargetInfo.to_json()

# convert the object into a dict
target_info_dict = target_info_instance.to_dict()
# create an instance of TargetInfo from a dict
target_info_form_dict = target_info.from_dict(target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


