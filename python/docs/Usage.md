# Usage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**product_reference** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**dimensions** | **Dict[str, str]** |  | [optional] 

## Example

```python
from graalsystems.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print Usage.to_json()

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_form_dict = usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


