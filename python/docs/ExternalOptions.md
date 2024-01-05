# ExternalOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.external_options import ExternalOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalOptions from a JSON string
external_options_instance = ExternalOptions.from_json(json)
# print the JSON string representation of the object
print ExternalOptions.to_json()

# convert the object into a dict
external_options_dict = external_options_instance.to_dict()
# create an instance of ExternalOptions from a dict
external_options_form_dict = external_options.from_dict(external_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


