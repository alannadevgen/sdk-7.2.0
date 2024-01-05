# graalsystems.RoleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RoleApi.md#create_role) | **POST** /roles | Create a role
[**delete_role_by_id**](RoleApi.md#delete_role_by_id) | **DELETE** /roles/{roleId} | Delete an role by an id
[**find_current_roles**](RoleApi.md#find_current_roles) | **GET** /me/roles | Retrieve all roles for the current user
[**find_permissions_by_role_id**](RoleApi.md#find_permissions_by_role_id) | **GET** /roles/{roleId}/permissions | Find permissions by role id
[**find_role_by_id**](RoleApi.md#find_role_by_id) | **GET** /roles/{roleId} | Find role by Id
[**find_roles**](RoleApi.md#find_roles) | **GET** /roles | Retrieve all roles


# **create_role**
> Role create_role(x_tenant, role)

Create a role

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.role import Role
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
    api_instance = graalsystems.RoleApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    role = graalsystems.Role() # Role | The role to be created

    try:
        # Create a role
        api_response = api_instance.create_role(x_tenant, role)
        print("The response of RoleApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **role** | [**Role**](Role.md)| The role to be created | 

### Return type

[**Role**](Role.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.role+json
 - **Accept**: application/vnd.graal.systems.v1.role+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_by_id**
> delete_role_by_id(x_tenant, role_id)

Delete an role by an id

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
    api_instance = graalsystems.RoleApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    role_id = 'role_id_example' # str | Id of the role

    try:
        # Delete an role by an id
        api_instance.delete_role_by_id(x_tenant, role_id)
    except Exception as e:
        print("Exception when calling RoleApi->delete_role_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **role_id** | **str**| Id of the role | 

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
**404** | User not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_current_roles**
> List[RoleAndAssignment] find_current_roles(x_tenant)

Retrieve all roles for the current user

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.role_and_assignment import RoleAndAssignment
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
    api_instance = graalsystems.RoleApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all roles for the current user
        api_response = api_instance.find_current_roles(x_tenant)
        print("The response of RoleApi->find_current_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->find_current_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[RoleAndAssignment]**](RoleAndAssignment.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.roleassignment+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_permissions_by_role_id**
> List[str] find_permissions_by_role_id(x_tenant, role_id)

Find permissions by role id

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
    api_instance = graalsystems.RoleApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    role_id = 'role_id_example' # str | Id of the role

    try:
        # Find permissions by role id
        api_response = api_instance.find_permissions_by_role_id(x_tenant, role_id)
        print("The response of RoleApi->find_permissions_by_role_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->find_permissions_by_role_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **role_id** | **str**| Id of the role | 

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
**404** | Role not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_role_by_id**
> Role find_role_by_id(x_tenant, role_id)

Find role by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.role import Role
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
    api_instance = graalsystems.RoleApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    role_id = 'role_id_example' # str | Id of the role

    try:
        # Find role by Id
        api_response = api_instance.find_role_by_id(x_tenant, role_id)
        print("The response of RoleApi->find_role_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->find_role_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **role_id** | **str**| Id of the role | 

### Return type

[**Role**](Role.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.role+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Role not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_roles**
> List[Role] find_roles(x_tenant)

Retrieve all roles

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.role import Role
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
    api_instance = graalsystems.RoleApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all roles
        api_response = api_instance.find_roles(x_tenant)
        print("The response of RoleApi->find_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->find_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Role]**](Role.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.role+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

