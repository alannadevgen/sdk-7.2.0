# WriteFileParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object file. | [optional] [default to 'file']
**connector** | [**Connector1**](Connector1.md) |  | 
**structure** | **List[Dict[str, str]]** | List of dictionaries representing the columns         (name and type). For each dictionnary the &#39;name&#39; represents the column         name and the &#39;type&#39; their corresponding type. | [optional] 
**object** | [**ParametersToWriteAFile3**](ParametersToWriteAFile3.md) |  | 

## Example

```python
from graalsystems.models.write_file_params import WriteFileParams

# TODO update the JSON string below
json = "{}"
# create an instance of WriteFileParams from a JSON string
write_file_params_instance = WriteFileParams.from_json(json)
# print the JSON string representation of the object
print WriteFileParams.to_json()

# convert the object into a dict
write_file_params_dict = write_file_params_instance.to_dict()
# create an instance of WriteFileParams from a dict
write_file_params_form_dict = write_file_params.from_dict(write_file_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


