# graalsystems.ModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model**](ModelApi.md#create_model) | **POST** /models | Create a model
[**delete_model_by_id**](ModelApi.md#delete_model_by_id) | **DELETE** /models/{modelId} | Delete a model by an id
[**delete_model_version_by_id**](ModelApi.md#delete_model_version_by_id) | **DELETE** /models/{modelId}/versions/{versionId} | Delete a model by an id
[**download_model**](ModelApi.md#download_model) | **GET** /models/{modelId}/versions/{versionId} | Download model by Id
[**find_model_by_id**](ModelApi.md#find_model_by_id) | **GET** /models/{modelId} | Find model by Id
[**find_model_version_metadata**](ModelApi.md#find_model_version_metadata) | **GET** /models/{modelId}/versions/{versionId}/metadata | Get model metadata by Id
[**find_models**](ModelApi.md#find_models) | **GET** /models | Retrieve all models
[**find_versions_for_model**](ModelApi.md#find_versions_for_model) | **GET** /models/{modelId}/versions | Retrieve all versions for a model
[**update_model**](ModelApi.md#update_model) | **PATCH** /models/{modelId} | Update a model


# **create_model**
> Model create_model(x_tenant, model)

Create a model

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.model import Model
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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    model = graalsystems.Model() # Model | The model to be created

    try:
        # Create a model
        api_response = api_instance.create_model(x_tenant, model)
        print("The response of ModelApi->create_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->create_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **model** | [**Model**](Model.md)| The model to be created | 

### Return type

[**Model**](Model.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.model+json
 - **Accept**: application/vnd.graal.systems.v1.project+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_by_id**
> delete_model_by_id(x_tenant, model_id)

Delete a model by an id

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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    model_id = 'model_id_example' # str | Id of the model

    try:
        # Delete a model by an id
        api_instance.delete_model_by_id(x_tenant, model_id)
    except Exception as e:
        print("Exception when calling ModelApi->delete_model_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **model_id** | **str**| Id of the model | 

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
**404** | Model not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_version_by_id**
> delete_model_version_by_id(x_tenant, model_id, version_id)

Delete a model by an id

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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    model_id = 'model_id_example' # str | Id of the model
    version_id = 'version_id_example' # str | Id of the version

    try:
        # Delete a model by an id
        api_instance.delete_model_version_by_id(x_tenant, model_id, version_id)
    except Exception as e:
        print("Exception when calling ModelApi->delete_model_version_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **model_id** | **str**| Id of the model | 
 **version_id** | **str**| Id of the version | 

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
**404** | Model not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_model**
> bytearray download_model(x_tenant, model_id, version_id)

Download model by Id

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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    model_id = 'model_id_example' # str | Id of the model
    version_id = 'version_id_example' # str | Id of the version

    try:
        # Download model by Id
        api_response = api_instance.download_model(x_tenant, model_id, version_id)
        print("The response of ModelApi->download_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->download_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **model_id** | **str**| Id of the model | 
 **version_id** | **str**| Id of the version | 

### Return type

**bytearray**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Model not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_model_by_id**
> Model find_model_by_id(x_tenant, model_id)

Find model by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.model import Model
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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    model_id = 'model_id_example' # str | Id of the model

    try:
        # Find model by Id
        api_response = api_instance.find_model_by_id(x_tenant, model_id)
        print("The response of ModelApi->find_model_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->find_model_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **model_id** | **str**| Id of the model | 

### Return type

[**Model**](Model.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.model+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Model not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_model_version_metadata**
> BlobMetadata find_model_version_metadata(x_tenant, model_id, version_id)

Get model metadata by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.blob_metadata import BlobMetadata
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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    model_id = 'model_id_example' # str | Id of the library
    version_id = 'version_id_example' # str | Id of the version

    try:
        # Get model metadata by Id
        api_response = api_instance.find_model_version_metadata(x_tenant, model_id, version_id)
        print("The response of ModelApi->find_model_version_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->find_model_version_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **model_id** | **str**| Id of the library | 
 **version_id** | **str**| Id of the version | 

### Return type

[**BlobMetadata**](BlobMetadata.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.blobmetadata+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Model not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_models**
> List[Model] find_models(x_tenant)

Retrieve all models

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.model import Model
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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all models
        api_response = api_instance.find_models(x_tenant)
        print("The response of ModelApi->find_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->find_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Model]**](Model.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.model+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_versions_for_model**
> List[ModelVersion] find_versions_for_model(x_tenant, model_id)

Retrieve all versions for a model

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.model_version import ModelVersion
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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    model_id = 'model_id_example' # str | Id of the model

    try:
        # Retrieve all versions for a model
        api_response = api_instance.find_versions_for_model(x_tenant, model_id)
        print("The response of ModelApi->find_versions_for_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->find_versions_for_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **model_id** | **str**| Id of the model | 

### Return type

[**List[ModelVersion]**](ModelVersion.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.modelversion+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> Model update_model(x_tenant, model_id, patch)

Update a model

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.model import Model
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
    api_instance = graalsystems.ModelApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    model_id = 'model_id_example' # str | Id of the model
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a model
        api_response = api_instance.update_model(x_tenant, model_id, patch)
        print("The response of ModelApi->update_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->update_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **model_id** | **str**| Id of the model | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Model**](Model.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.model+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Model not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

