# CountParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Count aggregation. | [optional] [default to 'count']
**columns** | **List[str]** | Column(s) to count. | 

## Example

```python
from graalsystems.models.count_params import CountParams

# TODO update the JSON string below
json = "{}"
# create an instance of CountParams from a JSON string
count_params_instance = CountParams.from_json(json)
# print the JSON string representation of the object
print CountParams.to_json()

# convert the object into a dict
count_params_dict = count_params_instance.to_dict()
# create an instance of CountParams from a dict
count_params_form_dict = count_params.from_dict(count_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


