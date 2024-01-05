# TimelineSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from graalsystems.models.timeline_summary import TimelineSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineSummary from a JSON string
timeline_summary_instance = TimelineSummary.from_json(json)
# print the JSON string representation of the object
print TimelineSummary.to_json()

# convert the object into a dict
timeline_summary_dict = timeline_summary_instance.to_dict()
# create an instance of TimelineSummary from a dict
timeline_summary_form_dict = timeline_summary.from_dict(timeline_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


