# graalsystems.BucketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket**](BucketApi.md#create_bucket) | **POST** /buckets | Create a bucket
[**delete_bucket_by_id**](BucketApi.md#delete_bucket_by_id) | **DELETE** /buckets/{bucketId} | Delete a bucket by an id
[**find_bucket_by_id**](BucketApi.md#find_bucket_by_id) | **GET** /buckets/{bucketId} | Find bucket by Id
[**find_buckets**](BucketApi.md#find_buckets) | **GET** /buckets | Retrieve all buckets
[**update_bucket**](BucketApi.md#update_bucket) | **PATCH** /buckets/{bucketId} | Update a bucket


# **create_bucket**
> Bucket create_bucket(x_tenant, bucket)

Create a bucket

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.bucket import Bucket
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
    api_instance = graalsystems.BucketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    bucket = graalsystems.Bucket() # Bucket | The bucket to be created

    try:
        # Create a bucket
        api_response = api_instance.create_bucket(x_tenant, bucket)
        print("The response of BucketApi->create_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketApi->create_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **bucket** | [**Bucket**](Bucket.md)| The bucket to be created | 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.bucket+json
 - **Accept**: application/vnd.graal.systems.v1.bucket+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bucket_by_id**
> delete_bucket_by_id(x_tenant, bucket_id)

Delete a bucket by an id

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
    api_instance = graalsystems.BucketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    bucket_id = 'bucket_id_example' # str | Id of the bucket

    try:
        # Delete a bucket by an id
        api_instance.delete_bucket_by_id(x_tenant, bucket_id)
    except Exception as e:
        print("Exception when calling BucketApi->delete_bucket_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **bucket_id** | **str**| Id of the bucket | 

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
**404** | Bucket not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_bucket_by_id**
> Bucket find_bucket_by_id(x_tenant, bucket_id)

Find bucket by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.bucket import Bucket
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
    api_instance = graalsystems.BucketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    bucket_id = 'bucket_id_example' # str | Id of the bucket

    try:
        # Find bucket by Id
        api_response = api_instance.find_bucket_by_id(x_tenant, bucket_id)
        print("The response of BucketApi->find_bucket_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketApi->find_bucket_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **bucket_id** | **str**| Id of the bucket | 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.bucket+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Bucket not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_buckets**
> List[Bucket] find_buckets(x_tenant)

Retrieve all buckets

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.bucket import Bucket
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
    api_instance = graalsystems.BucketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all buckets
        api_response = api_instance.find_buckets(x_tenant)
        print("The response of BucketApi->find_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketApi->find_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Bucket]**](Bucket.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.bucket+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bucket**
> Bucket update_bucket(x_tenant, bucket_id, patch)

Update a bucket

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.bucket import Bucket
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
    api_instance = graalsystems.BucketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    bucket_id = 'bucket_id_example' # str | Id of the bucket
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a bucket
        api_response = api_instance.update_bucket(x_tenant, bucket_id, patch)
        print("The response of BucketApi->update_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketApi->update_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **bucket_id** | **str**| Id of the bucket | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.bucket+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Bucket not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

