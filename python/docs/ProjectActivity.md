# ProjectActivity

Object ProjectActivity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**reaction_count** | [**List[Reaction]**](Reaction.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'project']
**actor** | [**User1**](User1.md) |  | 
**target** | [**Project1**](Project1.md) |  | 
**verb** | **str** |  | 

## Example

```python
from graalsystems.models.project_activity import ProjectActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectActivity from a JSON string
project_activity_instance = ProjectActivity.from_json(json)
# print the JSON string representation of the object
print ProjectActivity.to_json()

# convert the object into a dict
project_activity_dict = project_activity_instance.to_dict()
# create an instance of ProjectActivity from a dict
project_activity_form_dict = project_activity.from_dict(project_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


