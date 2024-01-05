# Graph


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.graph import Graph

# TODO update the JSON string below
json = "{}"
# create an instance of Graph from a JSON string
graph_instance = Graph.from_json(json)
# print the JSON string representation of the object
print Graph.to_json()

# convert the object into a dict
graph_dict = graph_instance.to_dict()
# create an instance of Graph from a dict
graph_form_dict = graph.from_dict(graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


