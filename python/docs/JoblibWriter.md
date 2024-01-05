# JoblibWriter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Name of the path. | 
**type** | **str** | Define file type for Joblib. | [optional] [default to 'joblib']

## Example

```python
from graalsystems.models.joblib_writer import JoblibWriter

# TODO update the JSON string below
json = "{}"
# create an instance of JoblibWriter from a JSON string
joblib_writer_instance = JoblibWriter.from_json(json)
# print the JSON string representation of the object
print JoblibWriter.to_json()

# convert the object into a dict
joblib_writer_dict = joblib_writer_instance.to_dict()
# create an instance of JoblibWriter from a dict
joblib_writer_form_dict = joblib_writer.from_dict(joblib_writer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


