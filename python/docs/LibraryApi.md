# graalsystems.LibraryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_library_by_id**](LibraryApi.md#delete_library_by_id) | **DELETE** /libraries/{libraryId} | Delete a library by an id
[**download_library**](LibraryApi.md#download_library) | **GET** /libraries/{libraryId} | Download library by Id
[**find_libraries**](LibraryApi.md#find_libraries) | **GET** /libraries | List all libraries
[**find_metadata**](LibraryApi.md#find_metadata) | **GET** /libraries/{libraryId}?metadata | Get library metadata by Id
[**upload_library**](LibraryApi.md#upload_library) | **POST** /libraries | Upload a library


# **delete_library_by_id**
> delete_library_by_id(x_tenant, library_id)

Delete a library by an id

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
    api_instance = graalsystems.LibraryApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    library_id = 'library_id_example' # str | Id of the library

    try:
        # Delete a library by an id
        api_instance.delete_library_by_id(x_tenant, library_id)
    except Exception as e:
        print("Exception when calling LibraryApi->delete_library_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **library_id** | **str**| Id of the library | 

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
**404** | Library not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_library**
> bytearray download_library(x_tenant, library_id)

Download library by Id

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
    api_instance = graalsystems.LibraryApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    library_id = 'library_id_example' # str | Id of the library

    try:
        # Download library by Id
        api_response = api_instance.download_library(x_tenant, library_id)
        print("The response of LibraryApi->download_library:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->download_library: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **library_id** | **str**| Id of the library | 

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
**404** | Library not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_libraries**
> List[BlobMetadata] find_libraries(x_tenant, id=id)

List all libraries

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.blob_metadata import BlobMetadata
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
    api_instance = graalsystems.LibraryApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    id = ['id_example'] # List[str] | Id of the library (optional)

    try:
        # List all libraries
        api_response = api_instance.find_libraries(x_tenant, id=id)
        print("The response of LibraryApi->find_libraries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->find_libraries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **id** | [**List[str]**](str.md)| Id of the library | [optional] 

### Return type

[**List[BlobMetadata]**](BlobMetadata.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.blobmetadata+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_metadata**
> BlobMetadata find_metadata(x_tenant, library_id)

Get library metadata by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.blob_metadata import BlobMetadata
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
    api_instance = graalsystems.LibraryApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    library_id = 'library_id_example' # str | Id of the library

    try:
        # Get library metadata by Id
        api_response = api_instance.find_metadata(x_tenant, library_id)
        print("The response of LibraryApi->find_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->find_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **library_id** | **str**| Id of the library | 

### Return type

[**BlobMetadata**](BlobMetadata.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.blobmetadata+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Library not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_library**
> List[BlobMetadata] upload_library(x_tenant, filename=filename)

Upload a library

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.blob_metadata import BlobMetadata
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
    api_instance = graalsystems.LibraryApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    filename = None # List[bytearray] |  (optional)

    try:
        # Upload a library
        api_response = api_instance.upload_library(x_tenant, filename=filename)
        print("The response of LibraryApi->upload_library:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryApi->upload_library: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **filename** | **List[bytearray]**|  | [optional] 

### Return type

[**List[BlobMetadata]**](BlobMetadata.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/vnd.graal.systems.v1.blobmetadata+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

