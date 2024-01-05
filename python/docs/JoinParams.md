# JoinParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[Dict[str, str]]** | List of dictionaries where the &#39;left&#39; key represents the         name of the column in the left DataFrame and the &#39;right&#39; key represents         the name of the column to join with the right DataFrame. | 
**join_type** | **str** | Join two tables (left, right, inner, outer) | 

## Example

```python
from graalsystems.models.join_params import JoinParams

# TODO update the JSON string below
json = "{}"
# create an instance of JoinParams from a JSON string
join_params_instance = JoinParams.from_json(json)
# print the JSON string representation of the object
print JoinParams.to_json()

# convert the object into a dict
join_params_dict = join_params_instance.to_dict()
# create an instance of JoinParams from a dict
join_params_form_dict = join_params.from_dict(join_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


