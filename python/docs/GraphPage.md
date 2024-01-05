# GraphPage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Graph]**](Graph.md) |  | [optional] 

## Example

```python
from graalsystems.models.graph_page import GraphPage

# TODO update the JSON string below
json = "{}"
# create an instance of GraphPage from a JSON string
graph_page_instance = GraphPage.from_json(json)
# print the JSON string representation of the object
print GraphPage.to_json()

# convert the object into a dict
graph_page_dict = graph_page_instance.to_dict()
# create an instance of GraphPage from a dict
graph_page_form_dict = graph_page.from_dict(graph_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


