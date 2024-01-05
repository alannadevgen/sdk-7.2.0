# graalsystems.GraphApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_graph**](GraphApi.md#create_graph) | **POST** /graphs | Create graph
[**delete_graph_by_id**](GraphApi.md#delete_graph_by_id) | **DELETE** /graphs/{graphId} | Delete a graph by an id
[**find_graph_by_id**](GraphApi.md#find_graph_by_id) | **GET** /graphs/{graphId} | Find graph by Id
[**find_graphs**](GraphApi.md#find_graphs) | **GET** /graphs | Retrieve all graphs
[**update_graph**](GraphApi.md#update_graph) | **PATCH** /graphs/{graphId} | Update a graph


# **create_graph**
> Graph create_graph(x_tenant, graph)

Create graph

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.graph import Graph
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
    api_instance = graalsystems.GraphApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    graph = graalsystems.Graph() # Graph | The graph to be created

    try:
        # Create graph
        api_response = api_instance.create_graph(x_tenant, graph)
        print("The response of GraphApi->create_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->create_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **graph** | [**Graph**](Graph.md)| The graph to be created | 

### Return type

[**Graph**](Graph.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.graph+json
 - **Accept**: application/vnd.graal.systems.v1.graph+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_graph_by_id**
> delete_graph_by_id(x_tenant, graph_id)

Delete a graph by an id

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
    api_instance = graalsystems.GraphApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    graph_id = 'graph_id_example' # str | Id of the graph

    try:
        # Delete a graph by an id
        api_instance.delete_graph_by_id(x_tenant, graph_id)
    except Exception as e:
        print("Exception when calling GraphApi->delete_graph_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **graph_id** | **str**| Id of the graph | 

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
**404** | Graph not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_graph_by_id**
> Graph find_graph_by_id(x_tenant, graph_id)

Find graph by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.graph import Graph
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
    api_instance = graalsystems.GraphApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    graph_id = 'graph_id_example' # str | Id of the graph

    try:
        # Find graph by Id
        api_response = api_instance.find_graph_by_id(x_tenant, graph_id)
        print("The response of GraphApi->find_graph_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->find_graph_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **graph_id** | **str**| Id of the graph | 

### Return type

[**Graph**](Graph.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.graph+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Graph not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_graphs**
> GraphPage find_graphs(x_tenant, page=page, size=size, owner=owner, type=type)

Retrieve all graphs

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.graph_page import GraphPage
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
    api_instance = graalsystems.GraphApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    page = 0 # int |  (optional) (default to 0)
    size = 200 # int |  (optional) (default to 200)
    owner = 'owner_example' # str |  (optional)
    type = 'type_example' # str |  (optional)

    try:
        # Retrieve all graphs
        api_response = api_instance.find_graphs(x_tenant, page=page, size=size, owner=owner, type=type)
        print("The response of GraphApi->find_graphs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->find_graphs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 200]
 **owner** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**GraphPage**](GraphPage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.graph+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_graph**
> Graph update_graph(x_tenant, graph_id, patch)

Update a graph

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.graph import Graph
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
    api_instance = graalsystems.GraphApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    graph_id = 'graph_id_example' # str | Id of the graph
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a graph
        api_response = api_instance.update_graph(x_tenant, graph_id, patch)
        print("The response of GraphApi->update_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->update_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **graph_id** | **str**| Id of the graph | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Graph**](Graph.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.graph+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

