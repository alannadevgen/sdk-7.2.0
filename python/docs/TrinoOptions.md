# TrinoOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | **Dict[str, str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'trino']
**number_workers** | **float** |  | [optional] 
**conf** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.trino_options import TrinoOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TrinoOptions from a JSON string
trino_options_instance = TrinoOptions.from_json(json)
# print the JSON string representation of the object
print TrinoOptions.to_json()

# convert the object into a dict
trino_options_dict = trino_options_instance.to_dict()
# create an instance of TrinoOptions from a dict
trino_options_form_dict = trino_options.from_dict(trino_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


