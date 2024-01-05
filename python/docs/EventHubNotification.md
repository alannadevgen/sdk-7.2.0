# EventHubNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'eventhub']
**connection_string** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.event_hub_notification import EventHubNotification

# TODO update the JSON string below
json = "{}"
# create an instance of EventHubNotification from a JSON string
event_hub_notification_instance = EventHubNotification.from_json(json)
# print the JSON string representation of the object
print EventHubNotification.to_json()

# convert the object into a dict
event_hub_notification_dict = event_hub_notification_instance.to_dict()
# create an instance of EventHubNotification from a dict
event_hub_notification_form_dict = event_hub_notification.from_dict(event_hub_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


