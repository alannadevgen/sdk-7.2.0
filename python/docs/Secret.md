# Secret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.secret import Secret

# TODO update the JSON string below
json = "{}"
# create an instance of Secret from a JSON string
secret_instance = Secret.from_json(json)
# print the JSON string representation of the object
print Secret.to_json()

# convert the object into a dict
secret_dict = secret_instance.to_dict()
# create an instance of Secret from a dict
secret_form_dict = secret.from_dict(secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


