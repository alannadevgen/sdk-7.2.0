# SynapseOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'synapse']

## Example

```python
from graalsystems.models.synapse_options import SynapseOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SynapseOptions from a JSON string
synapse_options_instance = SynapseOptions.from_json(json)
# print the JSON string representation of the object
print SynapseOptions.to_json()

# convert the object into a dict
synapse_options_dict = synapse_options_instance.to_dict()
# create an instance of SynapseOptions from a dict
synapse_options_form_dict = synapse_options.from_dict(synapse_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


