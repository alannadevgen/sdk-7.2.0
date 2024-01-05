# PyPiLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'pypi']
**dep** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.py_pi_library import PyPiLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of PyPiLibrary from a JSON string
py_pi_library_instance = PyPiLibrary.from_json(json)
# print the JSON string representation of the object
print PyPiLibrary.to_json()

# convert the object into a dict
py_pi_library_dict = py_pi_library_instance.to_dict()
# create an instance of PyPiLibrary from a dict
py_pi_library_form_dict = py_pi_library.from_dict(py_pi_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


