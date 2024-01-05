# graalsystems.TicketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ticket**](TicketApi.md#create_ticket) | **POST** /tickets | Create a ticket
[**delete_ticket_by_id**](TicketApi.md#delete_ticket_by_id) | **DELETE** /tickets/{ticketId} | Delete a ticket by its id
[**execute_action1**](TicketApi.md#execute_action1) | **POST** /tickets/{ticketId}/actions | Execute an action
[**find_ticket_by_id**](TicketApi.md#find_ticket_by_id) | **GET** /tickets/{ticketId} | Find ticket by Id
[**find_tickets**](TicketApi.md#find_tickets) | **GET** /tickets | Retrieve all tickets
[**update_ticket**](TicketApi.md#update_ticket) | **PATCH** /tickets/{ticketId} | Update a ticket


# **create_ticket**
> Ticket create_ticket(ticket, x_tenant=x_tenant, challenge=challenge)

Create a ticket

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.ticket import Ticket
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
    api_instance = graalsystems.TicketApi(api_client)
    ticket = graalsystems.Ticket() # Ticket | The ticket to be created
    x_tenant = 'x_tenant_example' # str |  (optional)
    challenge = 'challenge_example' # str |  (optional)

    try:
        # Create a ticket
        api_response = api_instance.create_ticket(ticket, x_tenant=x_tenant, challenge=challenge)
        print("The response of TicketApi->create_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->create_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket** | [**Ticket**](Ticket.md)| The ticket to be created | 
 **x_tenant** | **str**|  | [optional] 
 **challenge** | **str**|  | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.ticket+json
 - **Accept**: application/vnd.graal.systems.v1.ticket+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ticket_by_id**
> delete_ticket_by_id(x_tenant, ticket_id)

Delete a ticket by its id

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
    api_instance = graalsystems.TicketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    ticket_id = 'ticket_id_example' # str | Id of the Ticket

    try:
        # Delete a ticket by its id
        api_instance.delete_ticket_by_id(x_tenant, ticket_id)
    except Exception as e:
        print("Exception when calling TicketApi->delete_ticket_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **ticket_id** | **str**| Id of the Ticket | 

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
**404** | Ticket not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_action1**
> execute_action1(x_tenant, ticket_id, action)

Execute an action

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.action import Action
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
    api_instance = graalsystems.TicketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    ticket_id = 'ticket_id_example' # str | Id of the ticket
    action = graalsystems.Action() # Action | 

    try:
        # Execute an action
        api_instance.execute_action1(x_tenant, ticket_id, action)
    except Exception as e:
        print("Exception when calling TicketApi->execute_action1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **ticket_id** | **str**| Id of the ticket | 
 **action** | [**Action**](Action.md)|  | 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.action+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ticket_by_id**
> Ticket find_ticket_by_id(x_tenant, ticket_id)

Find ticket by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.ticket import Ticket
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
    api_instance = graalsystems.TicketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    ticket_id = 'ticket_id_example' # str | Id of the ticket

    try:
        # Find ticket by Id
        api_response = api_instance.find_ticket_by_id(x_tenant, ticket_id)
        print("The response of TicketApi->find_ticket_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->find_ticket_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **ticket_id** | **str**| Id of the ticket | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.ticket+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Ticket not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tickets**
> List[Ticket] find_tickets(x_tenant)

Retrieve all tickets

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.ticket import Ticket
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
    api_instance = graalsystems.TicketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all tickets
        api_response = api_instance.find_tickets(x_tenant)
        print("The response of TicketApi->find_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->find_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Ticket]**](Ticket.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.ticket+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ticket**
> Ticket update_ticket(x_tenant, ticket_id, patch)

Update a ticket

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.patch import Patch
from graalsystems.models.ticket import Ticket
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
    api_instance = graalsystems.TicketApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    ticket_id = 'ticket_id_example' # str | Id of the Ticket
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a ticket
        api_response = api_instance.update_ticket(x_tenant, ticket_id, patch)
        print("The response of TicketApi->update_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->update_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **ticket_id** | **str**| Id of the Ticket | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.ticket+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Ticket not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

