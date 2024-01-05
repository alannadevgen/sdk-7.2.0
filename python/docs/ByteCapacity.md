# ByteCapacity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **str** |  | [optional] 
**max** | **str** |  | [optional] 
**current** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.byte_capacity import ByteCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of ByteCapacity from a JSON string
byte_capacity_instance = ByteCapacity.from_json(json)
# print the JSON string representation of the object
print ByteCapacity.to_json()

# convert the object into a dict
byte_capacity_dict = byte_capacity_instance.to_dict()
# create an instance of ByteCapacity from a dict
byte_capacity_form_dict = byte_capacity.from_dict(byte_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


