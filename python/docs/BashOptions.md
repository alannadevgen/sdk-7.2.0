# BashOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'bash']
**lines** | **List[str]** |  | [optional] 

## Example

```python
from graalsystems.models.bash_options import BashOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BashOptions from a JSON string
bash_options_instance = BashOptions.from_json(json)
# print the JSON string representation of the object
print BashOptions.to_json()

# convert the object into a dict
bash_options_dict = bash_options_instance.to_dict()
# create an instance of BashOptions from a dict
bash_options_form_dict = bash_options.from_dict(bash_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


