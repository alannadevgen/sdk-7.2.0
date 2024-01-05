# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**identity_id** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 
**max_retries** | **int** |  | [optional] 
**secrets** | **List[str]** |  | [optional] 
**libraries** | [**List[Library]**](Library.md) |  | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**notifications** | [**Notifications**](Notifications.md) |  | [optional] 
**parameters** | **List[str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print Job.to_json()

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_form_dict = job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


