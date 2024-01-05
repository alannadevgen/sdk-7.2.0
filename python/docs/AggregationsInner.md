# AggregationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Sum aggregation. | [optional] [default to 'sum']
**columns** | **List[str]** | Column(s) to count. | 

## Example

```python
from graalsystems.models.aggregations_inner import AggregationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationsInner from a JSON string
aggregations_inner_instance = AggregationsInner.from_json(json)
# print the JSON string representation of the object
print AggregationsInner.to_json()

# convert the object into a dict
aggregations_inner_dict = aggregations_inner_instance.to_dict()
# create an instance of AggregationsInner from a dict
aggregations_inner_form_dict = aggregations_inner.from_dict(aggregations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


