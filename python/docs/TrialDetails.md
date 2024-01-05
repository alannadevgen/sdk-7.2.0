# TrialDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'trial']
**expire** | **datetime** |  | [optional] 

## Example

```python
from graalsystems.models.trial_details import TrialDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TrialDetails from a JSON string
trial_details_instance = TrialDetails.from_json(json)
# print the JSON string representation of the object
print TrialDetails.to_json()

# convert the object into a dict
trial_details_dict = trial_details_instance.to_dict()
# create an instance of TrialDetails from a dict
trial_details_form_dict = trial_details.from_dict(trial_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


