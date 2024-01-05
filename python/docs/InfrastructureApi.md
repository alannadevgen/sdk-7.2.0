# graalsystems.InfrastructureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_infrastructure_by_id**](InfrastructureApi.md#delete_infrastructure_by_id) | **DELETE** /infrastructures/{infrastructureId} | Delete a infrastructure by an id
[**find_capacity_by_infrastructure_by_id**](InfrastructureApi.md#find_capacity_by_infrastructure_by_id) | **GET** /infrastructures/{infrastructureId}/capacity | Retrieve the capacity of an infrastructure
[**find_infrastructure_by_infrastructure_id**](InfrastructureApi.md#find_infrastructure_by_infrastructure_id) | **GET** /infrastructures/{infrastructureId} | Find infrastructure by Id
[**find_infrastructures**](InfrastructureApi.md#find_infrastructures) | **GET** /infrastructures | Retrieve all infrastructure
[**find_public_ips_by_infrastructure_id**](InfrastructureApi.md#find_public_ips_by_infrastructure_id) | **GET** /infrastructures/{infrastructureId}/public-ips | Find public ips by infrastructure id
[**find_services_by_infrastructure_by_id**](InfrastructureApi.md#find_services_by_infrastructure_by_id) | **GET** /infrastructures/{infrastructureId}/services | Retrieve the services of an infrastructure
[**update_infrastructure**](InfrastructureApi.md#update_infrastructure) | **PATCH** /infrastructures/{infrastructureId} | Update an infrastructure


# **delete_infrastructure_by_id**
> delete_infrastructure_by_id(x_tenant, infrastructure_id)

Delete a infrastructure by an id

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
    api_instance = graalsystems.InfrastructureApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    infrastructure_id = 'infrastructure_id_example' # str | Id of the infrastructure

    try:
        # Delete a infrastructure by an id
        api_instance.delete_infrastructure_by_id(x_tenant, infrastructure_id)
    except Exception as e:
        print("Exception when calling InfrastructureApi->delete_infrastructure_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **infrastructure_id** | **str**| Id of the infrastructure | 

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
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_capacity_by_infrastructure_by_id**
> TargetInfo find_capacity_by_infrastructure_by_id(x_tenant, infrastructure_id)

Retrieve the capacity of an infrastructure

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.target_info import TargetInfo
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
    api_instance = graalsystems.InfrastructureApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    infrastructure_id = 'infrastructure_id_example' # str | Id of the infrastructure

    try:
        # Retrieve the capacity of an infrastructure
        api_response = api_instance.find_capacity_by_infrastructure_by_id(x_tenant, infrastructure_id)
        print("The response of InfrastructureApi->find_capacity_by_infrastructure_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->find_capacity_by_infrastructure_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **infrastructure_id** | **str**| Id of the infrastructure | 

### Return type

[**TargetInfo**](TargetInfo.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.capacity+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_infrastructure_by_infrastructure_id**
> Infrastructure find_infrastructure_by_infrastructure_id(x_tenant, infrastructure_id)

Find infrastructure by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.infrastructure import Infrastructure
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
    api_instance = graalsystems.InfrastructureApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    infrastructure_id = 'infrastructure_id_example' # str | Id of the infrastructure

    try:
        # Find infrastructure by Id
        api_response = api_instance.find_infrastructure_by_infrastructure_id(x_tenant, infrastructure_id)
        print("The response of InfrastructureApi->find_infrastructure_by_infrastructure_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->find_infrastructure_by_infrastructure_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **infrastructure_id** | **str**| Id of the infrastructure | 

### Return type

[**Infrastructure**](Infrastructure.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.infrastructure+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Infrastructure not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_infrastructures**
> List[Infrastructure] find_infrastructures(x_tenant)

Retrieve all infrastructure

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.infrastructure import Infrastructure
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
    api_instance = graalsystems.InfrastructureApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all infrastructure
        api_response = api_instance.find_infrastructures(x_tenant)
        print("The response of InfrastructureApi->find_infrastructures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->find_infrastructures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Infrastructure]**](Infrastructure.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.infrastructure+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_public_ips_by_infrastructure_id**
> List[str] find_public_ips_by_infrastructure_id(x_tenant, infrastructure_id)

Find public ips by infrastructure id

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
    api_instance = graalsystems.InfrastructureApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    infrastructure_id = 'infrastructure_id_example' # str | Id of the infrastructure

    try:
        # Find public ips by infrastructure id
        api_response = api_instance.find_public_ips_by_infrastructure_id(x_tenant, infrastructure_id)
        print("The response of InfrastructureApi->find_public_ips_by_infrastructure_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->find_public_ips_by_infrastructure_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **infrastructure_id** | **str**| Id of the infrastructure | 

### Return type

**List[str]**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Infrastructure not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_services_by_infrastructure_by_id**
> Services find_services_by_infrastructure_by_id(x_tenant, infrastructure_id)

Retrieve the services of an infrastructure

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.services import Services
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
    api_instance = graalsystems.InfrastructureApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    infrastructure_id = 'infrastructure_id_example' # str | Id of the infrastructure

    try:
        # Retrieve the services of an infrastructure
        api_response = api_instance.find_services_by_infrastructure_by_id(x_tenant, infrastructure_id)
        print("The response of InfrastructureApi->find_services_by_infrastructure_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->find_services_by_infrastructure_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **infrastructure_id** | **str**| Id of the infrastructure | 

### Return type

[**Services**](Services.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.services+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_infrastructure**
> Infrastructure update_infrastructure(x_tenant, infrastructure_id, patch)

Update an infrastructure

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.infrastructure import Infrastructure
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
    api_instance = graalsystems.InfrastructureApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    infrastructure_id = 'infrastructure_id_example' # str | Id of the infrastructure
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update an infrastructure
        api_response = api_instance.update_infrastructure(x_tenant, infrastructure_id, patch)
        print("The response of InfrastructureApi->update_infrastructure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->update_infrastructure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **infrastructure_id** | **str**| Id of the infrastructure | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Infrastructure**](Infrastructure.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.infrastructure+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

