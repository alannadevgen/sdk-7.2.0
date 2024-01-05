# ReadTaskParameters

Parameters of the read task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object file. | [optional] [default to 'file']
**connector** | [**Connector**](Connector.md) |  | 
**structure** | **List[Dict[str, str]]** | List of dictionaries representing the columns (name and type). For each dictionnary the         &#39;name&#39; represents the column name and the &#39;type&#39; their corresponding type. | [optional] 
**object** | [**ParametersToWriteAFile**](ParametersToWriteAFile.md) |  | 

## Example

```python
from graalsystems.models.read_task_parameters import ReadTaskParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ReadTaskParameters from a JSON string
read_task_parameters_instance = ReadTaskParameters.from_json(json)
# print the JSON string representation of the object
print ReadTaskParameters.to_json()

# convert the object into a dict
read_task_parameters_dict = read_task_parameters_instance.to_dict()
# create an instance of ReadTaskParameters from a dict
read_task_parameters_form_dict = read_task_parameters.from_dict(read_task_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


