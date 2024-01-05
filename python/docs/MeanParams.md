# MeanParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Mean aggregation. | [optional] [default to 'mean']
**columns** | **List[str]** | Column(s) to compute the mean. | 

## Example

```python
from graalsystems.models.mean_params import MeanParams

# TODO update the JSON string below
json = "{}"
# create an instance of MeanParams from a JSON string
mean_params_instance = MeanParams.from_json(json)
# print the JSON string representation of the object
print MeanParams.to_json()

# convert the object into a dict
mean_params_dict = mean_params_instance.to_dict()
# create an instance of MeanParams from a dict
mean_params_form_dict = mean_params.from_dict(mean_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


