# graalsystems.EndpointApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_proxy_infer**](EndpointApi.md#call_proxy_infer) | **POST** /projects/{projectId}/endpoints/{endpointId}/proxy/infer | Call proxy infer
[**call_proxy_metadata**](EndpointApi.md#call_proxy_metadata) | **GET** /projects/{projectId}/endpoints/{endpointId}/proxy/metadata | Call proxy metadata
[**create_endpoint_for_project**](EndpointApi.md#create_endpoint_for_project) | **POST** /projects/{projectId}/endpoints | Create endpoint
[**delete_endpoint_by_id_and_project_id**](EndpointApi.md#delete_endpoint_by_id_and_project_id) | **DELETE** /projects/{projectId}/endpoints/{endpointId} | Delete an endpoint by an id
[**find_endpoint_by_id_and_project_id**](EndpointApi.md#find_endpoint_by_id_and_project_id) | **GET** /projects/{projectId}/endpoints/{endpointId} | Find endpoint by Id
[**find_endpoints_by_project_id**](EndpointApi.md#find_endpoints_by_project_id) | **GET** /projects/{projectId}/endpoints | Retrieve all endpoints
[**get_logs_for_endpoint**](EndpointApi.md#get_logs_for_endpoint) | **GET** /projects/{projectId}/endpoints/{endpointId}/logs | Get logs
[**update_endpoint_by_id_and_project_id**](EndpointApi.md#update_endpoint_by_id_and_project_id) | **PATCH** /projects/{projectId}/endpoints/{endpointId} | Update an endpoint


# **call_proxy_infer**
> call_proxy_infer(x_tenant, project_id, endpoint_id, body=body)

Call proxy infer

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
    api_instance = graalsystems.EndpointApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    endpoint_id = 'endpoint_id_example' # str | Id of the endpoint
    body = None # object |  (optional)

    try:
        # Call proxy infer
        api_instance.call_proxy_infer(x_tenant, project_id, endpoint_id, body=body)
    except Exception as e:
        print("Exception when calling EndpointApi->call_proxy_infer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **endpoint_id** | **str**| Id of the endpoint | 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Endpoint not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_proxy_metadata**
> call_proxy_metadata(x_tenant, project_id, endpoint_id)

Call proxy metadata

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
    api_instance = graalsystems.EndpointApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    endpoint_id = 'endpoint_id_example' # str | Id of the endpoint

    try:
        # Call proxy metadata
        api_instance.call_proxy_metadata(x_tenant, project_id, endpoint_id)
    except Exception as e:
        print("Exception when calling EndpointApi->call_proxy_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **endpoint_id** | **str**| Id of the endpoint | 

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
**200** | Successful operation |  -  |
**404** | Endpoint not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoint_for_project**
> Endpoint create_endpoint_for_project(x_tenant, project_id, endpoint)

Create endpoint

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.endpoint import Endpoint
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
    api_instance = graalsystems.EndpointApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    endpoint = graalsystems.Endpoint() # Endpoint | The endpoint to be created

    try:
        # Create endpoint
        api_response = api_instance.create_endpoint_for_project(x_tenant, project_id, endpoint)
        print("The response of EndpointApi->create_endpoint_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointApi->create_endpoint_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **endpoint** | [**Endpoint**](Endpoint.md)| The endpoint to be created | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.endpoint+json
 - **Accept**: application/vnd.graal.systems.v1.endpoint+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint_by_id_and_project_id**
> delete_endpoint_by_id_and_project_id(x_tenant, project_id, endpoint_id)

Delete an endpoint by an id

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
    api_instance = graalsystems.EndpointApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    endpoint_id = 'endpoint_id_example' # str | Id of the endpoint

    try:
        # Delete an endpoint by an id
        api_instance.delete_endpoint_by_id_and_project_id(x_tenant, project_id, endpoint_id)
    except Exception as e:
        print("Exception when calling EndpointApi->delete_endpoint_by_id_and_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **endpoint_id** | **str**| Id of the endpoint | 

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
**404** | Endpoint not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_endpoint_by_id_and_project_id**
> Endpoint find_endpoint_by_id_and_project_id(x_tenant, project_id, endpoint_id)

Find endpoint by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.endpoint import Endpoint
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
    api_instance = graalsystems.EndpointApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    endpoint_id = 'endpoint_id_example' # str | Id of the endpoint

    try:
        # Find endpoint by Id
        api_response = api_instance.find_endpoint_by_id_and_project_id(x_tenant, project_id, endpoint_id)
        print("The response of EndpointApi->find_endpoint_by_id_and_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointApi->find_endpoint_by_id_and_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **endpoint_id** | **str**| Id of the endpoint | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.endpoint+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Endpoint not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_endpoints_by_project_id**
> EndpointPage find_endpoints_by_project_id(x_tenant, project_id, page=page, size=size)

Retrieve all endpoints

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.endpoint_page import EndpointPage
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
    api_instance = graalsystems.EndpointApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int |  (optional) (default to 0)
    size = 200 # int |  (optional) (default to 200)

    try:
        # Retrieve all endpoints
        api_response = api_instance.find_endpoints_by_project_id(x_tenant, project_id, page=page, size=size)
        print("The response of EndpointApi->find_endpoints_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointApi->find_endpoints_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 200]

### Return type

[**EndpointPage**](EndpointPage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.endpoint+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs_for_endpoint**
> List[LogEntry] get_logs_for_endpoint(x_tenant, project_id, endpoint_id, cursor=cursor)

Get logs

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.log_entry import LogEntry
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
    api_instance = graalsystems.EndpointApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    endpoint_id = 'endpoint_id_example' # str | Id of the endpoint
    cursor = 'cursor_example' # str | The cursor (optional)

    try:
        # Get logs
        api_response = api_instance.get_logs_for_endpoint(x_tenant, project_id, endpoint_id, cursor=cursor)
        print("The response of EndpointApi->get_logs_for_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointApi->get_logs_for_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **endpoint_id** | **str**| Id of the endpoint | 
 **cursor** | **str**| The cursor | [optional] 

### Return type

[**List[LogEntry]**](LogEntry.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.log+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * X-Cursor - Current cursor <br>  |
**400** | Bad Request |  -  |
**404** | Run of job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint_by_id_and_project_id**
> Endpoint update_endpoint_by_id_and_project_id(x_tenant, project_id, endpoint_id, patch)

Update an endpoint

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.endpoint import Endpoint
from graalsystems.models.patch import Patch
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
    api_instance = graalsystems.EndpointApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    endpoint_id = 'endpoint_id_example' # str | Id of the endpoint
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update an endpoint
        api_response = api_instance.update_endpoint_by_id_and_project_id(x_tenant, project_id, endpoint_id, patch)
        print("The response of EndpointApi->update_endpoint_by_id_and_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointApi->update_endpoint_by_id_and_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **endpoint_id** | **str**| Id of the endpoint | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.endpoint+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

