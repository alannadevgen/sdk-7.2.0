# OrderParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[Dict[str, str]]** | List of dictionary. For each element the &#39;name&#39;         corresponds to the columns to order and         the &#39;direction&#39; the direction for sorting (asc or desc). | 

## Example

```python
from graalsystems.models.order_params import OrderParams

# TODO update the JSON string below
json = "{}"
# create an instance of OrderParams from a JSON string
order_params_instance = OrderParams.from_json(json)
# print the JSON string representation of the object
print OrderParams.to_json()

# convert the object into a dict
order_params_dict = order_params_instance.to_dict()
# create an instance of OrderParams from a dict
order_params_form_dict = order_params.from_dict(order_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


