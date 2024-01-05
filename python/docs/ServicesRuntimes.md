# ServicesRuntimes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spark** | **bool** |  | [optional] 
**mxnet** | **bool** |  | [optional] 
**tensorflow** | **bool** |  | [optional] 
**xgboost** | **bool** |  | [optional] 
**mpi** | **object** |  | [optional] 
**pytorch** | **object** |  | [optional] 

## Example

```python
from graalsystems.models.services_runtimes import ServicesRuntimes

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesRuntimes from a JSON string
services_runtimes_instance = ServicesRuntimes.from_json(json)
# print the JSON string representation of the object
print ServicesRuntimes.to_json()

# convert the object into a dict
services_runtimes_dict = services_runtimes_instance.to_dict()
# create an instance of ServicesRuntimes from a dict
services_runtimes_form_dict = services_runtimes.from_dict(services_runtimes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


