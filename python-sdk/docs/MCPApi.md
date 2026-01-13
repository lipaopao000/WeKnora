# weknora.MCPApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mcp_services_get**](MCPApi.md#mcp_services_get) | **GET** /mcp-services | 获取MCP服务列表
[**mcp_services_id_delete**](MCPApi.md#mcp_services_id_delete) | **DELETE** /mcp-services/{id} | 删除MCP服务
[**mcp_services_id_get**](MCPApi.md#mcp_services_id_get) | **GET** /mcp-services/{id} | 获取MCP服务详情
[**mcp_services_id_put**](MCPApi.md#mcp_services_id_put) | **PUT** /mcp-services/{id} | 更新MCP服务
[**mcp_services_id_resources_get**](MCPApi.md#mcp_services_id_resources_get) | **GET** /mcp-services/{id}/resources | 获取MCP服务资源列表
[**mcp_services_id_test_post**](MCPApi.md#mcp_services_id_test_post) | **POST** /mcp-services/{id}/test | 测试MCP服务连接
[**mcp_services_id_tools_get**](MCPApi.md#mcp_services_id_tools_get) | **GET** /mcp-services/{id}/tools | 获取MCP服务工具列表
[**mcp_services_post**](MCPApi.md#mcp_services_post) | **POST** /mcp-services | 创建MCP服务


# **mcp_services_get**
> Dict[str, object] mcp_services_get()

获取MCP服务列表

获取当前租户的所有MCP服务

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.MCPApi(api_client)

    try:
        # 获取MCP服务列表
        api_response = api_instance.mcp_services_get()
        print("The response of MCPApi->mcp_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->mcp_services_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MCP服务列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mcp_services_id_delete**
> Dict[str, object] mcp_services_id_delete(id)

删除MCP服务

删除指定的MCP服务

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.MCPApi(api_client)
    id = 'id_example' # str | MCP服务ID

    try:
        # 删除MCP服务
        api_response = api_instance.mcp_services_id_delete(id)
        print("The response of MCPApi->mcp_services_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->mcp_services_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| MCP服务ID | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 删除成功 |  -  |
**500** | 服务器错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mcp_services_id_get**
> Dict[str, object] mcp_services_id_get(id)

获取MCP服务详情

根据ID获取MCP服务详情

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.MCPApi(api_client)
    id = 'id_example' # str | MCP服务ID

    try:
        # 获取MCP服务详情
        api_response = api_instance.mcp_services_id_get(id)
        print("The response of MCPApi->mcp_services_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->mcp_services_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| MCP服务ID | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MCP服务详情 |  -  |
**404** | 服务不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mcp_services_id_put**
> Dict[str, object] mcp_services_id_put(id, request)

更新MCP服务

更新MCP服务配置

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.MCPApi(api_client)
    id = 'id_example' # str | MCP服务ID
    request = None # object | 更新字段

    try:
        # 更新MCP服务
        api_response = api_instance.mcp_services_id_put(id, request)
        print("The response of MCPApi->mcp_services_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->mcp_services_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| MCP服务ID | 
 **request** | **object**| 更新字段 | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 更新后的MCP服务 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mcp_services_id_resources_get**
> Dict[str, object] mcp_services_id_resources_get(id)

获取MCP服务资源列表

获取MCP服务提供的资源列表

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.MCPApi(api_client)
    id = 'id_example' # str | MCP服务ID

    try:
        # 获取MCP服务资源列表
        api_response = api_instance.mcp_services_id_resources_get(id)
        print("The response of MCPApi->mcp_services_id_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->mcp_services_id_resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| MCP服务ID | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 资源列表 |  -  |
**500** | 服务器错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mcp_services_id_test_post**
> Dict[str, object] mcp_services_id_test_post(id)

测试MCP服务连接

测试MCP服务是否可以正常连接

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.MCPApi(api_client)
    id = 'id_example' # str | MCP服务ID

    try:
        # 测试MCP服务连接
        api_response = api_instance.mcp_services_id_test_post(id)
        print("The response of MCPApi->mcp_services_id_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->mcp_services_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| MCP服务ID | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 测试结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mcp_services_id_tools_get**
> Dict[str, object] mcp_services_id_tools_get(id)

获取MCP服务工具列表

获取MCP服务提供的工具列表

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.MCPApi(api_client)
    id = 'id_example' # str | MCP服务ID

    try:
        # 获取MCP服务工具列表
        api_response = api_instance.mcp_services_id_tools_get(id)
        print("The response of MCPApi->mcp_services_id_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->mcp_services_id_tools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| MCP服务ID | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 工具列表 |  -  |
**500** | 服务器错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mcp_services_post**
> Dict[str, object] mcp_services_post(request)

创建MCP服务

创建新的MCP服务配置

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.models.github_com_tencent_we_knora_internal_types_mcp_service import GithubComTencentWeKnoraInternalTypesMCPService
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.MCPApi(api_client)
    request = weknora.GithubComTencentWeKnoraInternalTypesMCPService() # GithubComTencentWeKnoraInternalTypesMCPService | MCP服务配置

    try:
        # 创建MCP服务
        api_response = api_instance.mcp_services_post(request)
        print("The response of MCPApi->mcp_services_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->mcp_services_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GithubComTencentWeKnoraInternalTypesMCPService**](GithubComTencentWeKnoraInternalTypesMCPService.md)| MCP服务配置 | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 创建的MCP服务 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

