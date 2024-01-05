# DistinctParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[str]** | Return dataframe with duplicate rows removed. Certain                 columns can be used for identifying duplicates, by default use                 all of the columns. | [optional] 

## Example

```python
from graalsystems.models.distinct_params import DistinctParams

# TODO update the JSON string below
json = "{}"
# create an instance of DistinctParams from a JSON string
distinct_params_instance = DistinctParams.from_json(json)
# print the JSON string representation of the object
print DistinctParams.to_json()

# convert the object into a dict
distinct_params_dict = distinct_params_instance.to_dict()
# create an instance of DistinctParams from a dict
distinct_params_form_dict = distinct_params.from_dict(distinct_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


