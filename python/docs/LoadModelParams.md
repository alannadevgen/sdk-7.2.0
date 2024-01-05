# LoadModelParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object model. | [optional] [default to 'model']
**connector** | [**Connector**](Connector.md) |  | 
**object** | [**ParametersToWriteAFile**](ParametersToWriteAFile.md) |  | 

## Example

```python
from graalsystems.models.load_model_params import LoadModelParams

# TODO update the JSON string below
json = "{}"
# create an instance of LoadModelParams from a JSON string
load_model_params_instance = LoadModelParams.from_json(json)
# print the JSON string representation of the object
print LoadModelParams.to_json()

# convert the object into a dict
load_model_params_dict = load_model_params_instance.to_dict()
# create an instance of LoadModelParams from a dict
load_model_params_form_dict = load_model_params.from_dict(load_model_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


