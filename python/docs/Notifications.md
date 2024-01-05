# Notifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_start** | [**List[Notification]**](Notification.md) |  | [optional] 
**on_success** | [**List[Notification]**](Notification.md) |  | [optional] 
**on_failure** | [**List[Notification]**](Notification.md) |  | [optional] 

## Example

```python
from graalsystems.models.notifications import Notifications

# TODO update the JSON string below
json = "{}"
# create an instance of Notifications from a JSON string
notifications_instance = Notifications.from_json(json)
# print the JSON string representation of the object
print Notifications.to_json()

# convert the object into a dict
notifications_dict = notifications_instance.to_dict()
# create an instance of Notifications from a dict
notifications_form_dict = notifications.from_dict(notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


