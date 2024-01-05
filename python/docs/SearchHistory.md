# SearchHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**term** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 

## Example

```python
from graalsystems.models.search_history import SearchHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SearchHistory from a JSON string
search_history_instance = SearchHistory.from_json(json)
# print the JSON string representation of the object
print SearchHistory.to_json()

# convert the object into a dict
search_history_dict = search_history_instance.to_dict()
# create an instance of SearchHistory from a dict
search_history_form_dict = search_history.from_dict(search_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


