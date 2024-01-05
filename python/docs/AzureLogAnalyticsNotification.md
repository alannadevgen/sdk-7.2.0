# AzureLogAnalyticsNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'eventhub']
**key** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.azure_log_analytics_notification import AzureLogAnalyticsNotification

# TODO update the JSON string below
json = "{}"
# create an instance of AzureLogAnalyticsNotification from a JSON string
azure_log_analytics_notification_instance = AzureLogAnalyticsNotification.from_json(json)
# print the JSON string representation of the object
print AzureLogAnalyticsNotification.to_json()

# convert the object into a dict
azure_log_analytics_notification_dict = azure_log_analytics_notification_instance.to_dict()
# create an instance of AzureLogAnalyticsNotification from a dict
azure_log_analytics_notification_form_dict = azure_log_analytics_notification.from_dict(azure_log_analytics_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


