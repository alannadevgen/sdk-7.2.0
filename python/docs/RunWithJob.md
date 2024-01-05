# RunWithJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run** | [**JobRun**](JobRun.md) |  | [optional] 
**job** | [**Job**](Job.md) |  | [optional] 

## Example

```python
from graalsystems.models.run_with_job import RunWithJob

# TODO update the JSON string below
json = "{}"
# create an instance of RunWithJob from a JSON string
run_with_job_instance = RunWithJob.from_json(json)
# print the JSON string representation of the object
print RunWithJob.to_json()

# convert the object into a dict
run_with_job_dict = run_with_job_instance.to_dict()
# create an instance of RunWithJob from a dict
run_with_job_form_dict = run_with_job.from_dict(run_with_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


