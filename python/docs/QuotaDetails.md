# QuotaDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'quota']
**scope** | **str** |  | [optional] 
**new_value** | **float** |  | [optional] 

## Example

```python
from graalsystems.models.quota_details import QuotaDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaDetails from a JSON string
quota_details_instance = QuotaDetails.from_json(json)
# print the JSON string representation of the object
print QuotaDetails.to_json()

# convert the object into a dict
quota_details_dict = quota_details_instance.to_dict()
# create an instance of QuotaDetails from a dict
quota_details_form_dict = quota_details.from_dict(quota_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


