# KnimeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'knime']
**workflow** | **str** |  | [optional] 
**archive** | [**Library**](Library.md) |  | [optional] 
**preferences** | **List[str]** |  | [optional] 

## Example

```python
from graalsystems.models.knime_options import KnimeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of KnimeOptions from a JSON string
knime_options_instance = KnimeOptions.from_json(json)
# print the JSON string representation of the object
print KnimeOptions.to_json()

# convert the object into a dict
knime_options_dict = knime_options_instance.to_dict()
# create an instance of KnimeOptions from a dict
knime_options_form_dict = knime_options.from_dict(knime_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


