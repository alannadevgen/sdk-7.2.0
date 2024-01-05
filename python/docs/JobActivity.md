# JobActivity

Object JobActivity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**reaction_count** | [**List[Reaction]**](Reaction.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'job']
**actor** | [**User1**](User1.md) |  | 
**target** | [**Job1**](Job1.md) |  | 
**verb** | **str** |  | 

## Example

```python
from graalsystems.models.job_activity import JobActivity

# TODO update the JSON string below
json = "{}"
# create an instance of JobActivity from a JSON string
job_activity_instance = JobActivity.from_json(json)
# print the JSON string representation of the object
print JobActivity.to_json()

# convert the object into a dict
job_activity_dict = job_activity_instance.to_dict()
# create an instance of JobActivity from a dict
job_activity_form_dict = job_activity.from_dict(job_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


