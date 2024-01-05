# Dag

DagUnverified with verified schema and framework compatibility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the Directed Acyclic Graph (DAG). | 
**tasks** | [**List[TaskListInner]**](TaskListInner.md) | List of tasks that compose the DAG. | 

## Example

```python
from graalsystems.models.dag import Dag

# TODO update the JSON string below
json = "{}"
# create an instance of Dag from a JSON string
dag_instance = Dag.from_json(json)
# print the JSON string representation of the object
print Dag.to_json()

# convert the object into a dict
dag_dict = dag_instance.to_dict()
# create an instance of Dag from a dict
dag_form_dict = dag.from_dict(dag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


