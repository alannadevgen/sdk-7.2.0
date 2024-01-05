# PrintParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_lines** | **int** | Number of lines to show. | [optional] 

## Example

```python
from graalsystems.models.print_params import PrintParams

# TODO update the JSON string below
json = "{}"
# create an instance of PrintParams from a JSON string
print_params_instance = PrintParams.from_json(json)
# print the JSON string representation of the object
print PrintParams.to_json()

# convert the object into a dict
print_params_dict = print_params_instance.to_dict()
# create an instance of PrintParams from a dict
print_params_form_dict = print_params.from_dict(print_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


