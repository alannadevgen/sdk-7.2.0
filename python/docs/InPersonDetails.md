# InPersonDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'in_person']

## Example

```python
from graalsystems.models.in_person_details import InPersonDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InPersonDetails from a JSON string
in_person_details_instance = InPersonDetails.from_json(json)
# print the JSON string representation of the object
print InPersonDetails.to_json()

# convert the object into a dict
in_person_details_dict = in_person_details_instance.to_dict()
# create an instance of InPersonDetails from a dict
in_person_details_form_dict = in_person_details.from_dict(in_person_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


