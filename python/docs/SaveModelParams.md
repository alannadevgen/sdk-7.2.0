# SaveModelParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object model. | [optional] [default to 'model']
**connector** | [**Connector**](Connector.md) |  | 
**object** | [**ParametersToWriteAFile2**](ParametersToWriteAFile2.md) |  | 

## Example

```python
from graalsystems.models.save_model_params import SaveModelParams

# TODO update the JSON string below
json = "{}"
# create an instance of SaveModelParams from a JSON string
save_model_params_instance = SaveModelParams.from_json(json)
# print the JSON string representation of the object
print SaveModelParams.to_json()

# convert the object into a dict
save_model_params_dict = save_model_params_instance.to_dict()
# create an instance of SaveModelParams from a dict
save_model_params_form_dict = save_model_params.from_dict(save_model_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


