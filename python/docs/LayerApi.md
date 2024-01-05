# graalsystems.LayerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_layer**](LayerApi.md#create_layer) | **POST** /layers | Create a layer
[**delete_layer_by_id**](LayerApi.md#delete_layer_by_id) | **DELETE** /layers/{name} | Delete a layer by an id
[**find_layer_by_id**](LayerApi.md#find_layer_by_id) | **GET** /layers/{name} | Find layer by Id
[**find_layers**](LayerApi.md#find_layers) | **GET** /layers | Retrieve all layers
[**update_layer**](LayerApi.md#update_layer) | **PATCH** /layers/{name} | Update a layer


# **create_layer**
> Layer create_layer(x_tenant, layer)

Create a layer

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.layer import Layer
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
    api_instance = graalsystems.LayerApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    layer = graalsystems.Layer() # Layer | The layer to be created

    try:
        # Create a layer
        api_response = api_instance.create_layer(x_tenant, layer)
        print("The response of LayerApi->create_layer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayerApi->create_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **layer** | [**Layer**](Layer.md)| The layer to be created | 

### Return type

[**Layer**](Layer.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.layer+json
 - **Accept**: application/vnd.graal.systems.v1.layer+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_layer_by_id**
> delete_layer_by_id(x_tenant, name)

Delete a layer by an id

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
    api_instance = graalsystems.LayerApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    name = 'name_example' # str | Id of the layer

    try:
        # Delete a layer by an id
        api_instance.delete_layer_by_id(x_tenant, name)
    except Exception as e:
        print("Exception when calling LayerApi->delete_layer_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **name** | **str**| Id of the layer | 

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
**404** | Layer not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_layer_by_id**
> Layer find_layer_by_id(x_tenant, name)

Find layer by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.layer import Layer
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
    api_instance = graalsystems.LayerApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    name = 'name_example' # str | Id of the layer

    try:
        # Find layer by Id
        api_response = api_instance.find_layer_by_id(x_tenant, name)
        print("The response of LayerApi->find_layer_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayerApi->find_layer_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **name** | **str**| Id of the layer | 

### Return type

[**Layer**](Layer.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.layer+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Layer not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_layers**
> List[Layer] find_layers(x_tenant)

Retrieve all layers

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.layer import Layer
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
    api_instance = graalsystems.LayerApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all layers
        api_response = api_instance.find_layers(x_tenant)
        print("The response of LayerApi->find_layers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayerApi->find_layers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Layer]**](Layer.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.layer+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_layer**
> Layer update_layer(x_tenant, name, patch)

Update a layer

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.layer import Layer
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
    api_instance = graalsystems.LayerApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    name = 'name_example' # str | Id of the layer
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a layer
        api_response = api_instance.update_layer(x_tenant, name, patch)
        print("The response of LayerApi->update_layer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LayerApi->update_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **name** | **str**| Id of the layer | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Layer**](Layer.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.layer+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Layer not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

