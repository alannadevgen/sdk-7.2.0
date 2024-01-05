# DagUnverified

Creates a DAG (Directed Acyclic Graph) from a JSON file.  Attributes ---------- id : str     Identifier of the DAG. tasks : ListIntVisited     Tasks that make up the DAG.  Methods ------- check_dependencies(tasks)     Checks if the tasks dependencies are valid. check_circle(tasks)     Checks that there are no circular dependencies in the DAG. get_zipped_code(language: LanguageType)     Returns the requirements and code in a zipped folder. get_nodes(tasks)     Returns all the information of the DAG as a list of tasks. get_edges(tasks)     Get all two-by-two dependencies between tasks. to_graph(tasks)     Create a graph from the DAG with the edges and nodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the Directed Acyclic Graph (DAG). | 
**tasks** | [**List[TaskListInner]**](TaskListInner.md) | List of tasks that compose the DAG. | 

## Example

```python
from graalsystems.models.dag_unverified import DagUnverified

# TODO update the JSON string below
json = "{}"
# create an instance of DagUnverified from a JSON string
dag_unverified_instance = DagUnverified.from_json(json)
# print the JSON string representation of the object
print DagUnverified.to_json()

# convert the object into a dict
dag_unverified_dict = dag_unverified_instance.to_dict()
# create an instance of DagUnverified from a dict
dag_unverified_form_dict = dag_unverified.from_dict(dag_unverified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


