# SumParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Sum aggregation. | [optional] [default to 'sum']
**columns** | **List[str]** | Columns to sum. | 

## Example

```python
from graalsystems.models.sum_params import SumParams

# TODO update the JSON string below
json = "{}"
# create an instance of SumParams from a JSON string
sum_params_instance = SumParams.from_json(json)
# print the JSON string representation of the object
print SumParams.to_json()

# convert the object into a dict
sum_params_dict = sum_params_instance.to_dict()
# create an instance of SumParams from a dict
sum_params_form_dict = sum_params.from_dict(sum_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


