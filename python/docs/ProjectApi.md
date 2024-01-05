# graalsystems.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_for_project**](ProjectApi.md#create_job_for_project) | **POST** /projects/{projectId}/jobs | Create job
[**create_project**](ProjectApi.md#create_project) | **POST** /projects | Create a project
[**create_workflow_for_project**](ProjectApi.md#create_workflow_for_project) | **POST** /projects/{projectId}/workflows | Create workflows
[**delete_project_by_id**](ProjectApi.md#delete_project_by_id) | **DELETE** /projects/{projectId} | Delete a project by an id
[**find_banner_by_project_id**](ProjectApi.md#find_banner_by_project_id) | **GET** /projects/{projectId}/banner | Get banner
[**find_jobs_by_project_id**](ProjectApi.md#find_jobs_by_project_id) | **GET** /projects/{projectId}/jobs | Retrieve all jobs for a project
[**find_latest_runs_by_project_id**](ProjectApi.md#find_latest_runs_by_project_id) | **GET** /projects/{projectId}/runs | Retrieve all jobs for a project
[**find_project_by_id**](ProjectApi.md#find_project_by_id) | **GET** /projects/{projectId} | Find project by Id
[**find_projects**](ProjectApi.md#find_projects) | **GET** /projects | Retrieve all projects
[**find_workflows_by_project_id**](ProjectApi.md#find_workflows_by_project_id) | **GET** /projects/{projectId}/workflows | Retrieve all workflows for a project
[**get_metrics_for_project**](ProjectApi.md#get_metrics_for_project) | **GET** /projects/{projectId}/metrics | Find the metrics for a project
[**get_stats_by_project_id**](ProjectApi.md#get_stats_by_project_id) | **GET** /projects/{projectId}/stats | Find the stats for a project
[**update_project**](ProjectApi.md#update_project) | **PATCH** /projects/{projectId} | Update a project
[**upload_banner**](ProjectApi.md#upload_banner) | **POST** /projects/{projectId}/banner | Upload a new banner


# **create_job_for_project**
> Job create_job_for_project(x_tenant, project_id, job)

Create job

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.job import Job
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    job = graalsystems.Job() # Job | The job to be created

    try:
        # Create job
        api_response = api_instance.create_job_for_project(x_tenant, project_id, job)
        print("The response of ProjectApi->create_job_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_job_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **job** | [**Job**](Job.md)| The job to be created | 

### Return type

[**Job**](Job.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.job+json
 - **Accept**: application/vnd.graal.systems.v1.job+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(x_tenant, project)

Create a project

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.project import Project
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project = graalsystems.Project() # Project | The project to be created

    try:
        # Create a project
        api_response = api_instance.create_project(x_tenant, project)
        print("The response of ProjectApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project** | [**Project**](Project.md)| The project to be created | 

### Return type

[**Project**](Project.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.project+json
 - **Accept**: application/vnd.graal.systems.v1.project+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workflow_for_project**
> Workflow create_workflow_for_project(x_tenant, project_id, workflow)

Create workflows

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.workflow import Workflow
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    workflow = graalsystems.Workflow() # Workflow | The workflows to be created

    try:
        # Create workflows
        api_response = api_instance.create_workflow_for_project(x_tenant, project_id, workflow)
        print("The response of ProjectApi->create_workflow_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_workflow_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **workflow** | [**Workflow**](Workflow.md)| The workflows to be created | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.workflow+json
 - **Accept**: application/vnd.graal.systems.v1.workflow+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_by_id**
> delete_project_by_id(x_tenant, project_id)

Delete a project by an id

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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project

    try:
        # Delete a project by an id
        api_instance.delete_project_by_id(x_tenant, project_id)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 

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

# **find_banner_by_project_id**
> bytearray find_banner_by_project_id(x_tenant, project_id, size=size)

Get banner

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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    size = 'size_example' # str | Size of the banner (optional)

    try:
        # Get banner
        api_response = api_instance.find_banner_by_project_id(x_tenant, project_id, size=size)
        print("The response of ProjectApi->find_banner_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->find_banner_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **size** | **str**| Size of the banner | [optional] 

### Return type

**bytearray**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_jobs_by_project_id**
> List[Job] find_jobs_by_project_id(x_tenant, project_id, type=type)

Retrieve all jobs for a project

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.job import Job
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    type = 'type_example' # str |  (optional)

    try:
        # Retrieve all jobs for a project
        api_response = api_instance.find_jobs_by_project_id(x_tenant, project_id, type=type)
        print("The response of ProjectApi->find_jobs_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->find_jobs_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **type** | **str**|  | [optional] 

### Return type

[**List[Job]**](Job.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.job+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_latest_runs_by_project_id**
> List[RunWithJob] find_latest_runs_by_project_id(x_tenant, project_id, number)

Retrieve all jobs for a project

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.run_with_job import RunWithJob
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    number = 56 # int | Number of runs

    try:
        # Retrieve all jobs for a project
        api_response = api_instance.find_latest_runs_by_project_id(x_tenant, project_id, number)
        print("The response of ProjectApi->find_latest_runs_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->find_latest_runs_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **number** | **int**| Number of runs | 

### Return type

[**List[RunWithJob]**](RunWithJob.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.jobrun-with-job+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_project_by_id**
> Project find_project_by_id(x_tenant, project_id)

Find project by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.project import Project
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project

    try:
        # Find project by Id
        api_response = api_instance.find_project_by_id(x_tenant, project_id)
        print("The response of ProjectApi->find_project_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->find_project_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 

### Return type

[**Project**](Project.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.project+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_projects**
> List[Project] find_projects(x_tenant)

Retrieve all projects

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.project import Project
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all projects
        api_response = api_instance.find_projects(x_tenant)
        print("The response of ProjectApi->find_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->find_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Project]**](Project.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.project+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workflows_by_project_id**
> List[Workflow] find_workflows_by_project_id(x_tenant, project_id)

Retrieve all workflows for a project

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.workflow import Workflow
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project

    try:
        # Retrieve all workflows for a project
        api_response = api_instance.find_workflows_by_project_id(x_tenant, project_id)
        print("The response of ProjectApi->find_workflows_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->find_workflows_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 

### Return type

[**List[Workflow]**](Workflow.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.workflow+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_for_project**
> List[Metric] get_metrics_for_project(x_tenant, project_id, metric, var_from=var_from, to=to)

Find the metrics for a project

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.metric import Metric
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    metric = 'metric_example' # str | The metric name
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Find the metrics for a project
        api_response = api_instance.get_metrics_for_project(x_tenant, project_id, metric, var_from=var_from, to=to)
        print("The response of ProjectApi->get_metrics_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_metrics_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **metric** | **str**| The metric name | 
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 

### Return type

[**List[Metric]**](Metric.md)

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
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_by_project_id**
> RunStats get_stats_by_project_id(x_tenant, project_id)

Find the stats for a project

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.run_stats import RunStats
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project

    try:
        # Find the stats for a project
        api_response = api_instance.get_stats_by_project_id(x_tenant, project_id)
        print("The response of ProjectApi->get_stats_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_stats_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 

### Return type

[**RunStats**](RunStats.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.stats+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(x_tenant, project_id, patch)

Update a project

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.patch import Patch
from graalsystems.models.project import Project
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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a project
        api_response = api_instance.update_project(x_tenant, project_id, patch)
        print("The response of ProjectApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Project**](Project.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.project+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_banner**
> upload_banner(x_tenant, project_id, filename=filename)

Upload a new banner

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
    api_instance = graalsystems.ProjectApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    project_id = 'project_id_example' # str | Id of the project
    filename = None # List[bytearray] |  (optional)

    try:
        # Upload a new banner
        api_instance.upload_banner(x_tenant, project_id, filename=filename)
    except Exception as e:
        print("Exception when calling ProjectApi->upload_banner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **project_id** | **str**| Id of the project | 
 **filename** | **List[bytearray]**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

