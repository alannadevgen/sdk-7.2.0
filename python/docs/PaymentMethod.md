# PaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**details** | [**Details1**](Details1.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**remote_payment_method_id** | **str** |  | [optional] 
**favorite** | **bool** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from graalsystems.models.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print PaymentMethod.to_json()

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_form_dict = payment_method.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


