# UserActivity

Object UserActivity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**reaction_count** | [**List[Reaction]**](Reaction.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'user']
**actor** | [**User1**](User1.md) |  | 
**target** | [**Target1**](Target1.md) |  | 
**verb** | **str** |  | 

## Example

```python
from graalsystems.models.user_activity import UserActivity

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivity from a JSON string
user_activity_instance = UserActivity.from_json(json)
# print the JSON string representation of the object
print UserActivity.to_json()

# convert the object into a dict
user_activity_dict = user_activity_instance.to_dict()
# create an instance of UserActivity from a dict
user_activity_form_dict = user_activity.from_dict(user_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


