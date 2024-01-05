# KubernetesTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'kubernetes']
**subtype** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**context** | **str** |  | [optional] 
**kubeconfig** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.kubernetes_target import KubernetesTarget

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesTarget from a JSON string
kubernetes_target_instance = KubernetesTarget.from_json(json)
# print the JSON string representation of the object
print KubernetesTarget.to_json()

# convert the object into a dict
kubernetes_target_dict = kubernetes_target_instance.to_dict()
# create an instance of KubernetesTarget from a dict
kubernetes_target_form_dict = kubernetes_target.from_dict(kubernetes_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


