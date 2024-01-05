# EnrollmentPage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Enrollment]**](Enrollment.md) |  | [optional] 

## Example

```python
from graalsystems.models.enrollment_page import EnrollmentPage

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentPage from a JSON string
enrollment_page_instance = EnrollmentPage.from_json(json)
# print the JSON string representation of the object
print EnrollmentPage.to_json()

# convert the object into a dict
enrollment_page_dict = enrollment_page_instance.to_dict()
# create an instance of EnrollmentPage from a dict
enrollment_page_form_dict = enrollment_page.from_dict(enrollment_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


