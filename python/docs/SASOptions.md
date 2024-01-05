# SASOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'sas']
**lines** | **List[str]** |  | [optional] 

## Example

```python
from graalsystems.models.sas_options import SASOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SASOptions from a JSON string
sas_options_instance = SASOptions.from_json(json)
# print the JSON string representation of the object
print SASOptions.to_json()

# convert the object into a dict
sas_options_dict = sas_options_instance.to_dict()
# create an instance of SASOptions from a dict
sas_options_form_dict = sas_options.from_dict(sas_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


