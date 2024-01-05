# XgboostOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'xgboost']
**module** | **str** |  | [optional] 
**number_replicas** | **float** |  | [optional] 
**master_instance_type** | **str** |  | [optional] 
**worker_instance_type** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.xgboost_options import XgboostOptions

# TODO update the JSON string below
json = "{}"
# create an instance of XgboostOptions from a JSON string
xgboost_options_instance = XgboostOptions.from_json(json)
# print the JSON string representation of the object
print XgboostOptions.to_json()

# convert the object into a dict
xgboost_options_dict = xgboost_options_instance.to_dict()
# create an instance of XgboostOptions from a dict
xgboost_options_form_dict = xgboost_options.from_dict(xgboost_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


