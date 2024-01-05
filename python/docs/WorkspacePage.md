# WorkspacePage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Workspace]**](Workspace.md) |  | [optional] 

## Example

```python
from graalsystems.models.workspace_page import WorkspacePage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePage from a JSON string
workspace_page_instance = WorkspacePage.from_json(json)
# print the JSON string representation of the object
print WorkspacePage.to_json()

# convert the object into a dict
workspace_page_dict = workspace_page_instance.to_dict()
# create an instance of WorkspacePage from a dict
workspace_page_form_dict = workspace_page.from_dict(workspace_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


