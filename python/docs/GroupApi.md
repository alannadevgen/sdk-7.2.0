# graalsystems.GroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupApi.md#create_group) | **POST** /groups | Create a group
[**delete_group_by_id**](GroupApi.md#delete_group_by_id) | **DELETE** /groups/{groupId} | Delete an group by an id
[**find_group_by_id**](GroupApi.md#find_group_by_id) | **GET** /groups/{groupId} | Find group by Id
[**find_groups**](GroupApi.md#find_groups) | **GET** /groups | Retrieve all groups
[**find_roles_by_group_id**](GroupApi.md#find_roles_by_group_id) | **GET** /groups/{groupId}/roles | Find roles by a group id


# **create_group**
> Group create_group(x_tenant, group)

Create a group

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.group import Group
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
    api_instance = graalsystems.GroupApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    group = graalsystems.Group() # Group | The identity to be created

    try:
        # Create a group
        api_response = api_instance.create_group(x_tenant, group)
        print("The response of GroupApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **group** | [**Group**](Group.md)| The identity to be created | 

### Return type

[**Group**](Group.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.group+json
 - **Accept**: application/vnd.graal.systems.v1.group+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_by_id**
> delete_group_by_id(x_tenant, group_id)

Delete an group by an id

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
    api_instance = graalsystems.GroupApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    group_id = 'group_id_example' # str | Id of the group

    try:
        # Delete an group by an id
        api_instance.delete_group_by_id(x_tenant, group_id)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **group_id** | **str**| Id of the group | 

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

# **find_group_by_id**
> Group find_group_by_id(x_tenant, group_id)

Find group by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.group import Group
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
    api_instance = graalsystems.GroupApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    group_id = 'group_id_example' # str | Id of the group

    try:
        # Find group by Id
        api_response = api_instance.find_group_by_id(x_tenant, group_id)
        print("The response of GroupApi->find_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->find_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **group_id** | **str**| Id of the group | 

### Return type

[**Group**](Group.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.group+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Group not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_groups**
> List[Group] find_groups(x_tenant)

Retrieve all groups

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.group import Group
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
    api_instance = graalsystems.GroupApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all groups
        api_response = api_instance.find_groups(x_tenant)
        print("The response of GroupApi->find_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->find_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Group]**](Group.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.group+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_roles_by_group_id**
> List[RoleAndAssignment] find_roles_by_group_id(x_tenant, group_id)

Find roles by a group id

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
    api_instance = graalsystems.GroupApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    group_id = 'group_id_example' # str | Id of the group

    try:
        # Find roles by a group id
        api_response = api_instance.find_roles_by_group_id(x_tenant, group_id)
        print("The response of GroupApi->find_roles_by_group_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->find_roles_by_group_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **group_id** | **str**| Id of the group | 

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

