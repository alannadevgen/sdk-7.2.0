# TimelineCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_date** | **str** |  | 
**max_date** | **str** |  | 
**sum_contributions** | **int** |  | 
**timeline_summary** | [**List[TimelineSummary]**](TimelineSummary.md) |  | 

## Example

```python
from graalsystems.models.timeline_count_response import TimelineCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineCountResponse from a JSON string
timeline_count_response_instance = TimelineCountResponse.from_json(json)
# print the JSON string representation of the object
print TimelineCountResponse.to_json()

# convert the object into a dict
timeline_count_response_dict = timeline_count_response_instance.to_dict()
# create an instance of TimelineCountResponse from a dict
timeline_count_response_form_dict = timeline_count_response.from_dict(timeline_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


