# graalsystems.DatawarehouseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_warehouse**](DatawarehouseApi.md#create_data_warehouse) | **POST** /datawarehouses | Create datawarehouse
[**delete_data_warehouse_by_id**](DatawarehouseApi.md#delete_data_warehouse_by_id) | **DELETE** /datawarehouses/{datawarehouseId} | Delete a datawarehouse by an id
[**find_changes**](DatawarehouseApi.md#find_changes) | **GET** /datawarehouses/{datawarehouseId}/changes | Find changes by datawarehouse id
[**find_data_warehouse_by_id**](DatawarehouseApi.md#find_data_warehouse_by_id) | **GET** /datawarehouses/{datawarehouseId} | Find datawarehouse by Id
[**find_data_warehouses**](DatawarehouseApi.md#find_data_warehouses) | **GET** /datawarehouses | Retrieve all datawarehouses
[**find_tables**](DatawarehouseApi.md#find_tables) | **GET** /datawarehouses/{datawarehouseId}/tables | Find tables by datawarehouse id
[**get_logs_for_datawarehouse**](DatawarehouseApi.md#get_logs_for_datawarehouse) | **GET** /datawarehouses/{datawarehouseId}/logs | Get logs
[**update_data_warehouse**](DatawarehouseApi.md#update_data_warehouse) | **PATCH** /datawarehouses/{datawarehouseId} | Update a datawarehouse


# **create_data_warehouse**
> DataWarehouse create_data_warehouse(x_tenant, data_warehouse)

Create datawarehouse

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.data_warehouse import DataWarehouse
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
    api_instance = graalsystems.DatawarehouseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    data_warehouse = graalsystems.DataWarehouse() # DataWarehouse | The datawarehouse to be created

    try:
        # Create datawarehouse
        api_response = api_instance.create_data_warehouse(x_tenant, data_warehouse)
        print("The response of DatawarehouseApi->create_data_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatawarehouseApi->create_data_warehouse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **data_warehouse** | [**DataWarehouse**](DataWarehouse.md)| The datawarehouse to be created | 

### Return type

[**DataWarehouse**](DataWarehouse.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.datawarehouse+json
 - **Accept**: application/vnd.graal.systems.v1.datawarehouse+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_warehouse_by_id**
> delete_data_warehouse_by_id(x_tenant, datawarehouse_id)

Delete a datawarehouse by an id

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
    api_instance = graalsystems.DatawarehouseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    datawarehouse_id = 'datawarehouse_id_example' # str | Id of the datawarehouse

    try:
        # Delete a datawarehouse by an id
        api_instance.delete_data_warehouse_by_id(x_tenant, datawarehouse_id)
    except Exception as e:
        print("Exception when calling DatawarehouseApi->delete_data_warehouse_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **datawarehouse_id** | **str**| Id of the datawarehouse | 

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
**404** | DataWarehouse not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_changes**
> ChangePage find_changes(x_tenant, datawarehouse_id, page=page, size=size)

Find changes by datawarehouse id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.change_page import ChangePage
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
    api_instance = graalsystems.DatawarehouseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    datawarehouse_id = 'datawarehouse_id_example' # str | Id of the datawarehouse
    page = 0 # int |  (optional) (default to 0)
    size = 200 # int |  (optional) (default to 200)

    try:
        # Find changes by datawarehouse id
        api_response = api_instance.find_changes(x_tenant, datawarehouse_id, page=page, size=size)
        print("The response of DatawarehouseApi->find_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatawarehouseApi->find_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **datawarehouse_id** | **str**| Id of the datawarehouse | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 200]

### Return type

[**ChangePage**](ChangePage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.change+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_data_warehouse_by_id**
> DataWarehouse find_data_warehouse_by_id(x_tenant, datawarehouse_id)

Find datawarehouse by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.data_warehouse import DataWarehouse
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
    api_instance = graalsystems.DatawarehouseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    datawarehouse_id = 'datawarehouse_id_example' # str | Id of the datawarehouse

    try:
        # Find datawarehouse by Id
        api_response = api_instance.find_data_warehouse_by_id(x_tenant, datawarehouse_id)
        print("The response of DatawarehouseApi->find_data_warehouse_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatawarehouseApi->find_data_warehouse_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **datawarehouse_id** | **str**| Id of the datawarehouse | 

### Return type

[**DataWarehouse**](DataWarehouse.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.datawarehouse+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | DataWarehouse not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_data_warehouses**
> DataWarehousePage find_data_warehouses(x_tenant, page=page, size=size)

Retrieve all datawarehouses

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.data_warehouse_page import DataWarehousePage
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
    api_instance = graalsystems.DatawarehouseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    page = 0 # int |  (optional) (default to 0)
    size = 200 # int |  (optional) (default to 200)

    try:
        # Retrieve all datawarehouses
        api_response = api_instance.find_data_warehouses(x_tenant, page=page, size=size)
        print("The response of DatawarehouseApi->find_data_warehouses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatawarehouseApi->find_data_warehouses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 200]

### Return type

[**DataWarehousePage**](DataWarehousePage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.datawarehouse+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tables**
> List[Table] find_tables(x_tenant, datawarehouse_id, page=page, size=size)

Find tables by datawarehouse id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.table import Table
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
    api_instance = graalsystems.DatawarehouseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    datawarehouse_id = 'datawarehouse_id_example' # str | Id of the datawarehouse
    page = 0 # int |  (optional) (default to 0)
    size = 200 # int |  (optional) (default to 200)

    try:
        # Find tables by datawarehouse id
        api_response = api_instance.find_tables(x_tenant, datawarehouse_id, page=page, size=size)
        print("The response of DatawarehouseApi->find_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatawarehouseApi->find_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **datawarehouse_id** | **str**| Id of the datawarehouse | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 200]

### Return type

[**List[Table]**](Table.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.table+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs_for_datawarehouse**
> List[LogEntry] get_logs_for_datawarehouse(x_tenant, datawarehouse_id, cursor=cursor)

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
    api_instance = graalsystems.DatawarehouseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    datawarehouse_id = 'datawarehouse_id_example' # str | Id of the datawarehouse
    cursor = 'cursor_example' # str | The cursor (optional)

    try:
        # Get logs
        api_response = api_instance.get_logs_for_datawarehouse(x_tenant, datawarehouse_id, cursor=cursor)
        print("The response of DatawarehouseApi->get_logs_for_datawarehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatawarehouseApi->get_logs_for_datawarehouse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **datawarehouse_id** | **str**| Id of the datawarehouse | 
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

# **update_data_warehouse**
> DataWarehouse update_data_warehouse(x_tenant, datawarehouse_id, patch)

Update a datawarehouse

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.data_warehouse import DataWarehouse
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
    api_instance = graalsystems.DatawarehouseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    datawarehouse_id = 'datawarehouse_id_example' # str | Id of the datawarehouse
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a datawarehouse
        api_response = api_instance.update_data_warehouse(x_tenant, datawarehouse_id, patch)
        print("The response of DatawarehouseApi->update_data_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatawarehouseApi->update_data_warehouse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **datawarehouse_id** | **str**| Id of the datawarehouse | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**DataWarehouse**](DataWarehouse.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.datawarehouse+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

