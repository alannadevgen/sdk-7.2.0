# AggParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_columns** | **List[str]** | Column(s) to use to group the dataset. | 
**aggregations** | [**List[AggregationsInner]**](AggregationsInner.md) | List of aggregations to compute. | 

## Example

```python
from graalsystems.models.agg_params import AggParams

# TODO update the JSON string below
json = "{}"
# create an instance of AggParams from a JSON string
agg_params_instance = AggParams.from_json(json)
# print the JSON string representation of the object
print AggParams.to_json()

# convert the object into a dict
agg_params_dict = agg_params_instance.to_dict()
# create an instance of AggParams from a dict
agg_params_form_dict = agg_params.from_dict(agg_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


