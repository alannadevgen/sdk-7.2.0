# ReactionCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**count** | **int** |  | [optional] 

## Example

```python
from graalsystems.models.reaction_count import ReactionCount

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionCount from a JSON string
reaction_count_instance = ReactionCount.from_json(json)
# print the JSON string representation of the object
print ReactionCount.to_json()

# convert the object into a dict
reaction_count_dict = reaction_count_instance.to_dict()
# create an instance of ReactionCount from a dict
reaction_count_form_dict = reaction_count.from_dict(reaction_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


