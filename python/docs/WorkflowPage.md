# WorkflowPage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Workflow]**](Workflow.md) |  | [optional] 

## Example

```python
from graalsystems.models.workflow_page import WorkflowPage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowPage from a JSON string
workflow_page_instance = WorkflowPage.from_json(json)
# print the JSON string representation of the object
print WorkflowPage.to_json()

# convert the object into a dict
workflow_page_dict = workflow_page_instance.to_dict()
# create an instance of WorkflowPage from a dict
workflow_page_form_dict = workflow_page.from_dict(workflow_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


