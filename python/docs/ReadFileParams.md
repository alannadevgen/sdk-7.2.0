# ReadFileParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object file. | [optional] [default to 'file']
**connector** | [**Connector1**](Connector1.md) |  | 
**structure** | **List[Dict[str, str]]** | List of dictionaries representing the columns         (name and type). For each dictionnary the &#39;name&#39; represents the column         name and the &#39;type&#39; their corresponding type. | [optional] 
**object** | [**ParametersToWriteAFile1**](ParametersToWriteAFile1.md) |  | 

## Example

```python
from graalsystems.models.read_file_params import ReadFileParams

# TODO update the JSON string below
json = "{}"
# create an instance of ReadFileParams from a JSON string
read_file_params_instance = ReadFileParams.from_json(json)
# print the JSON string representation of the object
print ReadFileParams.to_json()

# convert the object into a dict
read_file_params_dict = read_file_params_instance.to_dict()
# create an instance of ReadFileParams from a dict
read_file_params_form_dict = read_file_params.from_dict(read_file_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


