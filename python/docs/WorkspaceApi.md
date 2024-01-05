# graalsystems.WorkspaceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspaceApi.md#create_workspace) | **POST** /workspaces | Create workspace
[**delete_workspace_by_id**](WorkspaceApi.md#delete_workspace_by_id) | **DELETE** /workspaces/{workspaceId} | Delete a workspace by an id
[**find_workspace_by_id**](WorkspaceApi.md#find_workspace_by_id) | **GET** /workspaces/{workspaceId} | Find workspace by Id
[**find_workspaces**](WorkspaceApi.md#find_workspaces) | **GET** /workspaces | Retrieve all workspaces
[**get_logs_for_workspace**](WorkspaceApi.md#get_logs_for_workspace) | **GET** /workspaces/{workspaceId}/logs | Get logs
[**update_workspace**](WorkspaceApi.md#update_workspace) | **PATCH** /workspaces/{workspaceId} | Update a workspace
[**upload_file_in_workspace**](WorkspaceApi.md#upload_file_in_workspace) | **POST** /workspaces/{workspaceId}/files | Upload files in a workspace


# **create_workspace**
> Workspace create_workspace(x_tenant, workspace)

Create workspace

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.workspace import Workspace
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
    api_instance = graalsystems.WorkspaceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workspace = graalsystems.Workspace() # Workspace | The workspace to be created

    try:
        # Create workspace
        api_response = api_instance.create_workspace(x_tenant, workspace)
        print("The response of WorkspaceApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workspace** | [**Workspace**](Workspace.md)| The workspace to be created | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.workspace+json
 - **Accept**: application/vnd.graal.systems.v1.workspace+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_by_id**
> delete_workspace_by_id(x_tenant, workspace_id)

Delete a workspace by an id

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
    api_instance = graalsystems.WorkspaceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workspace_id = 'workspace_id_example' # str | Id of the workspace

    try:
        # Delete a workspace by an id
        api_instance.delete_workspace_by_id(x_tenant, workspace_id)
    except Exception as e:
        print("Exception when calling WorkspaceApi->delete_workspace_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workspace_id** | **str**| Id of the workspace | 

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
**404** | Workspace not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workspace_by_id**
> Workspace find_workspace_by_id(x_tenant, workspace_id)

Find workspace by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.workspace import Workspace
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
    api_instance = graalsystems.WorkspaceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workspace_id = 'workspace_id_example' # str | Id of the workspace

    try:
        # Find workspace by Id
        api_response = api_instance.find_workspace_by_id(x_tenant, workspace_id)
        print("The response of WorkspaceApi->find_workspace_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->find_workspace_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workspace_id** | **str**| Id of the workspace | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.workspace+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Workspace not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workspaces**
> WorkspacePage find_workspaces(x_tenant, page=page, size=size)

Retrieve all workspaces

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.workspace_page import WorkspacePage
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
    api_instance = graalsystems.WorkspaceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    page = 0 # int |  (optional) (default to 0)
    size = 200 # int |  (optional) (default to 200)

    try:
        # Retrieve all workspaces
        api_response = api_instance.find_workspaces(x_tenant, page=page, size=size)
        print("The response of WorkspaceApi->find_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->find_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 200]

### Return type

[**WorkspacePage**](WorkspacePage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.workspace+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs_for_workspace**
> List[LogEntry] get_logs_for_workspace(x_tenant, workspace_id, cursor=cursor)

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
    api_instance = graalsystems.WorkspaceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workspace_id = 'workspace_id_example' # str | Id of the workspace
    cursor = 'cursor_example' # str | The cursor (optional)

    try:
        # Get logs
        api_response = api_instance.get_logs_for_workspace(x_tenant, workspace_id, cursor=cursor)
        print("The response of WorkspaceApi->get_logs_for_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->get_logs_for_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workspace_id** | **str**| Id of the workspace | 
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

# **update_workspace**
> Workspace update_workspace(x_tenant, workspace_id, patch)

Update a workspace

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.patch import Patch
from graalsystems.models.workspace import Workspace
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
    api_instance = graalsystems.WorkspaceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workspace_id = 'workspace_id_example' # str | Id of the workspace
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a workspace
        api_response = api_instance.update_workspace(x_tenant, workspace_id, patch)
        print("The response of WorkspaceApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workspace_id** | **str**| Id of the workspace | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.workspace+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_in_workspace**
> upload_file_in_workspace(x_tenant, workspace_id, path=path, filename=filename)

Upload files in a workspace

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
    api_instance = graalsystems.WorkspaceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workspace_id = 'workspace_id_example' # str | Id of the bucket
    path = 'path_example' # str | path (optional)
    filename = None # List[bytearray] |  (optional)

    try:
        # Upload files in a workspace
        api_instance.upload_file_in_workspace(x_tenant, workspace_id, path=path, filename=filename)
    except Exception as e:
        print("Exception when calling WorkspaceApi->upload_file_in_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workspace_id** | **str**| Id of the bucket | 
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

