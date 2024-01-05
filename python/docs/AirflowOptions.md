# AirflowOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'airflow']

## Example

```python
from graalsystems.models.airflow_options import AirflowOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AirflowOptions from a JSON string
airflow_options_instance = AirflowOptions.from_json(json)
# print the JSON string representation of the object
print AirflowOptions.to_json()

# convert the object into a dict
airflow_options_dict = airflow_options_instance.to_dict()
# create an instance of AirflowOptions from a dict
airflow_options_form_dict = airflow_options.from_dict(airflow_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


