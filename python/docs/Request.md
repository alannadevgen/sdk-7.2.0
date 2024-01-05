# Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**product_reference** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from graalsystems.models.request import Request

# TODO update the JSON string below
json = "{}"
# create an instance of Request from a JSON string
request_instance = Request.from_json(json)
# print the JSON string representation of the object
print Request.to_json()

# convert the object into a dict
request_dict = request_instance.to_dict()
# create an instance of Request from a dict
request_form_dict = request.from_dict(request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


