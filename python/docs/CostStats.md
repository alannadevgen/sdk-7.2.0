# CostStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | [optional] 
**cumulative** | **List[float]** |  | [optional] 
**budget** | **List[float]** |  | [optional] 
**budget_lower_projection** | **List[float]** |  | [optional] 
**budget_upper_projection** | **List[float]** |  | [optional] 
**period** | **List[datetime]** |  | [optional] 
**projection_period** | **List[datetime]** |  | [optional] 
**type** | **str** |  | [optional] 
**by_type** | **Dict[str, float]** |  | [optional] 

## Example

```python
from graalsystems.models.cost_stats import CostStats

# TODO update the JSON string below
json = "{}"
# create an instance of CostStats from a JSON string
cost_stats_instance = CostStats.from_json(json)
# print the JSON string representation of the object
print CostStats.to_json()

# convert the object into a dict
cost_stats_dict = cost_stats_instance.to_dict()
# create an instance of CostStats from a dict
cost_stats_form_dict = cost_stats.from_dict(cost_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


