# MaxParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Maximum aggregation. | [optional] [default to 'max']
**columns** | **List[str]** | Column(s) to compute the maximum. | 

## Example

```python
from graalsystems.models.max_params import MaxParams

# TODO update the JSON string below
json = "{}"
# create an instance of MaxParams from a JSON string
max_params_instance = MaxParams.from_json(json)
# print the JSON string representation of the object
print MaxParams.to_json()

# convert the object into a dict
max_params_dict = max_params_instance.to_dict()
# create an instance of MaxParams from a dict
max_params_form_dict = max_params.from_dict(max_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


