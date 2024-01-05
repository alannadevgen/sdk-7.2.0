# MailNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'mail']
**to** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from graalsystems.models.mail_notification import MailNotification

# TODO update the JSON string below
json = "{}"
# create an instance of MailNotification from a JSON string
mail_notification_instance = MailNotification.from_json(json)
# print the JSON string representation of the object
print MailNotification.to_json()

# convert the object into a dict
mail_notification_dict = mail_notification_instance.to_dict()
# create an instance of MailNotification from a dict
mail_notification_form_dict = mail_notification.from_dict(mail_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


