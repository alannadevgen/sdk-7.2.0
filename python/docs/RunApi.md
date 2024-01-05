# graalsystems.RunApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_run_for_job**](RunApi.md#create_run_for_job) | **POST** /jobs/{jobId}/runs | Create a run for a job
[**create_run_for_workflow**](RunApi.md#create_run_for_workflow) | **POST** /workflows/{workflowId}/runs | Create a run for a workflow
[**delete_run_by_job_id_and_run_id**](RunApi.md#delete_run_by_job_id_and_run_id) | **DELETE** /jobs/{jobId}/runs/{runId} | Delete a run by a jobId and a runId
[**delete_run_by_workflow_id_and_run_id**](RunApi.md#delete_run_by_workflow_id_and_run_id) | **DELETE** /workflows/{workflowId}/runs/{runId} | Delete a run by a workflowId and a runId
[**find_latest_runs**](RunApi.md#find_latest_runs) | **GET** /runs | Find the latest runs
[**find_run_by_job_id_and_run_id**](RunApi.md#find_run_by_job_id_and_run_id) | **GET** /jobs/{jobId}/runs/{runId} | Find the run by a jobId and a runId
[**find_runs_by_job_id**](RunApi.md#find_runs_by_job_id) | **GET** /jobs/{jobId}/runs | Find the runs for a job
[**find_runs_by_workflow_id**](RunApi.md#find_runs_by_workflow_id) | **GET** /workflows/{workflowId}/runs | Find the runs for a workflow
[**get_file**](RunApi.md#get_file) | **GET** /jobs/{jobId}/runs/{runId}/files/{filename} | Get file
[**get_logs**](RunApi.md#get_logs) | **GET** /jobs/{jobId}/runs/{runId}/logs | Get logs
[**get_metrics_for_run**](RunApi.md#get_metrics_for_run) | **GET** /jobs/{jobId}/runs/{runId}/metrics | Find the metrics for a run
[**get_run_files**](RunApi.md#get_run_files) | **GET** /jobs/{jobId}/runs/{runId}/files | Get files
[**update_run**](RunApi.md#update_run) | **PATCH** /jobs/{jobId}/runs/{runId} | Update a run


# **create_run_for_job**
> JobRun create_run_for_job(x_tenant, job_id, job_run)

Create a run for a job

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.job_run import JobRun
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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job
    job_run = graalsystems.JobRun() # JobRun | The run to be created

    try:
        # Create a run for a job
        api_response = api_instance.create_run_for_job(x_tenant, job_id, job_run)
        print("The response of RunApi->create_run_for_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->create_run_for_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 
 **job_run** | [**JobRun**](JobRun.md)| The run to be created | 

### Return type

[**JobRun**](JobRun.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.jobrun+json
 - **Accept**: application/vnd.graal.systems.v1.jobrun+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_run_for_workflow**
> Workflow create_run_for_workflow(x_tenant, workflow_id, workflow_run)

Create a run for a workflow

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.workflow import Workflow
from graalsystems.models.workflow_run import WorkflowRun
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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workflow_id = 'workflow_id_example' # str | Id of the Workflow
    workflow_run = graalsystems.WorkflowRun() # WorkflowRun | The run to be created

    try:
        # Create a run for a workflow
        api_response = api_instance.create_run_for_workflow(x_tenant, workflow_id, workflow_run)
        print("The response of RunApi->create_run_for_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->create_run_for_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workflow_id** | **str**| Id of the Workflow | 
 **workflow_run** | [**WorkflowRun**](WorkflowRun.md)| The run to be created | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.workflowrun+json
 - **Accept**: application/vnd.graal.systems.v1.workflowrun+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Workflow not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_run_by_job_id_and_run_id**
> delete_run_by_job_id_and_run_id(x_tenant, job_id, run_id)

Delete a run by a jobId and a runId

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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job
    run_id = 'run_id_example' # str | Id of the Run

    try:
        # Delete a run by a jobId and a runId
        api_instance.delete_run_by_job_id_and_run_id(x_tenant, job_id, run_id)
    except Exception as e:
        print("Exception when calling RunApi->delete_run_by_job_id_and_run_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 
 **run_id** | **str**| Id of the Run | 

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
**404** | Run not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_run_by_workflow_id_and_run_id**
> delete_run_by_workflow_id_and_run_id(x_tenant, workflow_id, run_id)

Delete a run by a workflowId and a runId

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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workflow_id = 'workflow_id_example' # str | Id of the Workflow
    run_id = 'run_id_example' # str | Id of the Run

    try:
        # Delete a run by a workflowId and a runId
        api_instance.delete_run_by_workflow_id_and_run_id(x_tenant, workflow_id, run_id)
    except Exception as e:
        print("Exception when calling RunApi->delete_run_by_workflow_id_and_run_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workflow_id** | **str**| Id of the Workflow | 
 **run_id** | **str**| Id of the Run | 

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
**404** | Run not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_latest_runs**
> List[RunWithJob] find_latest_runs(x_tenant, number)

Find the latest runs

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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    number = 56 # int | Number of runs

    try:
        # Find the latest runs
        api_response = api_instance.find_latest_runs(x_tenant, number)
        print("The response of RunApi->find_latest_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->find_latest_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **number** | **int**| Number of runs | 

### Return type

[**List[RunWithJob]**](RunWithJob.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.jobrun-with-job+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_run_by_job_id_and_run_id**
> JobRun find_run_by_job_id_and_run_id(x_tenant, job_id, run_id)

Find the run by a jobId and a runId

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.job_run import JobRun
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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job
    run_id = 'run_id_example' # str | Id of the Run

    try:
        # Find the run by a jobId and a runId
        api_response = api_instance.find_run_by_job_id_and_run_id(x_tenant, job_id, run_id)
        print("The response of RunApi->find_run_by_job_id_and_run_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->find_run_by_job_id_and_run_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 
 **run_id** | **str**| Id of the Run | 

### Return type

[**JobRun**](JobRun.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.jobrun+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Run of job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_runs_by_job_id**
> List[JobRun] find_runs_by_job_id(x_tenant, job_id)

Find the runs for a job

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.job_run import JobRun
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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job

    try:
        # Find the runs for a job
        api_response = api_instance.find_runs_by_job_id(x_tenant, job_id)
        print("The response of RunApi->find_runs_by_job_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->find_runs_by_job_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 

### Return type

[**List[JobRun]**](JobRun.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.jobrun+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_runs_by_workflow_id**
> List[WorkflowRun] find_runs_by_workflow_id(x_tenant, workflow_id)

Find the runs for a workflow

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.workflow_run import WorkflowRun
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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    workflow_id = 'workflow_id_example' # str | Id of the Workflow

    try:
        # Find the runs for a workflow
        api_response = api_instance.find_runs_by_workflow_id(x_tenant, workflow_id)
        print("The response of RunApi->find_runs_by_workflow_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->find_runs_by_workflow_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **workflow_id** | **str**| Id of the Workflow | 

### Return type

[**List[WorkflowRun]**](WorkflowRun.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.workflowrun+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Workflow not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> bytearray get_file(x_tenant, job_id, run_id, filename)

Get file

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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job
    run_id = 'run_id_example' # str | Id of the Run
    filename = 'filename_example' # str | Name of the file

    try:
        # Get file
        api_response = api_instance.get_file(x_tenant, job_id, run_id, filename)
        print("The response of RunApi->get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->get_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 
 **run_id** | **str**| Id of the Run | 
 **filename** | **str**| Name of the file | 

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
**404** | Run of job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> List[LogEntry] get_logs(x_tenant, job_id, run_id, cursor=cursor)

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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job
    run_id = 'run_id_example' # str | Id of the Run
    cursor = 'cursor_example' # str | The cursor (optional)

    try:
        # Get logs
        api_response = api_instance.get_logs(x_tenant, job_id, run_id, cursor=cursor)
        print("The response of RunApi->get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->get_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 
 **run_id** | **str**| Id of the Run | 
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

# **get_metrics_for_run**
> List[Metric] get_metrics_for_run(x_tenant, job_id, run_id, metric, var_from=var_from, to=to)

Find the metrics for a run

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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job
    run_id = 'run_id_example' # str | Id of the Run
    metric = 'metric_example' # str | The metric name
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Find the metrics for a run
        api_response = api_instance.get_metrics_for_run(x_tenant, job_id, run_id, metric, var_from=var_from, to=to)
        print("The response of RunApi->get_metrics_for_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->get_metrics_for_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 
 **run_id** | **str**| Id of the Run | 
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
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_files**
> List[str] get_run_files(x_tenant, job_id, run_id)

Get files

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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job
    run_id = 'run_id_example' # str | Id of the Run

    try:
        # Get files
        api_response = api_instance.get_run_files(x_tenant, job_id, run_id)
        print("The response of RunApi->get_run_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->get_run_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 
 **run_id** | **str**| Id of the Run | 

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
**404** | Run of job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run**
> JobRun update_run(x_tenant, job_id, run_id, patch)

Update a run

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.job_run import JobRun
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
    api_instance = graalsystems.RunApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    job_id = 'job_id_example' # str | Id of the Job
    run_id = 'run_id_example' # str | Id of the Run
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a run
        api_response = api_instance.update_run(x_tenant, job_id, run_id, patch)
        print("The response of RunApi->update_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->update_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **job_id** | **str**| Id of the Job | 
 **run_id** | **str**| Id of the Run | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**JobRun**](JobRun.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.jobrun+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

