# MinParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Minimum aggregation. | [optional] [default to 'min']
**columns** | **List[str]** | Column(s) to compute the minimum. | 

## Example

```python
from graalsystems.models.min_params import MinParams

# TODO update the JSON string below
json = "{}"
# create an instance of MinParams from a JSON string
min_params_instance = MinParams.from_json(json)
# print the JSON string representation of the object
print MinParams.to_json()

# convert the object into a dict
min_params_dict = min_params_instance.to_dict()
# create an instance of MinParams from a dict
min_params_form_dict = min_params.from_dict(min_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


