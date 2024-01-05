# CommentActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**create_time** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.comment_activity import CommentActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CommentActivity from a JSON string
comment_activity_instance = CommentActivity.from_json(json)
# print the JSON string representation of the object
print CommentActivity.to_json()

# convert the object into a dict
comment_activity_dict = comment_activity_instance.to_dict()
# create an instance of CommentActivity from a dict
comment_activity_form_dict = comment_activity.from_dict(comment_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


