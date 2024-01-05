# graalsystems.RuntimeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_runtime_by_id**](RuntimeApi.md#build_runtime_by_id) | **PATCH** /runtimes/{runtimeId}/builds | Find runtime by Id
[**create_runtime**](RuntimeApi.md#create_runtime) | **POST** /runtimes | Create runtime
[**delete_runtime_by_id**](RuntimeApi.md#delete_runtime_by_id) | **DELETE** /runtimes/{runtimeId} | Delete a runtime by an id
[**find_build_by_runtime_id_and_build_id**](RuntimeApi.md#find_build_by_runtime_id_and_build_id) | **GET** /runtimes/{runtimeId}/builds/{buildId} | Find the build by a runtimeId and a buildId
[**find_builds_for_runtime**](RuntimeApi.md#find_builds_for_runtime) | **GET** /runtimes/{runtimeId}/builds | Retrieve all builds for a runtime
[**find_dependencies_by_runtime_id_and_version_id**](RuntimeApi.md#find_dependencies_by_runtime_id_and_version_id) | **GET** /runtimes/{runtimeId}/versions/{versionId}/dependencies | Find the dependencies by a runtimeId and a versionId
[**find_runtime_by_id**](RuntimeApi.md#find_runtime_by_id) | **GET** /runtimes/{runtimeId} | Find runtime by Id
[**find_runtimes**](RuntimeApi.md#find_runtimes) | **GET** /runtimes | Retrieve all runtimes
[**find_version_by_runtime_id_and_version_id**](RuntimeApi.md#find_version_by_runtime_id_and_version_id) | **GET** /runtimes/{runtimeId}/versions/{versionId} | Find the build by a runtimeId and a versionId
[**find_versions_for_runtime**](RuntimeApi.md#find_versions_for_runtime) | **GET** /runtimes/{runtimeId}/versions | Retrieve all versions for a runtime
[**get_logs_for_build**](RuntimeApi.md#get_logs_for_build) | **GET** /runtimes/{runtimeId}/builds/{buildId}/logs | Get logs


# **build_runtime_by_id**
> Build build_runtime_by_id(x_tenant, runtime_id)

Find runtime by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.build import Build
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime

    try:
        # Find runtime by Id
        api_response = api_instance.build_runtime_by_id(x_tenant, runtime_id)
        print("The response of RuntimeApi->build_runtime_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->build_runtime_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 

### Return type

[**Build**](Build.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.build+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Runtime not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_runtime**
> Runtime create_runtime(x_tenant, runtime)

Create runtime

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.runtime import Runtime
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime = graalsystems.Runtime() # Runtime | The runtime to be created

    try:
        # Create runtime
        api_response = api_instance.create_runtime(x_tenant, runtime)
        print("The response of RuntimeApi->create_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->create_runtime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime** | [**Runtime**](Runtime.md)| The runtime to be created | 

### Return type

[**Runtime**](Runtime.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.runtime+json
 - **Accept**: application/vnd.graal.systems.v1.runtime+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_runtime_by_id**
> delete_runtime_by_id(x_tenant, runtime_id)

Delete a runtime by an id

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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime

    try:
        # Delete a runtime by an id
        api_instance.delete_runtime_by_id(x_tenant, runtime_id)
    except Exception as e:
        print("Exception when calling RuntimeApi->delete_runtime_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 

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
**404** | Runtime not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_build_by_runtime_id_and_build_id**
> Build find_build_by_runtime_id_and_build_id(x_tenant, runtime_id, build_id)

Find the build by a runtimeId and a buildId

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.build import Build
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime
    build_id = 'build_id_example' # str | Id of the build

    try:
        # Find the build by a runtimeId and a buildId
        api_response = api_instance.find_build_by_runtime_id_and_build_id(x_tenant, runtime_id, build_id)
        print("The response of RuntimeApi->find_build_by_runtime_id_and_build_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->find_build_by_runtime_id_and_build_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 
 **build_id** | **str**| Id of the build | 

### Return type

[**Build**](Build.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.build+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Runtime not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_builds_for_runtime**
> List[Build] find_builds_for_runtime(x_tenant, runtime_id)

Retrieve all builds for a runtime

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.build import Build
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime

    try:
        # Retrieve all builds for a runtime
        api_response = api_instance.find_builds_for_runtime(x_tenant, runtime_id)
        print("The response of RuntimeApi->find_builds_for_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->find_builds_for_runtime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 

### Return type

[**List[Build]**](Build.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.build+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_dependencies_by_runtime_id_and_version_id**
> List[Dependency] find_dependencies_by_runtime_id_and_version_id(x_tenant, runtime_id, version_id)

Find the dependencies by a runtimeId and a versionId

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.dependency import Dependency
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime
    version_id = 'version_id_example' # str | Id of the version

    try:
        # Find the dependencies by a runtimeId and a versionId
        api_response = api_instance.find_dependencies_by_runtime_id_and_version_id(x_tenant, runtime_id, version_id)
        print("The response of RuntimeApi->find_dependencies_by_runtime_id_and_version_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->find_dependencies_by_runtime_id_and_version_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 
 **version_id** | **str**| Id of the version | 

### Return type

[**List[Dependency]**](Dependency.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.dependency+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Runtime not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_runtime_by_id**
> Runtime find_runtime_by_id(x_tenant, runtime_id)

Find runtime by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.runtime import Runtime
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime

    try:
        # Find runtime by Id
        api_response = api_instance.find_runtime_by_id(x_tenant, runtime_id)
        print("The response of RuntimeApi->find_runtime_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->find_runtime_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 

### Return type

[**Runtime**](Runtime.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.runtime+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Runtime not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_runtimes**
> List[Runtime] find_runtimes(x_tenant)

Retrieve all runtimes

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.runtime import Runtime
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all runtimes
        api_response = api_instance.find_runtimes(x_tenant)
        print("The response of RuntimeApi->find_runtimes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->find_runtimes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Runtime]**](Runtime.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.runtime+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_version_by_runtime_id_and_version_id**
> RuntimeVersion find_version_by_runtime_id_and_version_id(x_tenant, runtime_id, version_id)

Find the build by a runtimeId and a versionId

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.runtime_version import RuntimeVersion
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime
    version_id = 'version_id_example' # str | Id of the version

    try:
        # Find the build by a runtimeId and a versionId
        api_response = api_instance.find_version_by_runtime_id_and_version_id(x_tenant, runtime_id, version_id)
        print("The response of RuntimeApi->find_version_by_runtime_id_and_version_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->find_version_by_runtime_id_and_version_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 
 **version_id** | **str**| Id of the version | 

### Return type

[**RuntimeVersion**](RuntimeVersion.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.runtimeversion+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Runtime not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_versions_for_runtime**
> List[RuntimeVersion] find_versions_for_runtime(x_tenant, runtime_id)

Retrieve all versions for a runtime

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.runtime_version import RuntimeVersion
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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime

    try:
        # Retrieve all versions for a runtime
        api_response = api_instance.find_versions_for_runtime(x_tenant, runtime_id)
        print("The response of RuntimeApi->find_versions_for_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->find_versions_for_runtime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 

### Return type

[**List[RuntimeVersion]**](RuntimeVersion.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.runtimeversion+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs_for_build**
> List[LogEntry] get_logs_for_build(x_tenant, runtime_id, build_id, cursor=cursor)

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
    api_instance = graalsystems.RuntimeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    runtime_id = 'runtime_id_example' # str | Id of the runtime
    build_id = 'build_id_example' # str | Id of the build
    cursor = 'cursor_example' # str | The cursor (optional)

    try:
        # Get logs
        api_response = api_instance.get_logs_for_build(x_tenant, runtime_id, build_id, cursor=cursor)
        print("The response of RuntimeApi->get_logs_for_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->get_logs_for_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **runtime_id** | **str**| Id of the runtime | 
 **build_id** | **str**| Id of the build | 
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

