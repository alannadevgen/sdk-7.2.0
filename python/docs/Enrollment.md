# Enrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**platform_public_key** | **str** |  | [optional] 
**device_certificate** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from graalsystems.models.enrollment import Enrollment

# TODO update the JSON string below
json = "{}"
# create an instance of Enrollment from a JSON string
enrollment_instance = Enrollment.from_json(json)
# print the JSON string representation of the object
print Enrollment.to_json()

# convert the object into a dict
enrollment_dict = enrollment_instance.to_dict()
# create an instance of Enrollment from a dict
enrollment_form_dict = enrollment.from_dict(enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


