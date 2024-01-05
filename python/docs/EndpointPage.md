# EndpointPage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[Endpoint]**](Endpoint.md) |  | [optional] 

## Example

```python
from graalsystems.models.endpoint_page import EndpointPage

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointPage from a JSON string
endpoint_page_instance = EndpointPage.from_json(json)
# print the JSON string representation of the object
print EndpointPage.to_json()

# convert the object into a dict
endpoint_page_dict = endpoint_page_instance.to_dict()
# create an instance of EndpointPage from a dict
endpoint_page_form_dict = endpoint_page.from_dict(endpoint_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


