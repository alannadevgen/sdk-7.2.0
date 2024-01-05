# StarburstOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | **Dict[str, str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'starburst']
**licence** | **str** |  | [optional] 
**number_workers** | **float** |  | [optional] 
**database_instance_type** | **str** |  | [optional] 
**database_type** | **str** |  | [optional] 
**conf** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.starburst_options import StarburstOptions

# TODO update the JSON string below
json = "{}"
# create an instance of StarburstOptions from a JSON string
starburst_options_instance = StarburstOptions.from_json(json)
# print the JSON string representation of the object
print StarburstOptions.to_json()

# convert the object into a dict
starburst_options_dict = starburst_options_instance.to_dict()
# create an instance of StarburstOptions from a dict
starburst_options_form_dict = starburst_options.from_dict(starburst_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


