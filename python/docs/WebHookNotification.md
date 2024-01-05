# WebHookNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'webhook']
**url** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from graalsystems.models.web_hook_notification import WebHookNotification

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookNotification from a JSON string
web_hook_notification_instance = WebHookNotification.from_json(json)
# print the JSON string representation of the object
print WebHookNotification.to_json()

# convert the object into a dict
web_hook_notification_dict = web_hook_notification_instance.to_dict()
# create an instance of WebHookNotification from a dict
web_hook_notification_form_dict = web_hook_notification.from_dict(web_hook_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


