# Capacity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**current** | **float** |  | [optional] 

## Example

```python
from graalsystems.models.capacity import Capacity

# TODO update the JSON string below
json = "{}"
# create an instance of Capacity from a JSON string
capacity_instance = Capacity.from_json(json)
# print the JSON string representation of the object
print Capacity.to_json()

# convert the object into a dict
capacity_dict = capacity_instance.to_dict()
# create an instance of Capacity from a dict
capacity_form_dict = capacity.from_dict(capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


