# graalsystems.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notebook**](SessionsApi.md#create_notebook) | **GET** /sessions/{session_id} | Check if the workspace is running and create a notebook
[**create_session**](SessionsApi.md#create_session) | **POST** /sessions | Create a new workspace and corresponding session
[**delete_session**](SessionsApi.md#delete_session) | **DELETE** /sessions/{session_id} | Delete a session
[**get_sessions**](SessionsApi.md#get_sessions) | **GET** /sessions | Get existing Sessions, used for live-coding.
[**run_session**](SessionsApi.md#run_session) | **POST** /sessions/{session_id} | Run a session


# **create_notebook**
> str create_notebook(x_tenant, session_id)

Check if the workspace is running and create a notebook

Check if the workspace is running and create a notebook.

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
    api_instance = graalsystems.SessionsApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # Check if the workspace is running and create a notebook
        api_response = api_instance.create_notebook(x_tenant, session_id)
        print("The response of SessionsApi->create_notebook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->create_notebook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

**str**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> object create_session(x_tenant, workspace_name, infrastructure_id=infrastructure_id, instance_type=instance_type)

Create a new workspace and corresponding session

Generates a session from live-coding information.

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
    api_instance = graalsystems.SessionsApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workspace_name = 'workspace_name_example' # str | 
    infrastructure_id = 'scaleway-frpar1' # str |  (optional) (default to 'scaleway-frpar1')
    instance_type = 'Standard_General_G0_v1' # str |  (optional) (default to 'Standard_General_G0_v1')

    try:
        # Create a new workspace and corresponding session
        api_response = api_instance.create_session(x_tenant, workspace_name, infrastructure_id=infrastructure_id, instance_type=instance_type)
        print("The response of SessionsApi->create_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->create_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workspace_name** | **str**|  | 
 **infrastructure_id** | **str**|  | [optional] [default to &#39;scaleway-frpar1&#39;]
 **instance_type** | **str**|  | [optional] [default to &#39;Standard_General_G0_v1&#39;]

### Return type

**object**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_session**
> str delete_session(x_tenant, session_id)

Delete a session

Delete a Session from a Zeppelin environment.

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
    api_instance = graalsystems.SessionsApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # Delete a session
        api_response = api_instance.delete_session(x_tenant, session_id)
        print("The response of SessionsApi->delete_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->delete_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

**str**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> List[Session] get_sessions(x_tenant, inactive=inactive, expiration_time=expiration_time)

Get existing Sessions, used for live-coding.

Returns a list of session id that you can filter depending on their status.

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.session import Session
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
    api_instance = graalsystems.SessionsApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    inactive = False # bool |  (optional) (default to False)
    expiration_time = 10 # int |  (optional) (default to 10)

    try:
        # Get existing Sessions, used for live-coding.
        api_response = api_instance.get_sessions(x_tenant, inactive=inactive, expiration_time=expiration_time)
        print("The response of SessionsApi->get_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **inactive** | **bool**|  | [optional] [default to False]
 **expiration_time** | **int**|  | [optional] [default to 10]

### Return type

[**List[Session]**](Session.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_session**
> object run_session(x_tenant, session_id, dag_unverified)

Run a session

Run a Session in a Zeppelin environment.

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.dag_unverified import DagUnverified
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
    api_instance = graalsystems.SessionsApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    session_id = 'session_id_example' # str | 
    dag_unverified = graalsystems.DagUnverified() # DagUnverified | 

    try:
        # Run a session
        api_response = api_instance.run_session(x_tenant, session_id, dag_unverified)
        print("The response of SessionsApi->run_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->run_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **session_id** | **str**|  | 
 **dag_unverified** | [**DagUnverified**](DagUnverified.md)|  | 

### Return type

**object**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

