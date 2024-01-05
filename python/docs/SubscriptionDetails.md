# SubscriptionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'subscription']
**support_plan** | **str** |  | [optional] 
**account** | **str** |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from graalsystems.models.subscription_details import SubscriptionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetails from a JSON string
subscription_details_instance = SubscriptionDetails.from_json(json)
# print the JSON string representation of the object
print SubscriptionDetails.to_json()

# convert the object into a dict
subscription_details_dict = subscription_details_instance.to_dict()
# create an instance of SubscriptionDetails from a dict
subscription_details_form_dict = subscription_details.from_dict(subscription_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


