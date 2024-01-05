# graalsystems.DatabaseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_database**](DatabaseApi.md#create_database) | **POST** /layers/{layer_name}/databases | Create a database
[**delete_database_by_id**](DatabaseApi.md#delete_database_by_id) | **DELETE** /layers/{layer_name}/databases/{database_name} | Delete a database by an id
[**find_database_by_id**](DatabaseApi.md#find_database_by_id) | **GET** /layers/{layer_name}/databases/{database_name} | Find database by Id
[**find_databases**](DatabaseApi.md#find_databases) | **GET** /layers/{layer_name}/databases | Retrieve all databases
[**update_database**](DatabaseApi.md#update_database) | **PATCH** /layers/{layer_name}/databases/{database_name} | Update a database


# **create_database**
> Database create_database(x_tenant, layer_name, database)

Create a database

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.database import Database
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
    api_instance = graalsystems.DatabaseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    layer_name = 'layer_name_example' # str | Name of the layer
    database = graalsystems.Database() # Database | The database to be created

    try:
        # Create a database
        api_response = api_instance.create_database(x_tenant, layer_name, database)
        print("The response of DatabaseApi->create_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->create_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **layer_name** | **str**| Name of the layer | 
 **database** | [**Database**](Database.md)| The database to be created | 

### Return type

[**Database**](Database.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.database+json
 - **Accept**: application/vnd.graal.systems.v1.database+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_by_id**
> delete_database_by_id(x_tenant, layer_name, database_name)

Delete a database by an id

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
    api_instance = graalsystems.DatabaseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    layer_name = 'layer_name_example' # str | Id of the layer
    database_name = 'database_name_example' # str | Id of the database

    try:
        # Delete a database by an id
        api_instance.delete_database_by_id(x_tenant, layer_name, database_name)
    except Exception as e:
        print("Exception when calling DatabaseApi->delete_database_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **layer_name** | **str**| Id of the layer | 
 **database_name** | **str**| Id of the database | 

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
**404** | Database not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_database_by_id**
> Database find_database_by_id(x_tenant, layer_name, database_name)

Find database by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.database import Database
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
    api_instance = graalsystems.DatabaseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    layer_name = 'layer_name_example' # str | Id of the layer
    database_name = 'database_name_example' # str | Id of the database

    try:
        # Find database by Id
        api_response = api_instance.find_database_by_id(x_tenant, layer_name, database_name)
        print("The response of DatabaseApi->find_database_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->find_database_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **layer_name** | **str**| Id of the layer | 
 **database_name** | **str**| Id of the database | 

### Return type

[**Database**](Database.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.database+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Database not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_databases**
> List[Database] find_databases(x_tenant, layer_name)

Retrieve all databases

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.database import Database
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
    api_instance = graalsystems.DatabaseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    layer_name = 'layer_name_example' # str | Name of the layer

    try:
        # Retrieve all databases
        api_response = api_instance.find_databases(x_tenant, layer_name)
        print("The response of DatabaseApi->find_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->find_databases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **layer_name** | **str**| Name of the layer | 

### Return type

[**List[Database]**](Database.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.database+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database**
> Database update_database(x_tenant, layer_name, database_name, patch)

Update a database

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.database import Database
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
    api_instance = graalsystems.DatabaseApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    layer_name = 'layer_name_example' # str | Id of the layer
    database_name = 'database_name_example' # str | Id of the database
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a database
        api_response = api_instance.update_database(x_tenant, layer_name, database_name, patch)
        print("The response of DatabaseApi->update_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->update_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **layer_name** | **str**| Id of the layer | 
 **database_name** | **str**| Id of the database | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Database**](Database.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.database+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Database not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

