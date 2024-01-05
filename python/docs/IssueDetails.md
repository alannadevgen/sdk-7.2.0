# IssueDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'issue']
**resource_type** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.issue_details import IssueDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IssueDetails from a JSON string
issue_details_instance = IssueDetails.from_json(json)
# print the JSON string representation of the object
print IssueDetails.to_json()

# convert the object into a dict
issue_details_dict = issue_details_instance.to_dict()
# create an instance of IssueDetails from a dict
issue_details_form_dict = issue_details.from_dict(issue_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


