# SepaDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'sepa']
**iban** | **str** |  | [optional] 
**bank_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**branch_code** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.sepa_details import SepaDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SepaDetails from a JSON string
sepa_details_instance = SepaDetails.from_json(json)
# print the JSON string representation of the object
print SepaDetails.to_json()

# convert the object into a dict
sepa_details_dict = sepa_details_instance.to_dict()
# create an instance of SepaDetails from a dict
sepa_details_form_dict = sepa_details.from_dict(sepa_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


