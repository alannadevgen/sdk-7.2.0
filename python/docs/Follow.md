# Follow

Object Follow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**resource** | [**Resource1**](Resource1.md) |  | [optional] 
**follower** | [**User1**](User1.md) |  | [optional] 

## Example

```python
from graalsystems.models.follow import Follow

# TODO update the JSON string below
json = "{}"
# create an instance of Follow from a JSON string
follow_instance = Follow.from_json(json)
# print the JSON string representation of the object
print Follow.to_json()

# convert the object into a dict
follow_dict = follow_instance.to_dict()
# create an instance of Follow from a dict
follow_form_dict = follow.from_dict(follow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


