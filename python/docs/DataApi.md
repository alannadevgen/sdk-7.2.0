# graalsystems.DataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_files**](DataApi.md#delete_files) | **DELETE** /buckets/{bucketId}/data | Delete files
[**download_file**](DataApi.md#download_file) | **GET** /buckets/{bucketId}/data?download | Download data by path
[**get_data_files**](DataApi.md#get_data_files) | **GET** /buckets/{bucketId}/data | Get files
[**upload_file**](DataApi.md#upload_file) | **POST** /buckets/{bucketId}/data | Upload a file


# **delete_files**
> delete_files(x_tenant, bucket_id, path)

Delete files

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = graalsystems.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with graalsystems.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graalsystems.DataApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    bucket_id = 'bucket_id_example' # str | Id of the bucket
    path = ['path_example'] # List[str] | path

    try:
        # Delete files
        api_instance.delete_files(x_tenant, bucket_id, path)
    except Exception as e:
        print("Exception when calling DataApi->delete_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **bucket_id** | **str**| Id of the bucket | 
 **path** | [**List[str]**](str.md)| path | 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**404** | File not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> bytearray download_file(x_tenant, bucket_id, path)

Download data by path

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = graalsystems.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with graalsystems.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graalsystems.DataApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    bucket_id = 'bucket_id_example' # str | Id of the bucket
    path = 'path_example' # str | path

    try:
        # Download data by path
        api_response = api_instance.download_file(x_tenant, bucket_id, path)
        print("The response of DataApi->download_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->download_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **bucket_id** | **str**| Id of the bucket | 
 **path** | **str**| path | 

### Return type

**bytearray**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | File not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_files**
> List[FileOrDirectory] get_data_files(x_tenant, bucket_id, path)

Get files

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.file_or_directory import FileOrDirectory
from graalsystems.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = graalsystems.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with graalsystems.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graalsystems.DataApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    bucket_id = 'bucket_id_example' # str | Id of the bucket
    path = 'path_example' # str | path

    try:
        # Get files
        api_response = api_instance.get_data_files(x_tenant, bucket_id, path)
        print("The response of DataApi->get_data_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->get_data_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **bucket_id** | **str**| Id of the bucket | 
 **path** | **str**| path | 

### Return type

[**List[FileOrDirectory]**](FileOrDirectory.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.file+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | File not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> upload_file(x_tenant, bucket_id, path=path, filename=filename)

Upload a file

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = graalsystems.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with graalsystems.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graalsystems.DataApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    bucket_id = 'bucket_id_example' # str | Id of the bucket
    path = 'path_example' # str | path (optional)
    filename = None # List[bytearray] |  (optional)

    try:
        # Upload a file
        api_instance.upload_file(x_tenant, bucket_id, path=path, filename=filename)
    except Exception as e:
        print("Exception when calling DataApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **bucket_id** | **str**| Id of the bucket | 
 **path** | **str**| path | [optional] 
 **filename** | **List[bytearray]**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

