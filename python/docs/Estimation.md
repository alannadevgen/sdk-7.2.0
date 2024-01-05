# Estimation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**requests** | [**List[Request]**](Request.md) |  | [optional] 

## Example

```python
from graalsystems.models.estimation import Estimation

# TODO update the JSON string below
json = "{}"
# create an instance of Estimation from a JSON string
estimation_instance = Estimation.from_json(json)
# print the JSON string representation of the object
print Estimation.to_json()

# convert the object into a dict
estimation_dict = estimation_instance.to_dict()
# create an instance of Estimation from a dict
estimation_form_dict = estimation.from_dict(estimation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


