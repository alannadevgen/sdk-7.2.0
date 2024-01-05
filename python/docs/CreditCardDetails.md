# CreditCardDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'credit_card']
**number** | **str** |  | [optional] 
**cvc** | **str** |  | [optional] 
**expiration_month** | **str** |  | [optional] 
**expiration_year** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.credit_card_details import CreditCardDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardDetails from a JSON string
credit_card_details_instance = CreditCardDetails.from_json(json)
# print the JSON string representation of the object
print CreditCardDetails.to_json()

# convert the object into a dict
credit_card_details_dict = credit_card_details_instance.to_dict()
# create an instance of CreditCardDetails from a dict
credit_card_details_form_dict = credit_card_details.from_dict(credit_card_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


