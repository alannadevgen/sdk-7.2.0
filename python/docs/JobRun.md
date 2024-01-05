# JobRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**initiator** | **str** |  | [optional] 
**infrastructure_id** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**job_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**parameters** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.job_run import JobRun

# TODO update the JSON string below
json = "{}"
# create an instance of JobRun from a JSON string
job_run_instance = JobRun.from_json(json)
# print the JSON string representation of the object
print JobRun.to_json()

# convert the object into a dict
job_run_dict = job_run_instance.to_dict()
# create an instance of JobRun from a dict
job_run_form_dict = job_run.from_dict(job_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


