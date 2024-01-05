# PickleWriter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Name of the path. | 
**type** | **str** | Define file type for Pickle. | [optional] [default to 'pickle']

## Example

```python
from graalsystems.models.pickle_writer import PickleWriter

# TODO update the JSON string below
json = "{}"
# create an instance of PickleWriter from a JSON string
pickle_writer_instance = PickleWriter.from_json(json)
# print the JSON string representation of the object
print PickleWriter.to_json()

# convert the object into a dict
pickle_writer_dict = pickle_writer_instance.to_dict()
# create an instance of PickleWriter from a dict
pickle_writer_form_dict = pickle_writer.from_dict(pickle_writer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


