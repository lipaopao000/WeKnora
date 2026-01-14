# weknora_sdk.DefaultApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_change_password_post**](DefaultApi.md#auth_change_password_post) | **POST** /auth/change-password | 修改密码
[**auth_login_post**](DefaultApi.md#auth_login_post) | **POST** /auth/login | 用户登录
[**auth_logout_post**](DefaultApi.md#auth_logout_post) | **POST** /auth/logout | 用户登出
[**auth_me_get**](DefaultApi.md#auth_me_get) | **GET** /auth/me | 获取当前用户信息
[**auth_refresh_post**](DefaultApi.md#auth_refresh_post) | **POST** /auth/refresh | 刷新令牌
[**auth_register_post**](DefaultApi.md#auth_register_post) | **POST** /auth/register | 用户注册
[**auth_validate_get**](DefaultApi.md#auth_validate_get) | **GET** /auth/validate | 验证令牌
[**chunks_by_id_id_get**](DefaultApi.md#chunks_by_id_id_get) | **GET** /chunks/by-id/{id} | 通过ID获取分块
[**chunks_by_id_id_questions_delete**](DefaultApi.md#chunks_by_id_id_questions_delete) | **DELETE** /chunks/by-id/{id}/questions | 删除生成的问题
[**chunks_knowledge_id_delete**](DefaultApi.md#chunks_knowledge_id_delete) | **DELETE** /chunks/{knowledge_id} | 删除知识下所有分块
[**chunks_knowledge_id_get**](DefaultApi.md#chunks_knowledge_id_get) | **GET** /chunks/{knowledge_id} | 获取知识分块列表
[**chunks_knowledge_id_id_delete**](DefaultApi.md#chunks_knowledge_id_id_delete) | **DELETE** /chunks/{knowledge_id}/{id} | 删除分块
[**chunks_knowledge_id_id_put**](DefaultApi.md#chunks_knowledge_id_id_put) | **PUT** /chunks/{knowledge_id}/{id} | 更新分块
[**evaluation_get**](DefaultApi.md#evaluation_get) | **GET** /evaluation/ | 获取评估结果
[**evaluation_post**](DefaultApi.md#evaluation_post) | **POST** /evaluation/ | 执行评估
[**initialization_extract_relations_post**](DefaultApi.md#initialization_extract_relations_post) | **POST** /initialization/extract/relations | 提取文本关系
[**initialization_fabri_tag_get**](DefaultApi.md#initialization_fabri_tag_get) | **GET** /initialization/fabri/tag | 生成随机标签
[**initialization_fabri_text_post**](DefaultApi.md#initialization_fabri_text_post) | **POST** /initialization/fabri/text | 生成示例文本
[**initialization_kb_kb_id_config_get**](DefaultApi.md#initialization_kb_kb_id_config_get) | **GET** /initialization/kb/{kbId}/config | 获取知识库配置
[**initialization_kb_kb_id_config_put**](DefaultApi.md#initialization_kb_kb_id_config_put) | **PUT** /initialization/kb/{kbId}/config | 更新知识库配置
[**initialization_kb_kb_id_post**](DefaultApi.md#initialization_kb_kb_id_post) | **POST** /initialization/kb/{kbId} | 初始化知识库配置
[**initialization_models_embedding_test_post**](DefaultApi.md#initialization_models_embedding_test_post) | **POST** /initialization/models/embedding/test | 测试Embedding模型
[**initialization_models_remote_check_post**](DefaultApi.md#initialization_models_remote_check_post) | **POST** /initialization/models/remote/check | 检查远程模型
[**initialization_models_rerank_check_post**](DefaultApi.md#initialization_models_rerank_check_post) | **POST** /initialization/models/rerank/check | 检查Rerank模型
[**initialization_multimodal_test_post**](DefaultApi.md#initialization_multimodal_test_post) | **POST** /initialization/multimodal/test | 测试多模态功能
[**initialization_ollama_download_task_id_get**](DefaultApi.md#initialization_ollama_download_task_id_get) | **GET** /initialization/ollama/download/{taskId} | 获取下载进度
[**initialization_ollama_download_tasks_get**](DefaultApi.md#initialization_ollama_download_tasks_get) | **GET** /initialization/ollama/download/tasks | 列出下载任务
[**initialization_ollama_models_check_post**](DefaultApi.md#initialization_ollama_models_check_post) | **POST** /initialization/ollama/models/check | 检查Ollama模型状态
[**initialization_ollama_models_download_post**](DefaultApi.md#initialization_ollama_models_download_post) | **POST** /initialization/ollama/models/download | 下载Ollama模型
[**initialization_ollama_models_get**](DefaultApi.md#initialization_ollama_models_get) | **GET** /initialization/ollama/models | 列出Ollama模型
[**initialization_ollama_status_get**](DefaultApi.md#initialization_ollama_status_get) | **GET** /initialization/ollama/status | 检查Ollama服务状态
[**knowledge_bases_copy_post**](DefaultApi.md#knowledge_bases_copy_post) | **POST** /knowledge-bases/copy | 复制知识库
[**knowledge_bases_copy_progress_task_id_get**](DefaultApi.md#knowledge_bases_copy_progress_task_id_get) | **GET** /knowledge-bases/copy/progress/{task_id} | 获取知识库复制进度
[**knowledge_bases_get**](DefaultApi.md#knowledge_bases_get) | **GET** /knowledge-bases | 获取知识库列表
[**knowledge_bases_id_delete**](DefaultApi.md#knowledge_bases_id_delete) | **DELETE** /knowledge-bases/{id} | 删除知识库
[**knowledge_bases_id_get**](DefaultApi.md#knowledge_bases_id_get) | **GET** /knowledge-bases/{id} | 获取知识库详情
[**knowledge_bases_id_hybrid_search_get**](DefaultApi.md#knowledge_bases_id_hybrid_search_get) | **GET** /knowledge-bases/{id}/hybrid-search | 混合搜索
[**knowledge_bases_id_knowledge_file_post**](DefaultApi.md#knowledge_bases_id_knowledge_file_post) | **POST** /knowledge-bases/{id}/knowledge/file | 从文件创建知识
[**knowledge_bases_id_knowledge_get**](DefaultApi.md#knowledge_bases_id_knowledge_get) | **GET** /knowledge-bases/{id}/knowledge | 获取知识列表
[**knowledge_bases_id_knowledge_manual_post**](DefaultApi.md#knowledge_bases_id_knowledge_manual_post) | **POST** /knowledge-bases/{id}/knowledge/manual | 手工创建知识
[**knowledge_bases_id_knowledge_url_post**](DefaultApi.md#knowledge_bases_id_knowledge_url_post) | **POST** /knowledge-bases/{id}/knowledge/url | 从URL创建知识
[**knowledge_bases_id_put**](DefaultApi.md#knowledge_bases_id_put) | **PUT** /knowledge-bases/{id} | 更新知识库
[**knowledge_bases_id_tags_get**](DefaultApi.md#knowledge_bases_id_tags_get) | **GET** /knowledge-bases/{id}/tags | 获取标签列表
[**knowledge_bases_id_tags_post**](DefaultApi.md#knowledge_bases_id_tags_post) | **POST** /knowledge-bases/{id}/tags | 创建标签
[**knowledge_bases_id_tags_tag_id_delete**](DefaultApi.md#knowledge_bases_id_tags_tag_id_delete) | **DELETE** /knowledge-bases/{id}/tags/{tag_id} | 删除标签
[**knowledge_bases_id_tags_tag_id_put**](DefaultApi.md#knowledge_bases_id_tags_tag_id_put) | **PUT** /knowledge-bases/{id}/tags/{tag_id} | 更新标签
[**knowledge_bases_post**](DefaultApi.md#knowledge_bases_post) | **POST** /knowledge-bases | 创建知识库
[**knowledge_batch_get**](DefaultApi.md#knowledge_batch_get) | **GET** /knowledge/batch | 批量获取知识
[**knowledge_id_delete**](DefaultApi.md#knowledge_id_delete) | **DELETE** /knowledge/{id} | 删除知识
[**knowledge_id_download_get**](DefaultApi.md#knowledge_id_download_get) | **GET** /knowledge/{id}/download | 下载知识文件
[**knowledge_id_get**](DefaultApi.md#knowledge_id_get) | **GET** /knowledge/{id} | 获取知识详情
[**knowledge_id_put**](DefaultApi.md#knowledge_id_put) | **PUT** /knowledge/{id} | 更新知识
[**knowledge_image_id_chunk_id_put**](DefaultApi.md#knowledge_image_id_chunk_id_put) | **PUT** /knowledge/image/{id}/{chunk_id} | 更新图像信息
[**knowledge_manual_id_put**](DefaultApi.md#knowledge_manual_id_put) | **PUT** /knowledge/manual/{id} | 更新手工知识
[**knowledge_tags_put**](DefaultApi.md#knowledge_tags_put) | **PUT** /knowledge/tags | 批量更新知识标签
[**messages_session_id_id_delete**](DefaultApi.md#messages_session_id_id_delete) | **DELETE** /messages/{session_id}/{id} | 删除消息
[**messages_session_id_load_get**](DefaultApi.md#messages_session_id_load_get) | **GET** /messages/{session_id}/load | 加载消息历史
[**models_get**](DefaultApi.md#models_get) | **GET** /models | 获取模型列表
[**models_id_delete**](DefaultApi.md#models_id_delete) | **DELETE** /models/{id} | 删除模型
[**models_id_get**](DefaultApi.md#models_id_get) | **GET** /models/{id} | 获取模型详情
[**models_id_put**](DefaultApi.md#models_id_put) | **PUT** /models/{id} | 更新模型
[**models_post**](DefaultApi.md#models_post) | **POST** /models | 创建模型
[**sessions_get**](DefaultApi.md#sessions_get) | **GET** /sessions | 获取会话列表
[**sessions_id_delete**](DefaultApi.md#sessions_id_delete) | **DELETE** /sessions/{id} | 删除会话
[**sessions_id_get**](DefaultApi.md#sessions_id_get) | **GET** /sessions/{id} | 获取会话详情
[**sessions_id_put**](DefaultApi.md#sessions_id_put) | **PUT** /sessions/{id} | 更新会话
[**sessions_post**](DefaultApi.md#sessions_post) | **POST** /sessions | 创建会话
[**sessions_search_post**](DefaultApi.md#sessions_search_post) | **POST** /sessions/search | 知识搜索
[**sessions_session_id_agent_qa_post**](DefaultApi.md#sessions_session_id_agent_qa_post) | **POST** /sessions/{session_id}/agent-qa | Agent问答
[**sessions_session_id_continue_get**](DefaultApi.md#sessions_session_id_continue_get) | **GET** /sessions/{session_id}/continue | 继续流式响应
[**sessions_session_id_knowledge_qa_post**](DefaultApi.md#sessions_session_id_knowledge_qa_post) | **POST** /sessions/{session_id}/knowledge-qa | 知识问答
[**sessions_session_id_stop_post**](DefaultApi.md#sessions_session_id_stop_post) | **POST** /sessions/{session_id}/stop | 停止生成
[**sessions_session_id_title_post**](DefaultApi.md#sessions_session_id_title_post) | **POST** /sessions/{session_id}/title | 生成会话标题
[**system_info_get**](DefaultApi.md#system_info_get) | **GET** /system/info | 获取系统信息
[**tenants_all_get**](DefaultApi.md#tenants_all_get) | **GET** /tenants/all | 获取所有租户列表
[**tenants_get**](DefaultApi.md#tenants_get) | **GET** /tenants | 获取租户列表
[**tenants_id_delete**](DefaultApi.md#tenants_id_delete) | **DELETE** /tenants/{id} | 删除租户
[**tenants_id_get**](DefaultApi.md#tenants_id_get) | **GET** /tenants/{id} | 获取租户详情
[**tenants_id_put**](DefaultApi.md#tenants_id_put) | **PUT** /tenants/{id} | 更新租户
[**tenants_kv_agent_config_get**](DefaultApi.md#tenants_kv_agent_config_get) | **GET** /tenants/kv/agent-config | 获取租户Agent配置
[**tenants_kv_conversation_config_get**](DefaultApi.md#tenants_kv_conversation_config_get) | **GET** /tenants/kv/conversation-config | 获取租户对话配置
[**tenants_kv_key_get**](DefaultApi.md#tenants_kv_key_get) | **GET** /tenants/kv/{key} | 获取租户KV配置
[**tenants_kv_key_put**](DefaultApi.md#tenants_kv_key_put) | **PUT** /tenants/kv/{key} | 更新租户KV配置
[**tenants_kv_web_search_config_get**](DefaultApi.md#tenants_kv_web_search_config_get) | **GET** /tenants/kv/web-search-config | 获取租户网络搜索配置
[**tenants_post**](DefaultApi.md#tenants_post) | **POST** /tenants | 创建租户
[**tenants_search_get**](DefaultApi.md#tenants_search_get) | **GET** /tenants/search | 搜索租户


# **auth_change_password_post**
> Dict[str, object] auth_change_password_post(request)

修改密码

修改当前用户的登录密码

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.auth_change_password_post_request import AuthChangePasswordPostRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.AuthChangePasswordPostRequest() # AuthChangePasswordPostRequest | 密码修改请求

    try:
        # 修改密码
        api_response = api_instance.auth_change_password_post(request)
        print("The response of DefaultApi->auth_change_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_change_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AuthChangePasswordPostRequest**](AuthChangePasswordPostRequest.md)| 密码修改请求 | 

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 修改成功 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_login_post**
> GithubComTencentWeKnoraInternalTypesLoginResponse auth_login_post(request)

用户登录

用户登录并获取访问令牌

### Example


```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_login_request import GithubComTencentWeKnoraInternalTypesLoginRequest
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_login_response import GithubComTencentWeKnoraInternalTypesLoginResponse
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesLoginRequest() # GithubComTencentWeKnoraInternalTypesLoginRequest | 登录请求参数

    try:
        # 用户登录
        api_response = api_instance.auth_login_post(request)
        print("The response of DefaultApi->auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GithubComTencentWeKnoraInternalTypesLoginRequest**](GithubComTencentWeKnoraInternalTypesLoginRequest.md)| 登录请求参数 | 

### Return type

[**GithubComTencentWeKnoraInternalTypesLoginResponse**](GithubComTencentWeKnoraInternalTypesLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | 认证失败 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_logout_post**
> Dict[str, object] auth_logout_post()

用户登出

撤销当前访问令牌并登出

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 用户登出
        api_response = api_instance.auth_logout_post()
        print("The response of DefaultApi->auth_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_logout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 登出成功 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_me_get**
> Dict[str, object] auth_me_get()

获取当前用户信息

获取当前登录用户的详细信息

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取当前用户信息
        api_response = api_instance.auth_me_get()
        print("The response of DefaultApi->auth_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 用户信息 |  -  |
**401** | 未授权 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_refresh_post**
> Dict[str, object] auth_refresh_post(request)

刷新令牌

使用刷新令牌获取新的访问令牌

### Example


```python
import weknora_sdk
from weknora_sdk.models.auth_refresh_post_request import AuthRefreshPostRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.AuthRefreshPostRequest() # AuthRefreshPostRequest | 刷新令牌

    try:
        # 刷新令牌
        api_response = api_instance.auth_refresh_post(request)
        print("The response of DefaultApi->auth_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AuthRefreshPostRequest**](AuthRefreshPostRequest.md)| 刷新令牌 | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 新令牌 |  -  |
**401** | 令牌无效 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_register_post**
> GithubComTencentWeKnoraInternalTypesRegisterResponse auth_register_post(request)

用户注册

注册新用户账号

### Example


```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_register_request import GithubComTencentWeKnoraInternalTypesRegisterRequest
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_register_response import GithubComTencentWeKnoraInternalTypesRegisterResponse
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesRegisterRequest() # GithubComTencentWeKnoraInternalTypesRegisterRequest | 注册请求参数

    try:
        # 用户注册
        api_response = api_instance.auth_register_post(request)
        print("The response of DefaultApi->auth_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GithubComTencentWeKnoraInternalTypesRegisterRequest**](GithubComTencentWeKnoraInternalTypesRegisterRequest.md)| 注册请求参数 | 

### Return type

[**GithubComTencentWeKnoraInternalTypesRegisterResponse**](GithubComTencentWeKnoraInternalTypesRegisterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | 请求参数错误 |  -  |
**403** | 注册功能已禁用 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_validate_get**
> Dict[str, object] auth_validate_get()

验证令牌

验证访问令牌是否有效

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 验证令牌
        api_response = api_instance.auth_validate_get()
        print("The response of DefaultApi->auth_validate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_validate_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 令牌有效 |  -  |
**401** | 令牌无效 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chunks_by_id_id_get**
> Dict[str, object] chunks_by_id_id_get(id)

通过ID获取分块

仅通过分块ID获取分块详情（不需要knowledge_id）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 分块ID

    try:
        # 通过ID获取分块
        api_response = api_instance.chunks_by_id_id_get(id)
        print("The response of DefaultApi->chunks_by_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chunks_by_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 分块ID | 

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
**200** | 分块详情 |  -  |
**400** | 请求参数错误 |  -  |
**404** | 分块不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chunks_by_id_id_questions_delete**
> Dict[str, object] chunks_by_id_id_questions_delete(id, request)

删除生成的问题

删除分块中生成的问题

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.chunks_by_id_id_questions_delete_request import ChunksByIdIdQuestionsDeleteRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 分块ID
    request = weknora_sdk.ChunksByIdIdQuestionsDeleteRequest() # ChunksByIdIdQuestionsDeleteRequest | 问题ID

    try:
        # 删除生成的问题
        api_response = api_instance.chunks_by_id_id_questions_delete(id, request)
        print("The response of DefaultApi->chunks_by_id_id_questions_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chunks_by_id_id_questions_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 分块ID | 
 **request** | [**ChunksByIdIdQuestionsDeleteRequest**](ChunksByIdIdQuestionsDeleteRequest.md)| 问题ID | 

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
**200** | 删除成功 |  -  |
**400** | 请求参数错误 |  -  |
**404** | 分块不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chunks_knowledge_id_delete**
> Dict[str, object] chunks_knowledge_id_delete(knowledge_id)

删除知识下所有分块

删除指定知识下的所有分块

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    knowledge_id = 'knowledge_id_example' # str | 知识ID

    try:
        # 删除知识下所有分块
        api_response = api_instance.chunks_knowledge_id_delete(knowledge_id)
        print("The response of DefaultApi->chunks_knowledge_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chunks_knowledge_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **knowledge_id** | **str**| 知识ID | 

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
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chunks_knowledge_id_get**
> Dict[str, object] chunks_knowledge_id_get(knowledge_id, page=page, page_size=page_size)

获取知识分块列表

获取指定知识下的所有分块列表，支持分页

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    knowledge_id = 'knowledge_id_example' # str | 知识ID
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 10 # int | 每页数量 (optional) (default to 10)

    try:
        # 获取知识分块列表
        api_response = api_instance.chunks_knowledge_id_get(knowledge_id, page=page, page_size=page_size)
        print("The response of DefaultApi->chunks_knowledge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chunks_knowledge_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **knowledge_id** | **str**| 知识ID | 
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 10]

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
**200** | 分块列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chunks_knowledge_id_id_delete**
> Dict[str, object] chunks_knowledge_id_id_delete(knowledge_id, id)

删除分块

删除指定的分块

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    knowledge_id = 'knowledge_id_example' # str | 知识ID
    id = 'id_example' # str | 分块ID

    try:
        # 删除分块
        api_response = api_instance.chunks_knowledge_id_id_delete(knowledge_id, id)
        print("The response of DefaultApi->chunks_knowledge_id_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chunks_knowledge_id_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **knowledge_id** | **str**| 知识ID | 
 **id** | **str**| 分块ID | 

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
**400** | 请求参数错误 |  -  |
**404** | 分块不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chunks_knowledge_id_id_put**
> Dict[str, object] chunks_knowledge_id_id_put(knowledge_id, id, request)

更新分块

更新指定分块的内容和属性

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_update_chunk_request import InternalHandlerUpdateChunkRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    knowledge_id = 'knowledge_id_example' # str | 知识ID
    id = 'id_example' # str | 分块ID
    request = weknora_sdk.InternalHandlerUpdateChunkRequest() # InternalHandlerUpdateChunkRequest | 更新请求

    try:
        # 更新分块
        api_response = api_instance.chunks_knowledge_id_id_put(knowledge_id, id, request)
        print("The response of DefaultApi->chunks_knowledge_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chunks_knowledge_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **knowledge_id** | **str**| 知识ID | 
 **id** | **str**| 分块ID | 
 **request** | [**InternalHandlerUpdateChunkRequest**](InternalHandlerUpdateChunkRequest.md)| 更新请求 | 

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
**200** | 更新后的分块 |  -  |
**400** | 请求参数错误 |  -  |
**404** | 分块不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluation_get**
> Dict[str, object] evaluation_get(task_id)

获取评估结果

根据任务ID获取评估结果

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    task_id = 'task_id_example' # str | 评估任务ID

    try:
        # 获取评估结果
        api_response = api_instance.evaluation_get(task_id)
        print("The response of DefaultApi->evaluation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->evaluation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| 评估任务ID | 

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
**200** | 评估结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluation_post**
> Dict[str, object] evaluation_post(request)

执行评估

对知识库进行评估测试

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_evaluation_request import InternalHandlerEvaluationRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InternalHandlerEvaluationRequest() # InternalHandlerEvaluationRequest | 评估请求参数

    try:
        # 执行评估
        api_response = api_instance.evaluation_post(request)
        print("The response of DefaultApi->evaluation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->evaluation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalHandlerEvaluationRequest**](InternalHandlerEvaluationRequest.md)| 评估请求参数 | 

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
**200** | 评估任务 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_extract_relations_post**
> Dict[str, object] initialization_extract_relations_post(request)

提取文本关系

从文本中提取实体和关系

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_text_relation_extraction_request import InternalHandlerTextRelationExtractionRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InternalHandlerTextRelationExtractionRequest() # InternalHandlerTextRelationExtractionRequest | 提取请求

    try:
        # 提取文本关系
        api_response = api_instance.initialization_extract_relations_post(request)
        print("The response of DefaultApi->initialization_extract_relations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_extract_relations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalHandlerTextRelationExtractionRequest**](InternalHandlerTextRelationExtractionRequest.md)| 提取请求 | 

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
**200** | 提取结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_fabri_tag_get**
> Dict[str, object] initialization_fabri_tag_get()

生成随机标签

随机生成一组标签

### Example


```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 生成随机标签
        api_response = api_instance.initialization_fabri_tag_get()
        print("The response of DefaultApi->initialization_fabri_tag_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_fabri_tag_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 生成的标签 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_fabri_text_post**
> Dict[str, object] initialization_fabri_text_post(request)

生成示例文本

根据标签生成示例文本

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_fabri_text_request import InternalHandlerFabriTextRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InternalHandlerFabriTextRequest() # InternalHandlerFabriTextRequest | 生成请求

    try:
        # 生成示例文本
        api_response = api_instance.initialization_fabri_text_post(request)
        print("The response of DefaultApi->initialization_fabri_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_fabri_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalHandlerFabriTextRequest**](InternalHandlerFabriTextRequest.md)| 生成请求 | 

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
**200** | 生成的文本 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_kb_kb_id_config_get**
> Dict[str, object] initialization_kb_kb_id_config_get(kb_id)

获取知识库配置

根据知识库ID获取当前配置信息

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    kb_id = 'kb_id_example' # str | 知识库ID

    try:
        # 获取知识库配置
        api_response = api_instance.initialization_kb_kb_id_config_get(kb_id)
        print("The response of DefaultApi->initialization_kb_kb_id_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_kb_kb_id_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**| 知识库ID | 

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
**200** | 配置信息 |  -  |
**404** | 知识库不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_kb_kb_id_config_put**
> Dict[str, object] initialization_kb_kb_id_config_put(kb_id, request)

更新知识库配置

根据知识库ID更新模型和分块配置

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_kb_model_config_request import InternalHandlerKBModelConfigRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    kb_id = 'kb_id_example' # str | 知识库ID
    request = weknora_sdk.InternalHandlerKBModelConfigRequest() # InternalHandlerKBModelConfigRequest | 配置请求

    try:
        # 更新知识库配置
        api_response = api_instance.initialization_kb_kb_id_config_put(kb_id, request)
        print("The response of DefaultApi->initialization_kb_kb_id_config_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_kb_kb_id_config_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**| 知识库ID | 
 **request** | [**InternalHandlerKBModelConfigRequest**](InternalHandlerKBModelConfigRequest.md)| 配置请求 | 

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
**200** | 更新成功 |  -  |
**400** | 请求参数错误 |  -  |
**404** | 知识库不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_kb_kb_id_post**
> Dict[str, object] initialization_kb_kb_id_post(kb_id, request)

初始化知识库配置

根据知识库ID执行完整配置更新

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    kb_id = 'kb_id_example' # str | 知识库ID
    request = None # object | 初始化请求

    try:
        # 初始化知识库配置
        api_response = api_instance.initialization_kb_kb_id_post(kb_id, request)
        print("The response of DefaultApi->initialization_kb_kb_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_kb_kb_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**| 知识库ID | 
 **request** | **object**| 初始化请求 | 

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
**200** | 初始化成功 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_models_embedding_test_post**
> Dict[str, object] initialization_models_embedding_test_post(request)

测试Embedding模型

测试Embedding接口是否可用并返回向量维度

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = None # object | Embedding测试请求

    try:
        # 测试Embedding模型
        api_response = api_instance.initialization_models_embedding_test_post(request)
        print("The response of DefaultApi->initialization_models_embedding_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_models_embedding_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **object**| Embedding测试请求 | 

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
**200** | 测试结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_models_remote_check_post**
> Dict[str, object] initialization_models_remote_check_post(request)

检查远程模型

检查远程API模型连接是否正常

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_remote_model_check_request import InternalHandlerRemoteModelCheckRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InternalHandlerRemoteModelCheckRequest() # InternalHandlerRemoteModelCheckRequest | 模型检查请求

    try:
        # 检查远程模型
        api_response = api_instance.initialization_models_remote_check_post(request)
        print("The response of DefaultApi->initialization_models_remote_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_models_remote_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalHandlerRemoteModelCheckRequest**](InternalHandlerRemoteModelCheckRequest.md)| 模型检查请求 | 

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
**200** | 检查结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_models_rerank_check_post**
> Dict[str, object] initialization_models_rerank_check_post(request)

检查Rerank模型

检查Rerank模型连接和功能是否正常

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = None # object | Rerank检查请求

    try:
        # 检查Rerank模型
        api_response = api_instance.initialization_models_rerank_check_post(request)
        print("The response of DefaultApi->initialization_models_rerank_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_models_rerank_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **object**| Rerank检查请求 | 

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
**200** | 检查结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_multimodal_test_post**
> Dict[str, object] initialization_multimodal_test_post(image, vlm_model, vlm_base_url, storage_type, vlm_api_key=vlm_api_key, vlm_interface_type=vlm_interface_type)

测试多模态功能

上传图片测试多模态处理功能

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    image = None # bytearray | 测试图片
    vlm_model = 'vlm_model_example' # str | VLM模型名称
    vlm_base_url = 'vlm_base_url_example' # str | VLM Base URL
    storage_type = 'storage_type_example' # str | 存储类型(cos/minio)
    vlm_api_key = 'vlm_api_key_example' # str | VLM API Key (optional)
    vlm_interface_type = 'vlm_interface_type_example' # str | VLM接口类型 (optional)

    try:
        # 测试多模态功能
        api_response = api_instance.initialization_multimodal_test_post(image, vlm_model, vlm_base_url, storage_type, vlm_api_key=vlm_api_key, vlm_interface_type=vlm_interface_type)
        print("The response of DefaultApi->initialization_multimodal_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_multimodal_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **bytearray**| 测试图片 | 
 **vlm_model** | **str**| VLM模型名称 | 
 **vlm_base_url** | **str**| VLM Base URL | 
 **storage_type** | **str**| 存储类型(cos/minio) | 
 **vlm_api_key** | **str**| VLM API Key | [optional] 
 **vlm_interface_type** | **str**| VLM接口类型 | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 测试结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_ollama_download_task_id_get**
> Dict[str, object] initialization_ollama_download_task_id_get(task_id)

获取下载进度

获取Ollama模型下载任务的进度

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    task_id = 'task_id_example' # str | 任务ID

    try:
        # 获取下载进度
        api_response = api_instance.initialization_ollama_download_task_id_get(task_id)
        print("The response of DefaultApi->initialization_ollama_download_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_ollama_download_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| 任务ID | 

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
**200** | 下载进度 |  -  |
**404** | 任务不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_ollama_download_tasks_get**
> Dict[str, object] initialization_ollama_download_tasks_get()

列出下载任务

列出所有Ollama模型下载任务

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 列出下载任务
        api_response = api_instance.initialization_ollama_download_tasks_get()
        print("The response of DefaultApi->initialization_ollama_download_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_ollama_download_tasks_get: %s\n" % e)
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
**200** | 任务列表 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_ollama_models_check_post**
> Dict[str, object] initialization_ollama_models_check_post(request)

检查Ollama模型状态

检查指定的Ollama模型是否已安装

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.initialization_ollama_models_check_post_request import InitializationOllamaModelsCheckPostRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InitializationOllamaModelsCheckPostRequest() # InitializationOllamaModelsCheckPostRequest | 模型名称列表

    try:
        # 检查Ollama模型状态
        api_response = api_instance.initialization_ollama_models_check_post(request)
        print("The response of DefaultApi->initialization_ollama_models_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_ollama_models_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InitializationOllamaModelsCheckPostRequest**](InitializationOllamaModelsCheckPostRequest.md)| 模型名称列表 | 

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
**200** | 模型状态 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_ollama_models_download_post**
> Dict[str, object] initialization_ollama_models_download_post(request)

下载Ollama模型

异步下载指定的Ollama模型

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.initialization_ollama_models_download_post_request import InitializationOllamaModelsDownloadPostRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InitializationOllamaModelsDownloadPostRequest() # InitializationOllamaModelsDownloadPostRequest | 模型名称

    try:
        # 下载Ollama模型
        api_response = api_instance.initialization_ollama_models_download_post(request)
        print("The response of DefaultApi->initialization_ollama_models_download_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_ollama_models_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InitializationOllamaModelsDownloadPostRequest**](InitializationOllamaModelsDownloadPostRequest.md)| 模型名称 | 

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
**200** | 下载任务信息 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_ollama_models_get**
> Dict[str, object] initialization_ollama_models_get()

列出Ollama模型

列出已安装的Ollama模型

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 列出Ollama模型
        api_response = api_instance.initialization_ollama_models_get()
        print("The response of DefaultApi->initialization_ollama_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_ollama_models_get: %s\n" % e)
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
**200** | 模型列表 |  -  |
**500** | 服务器错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialization_ollama_status_get**
> Dict[str, object] initialization_ollama_status_get()

检查Ollama服务状态

检查Ollama服务是否可用

### Example


```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 检查Ollama服务状态
        api_response = api_instance.initialization_ollama_status_get()
        print("The response of DefaultApi->initialization_ollama_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initialization_ollama_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ollama状态 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_copy_post**
> Dict[str, object] knowledge_bases_copy_post(request)

复制知识库

将一个知识库的内容复制到另一个知识库（异步任务）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_copy_knowledge_base_request import InternalHandlerCopyKnowledgeBaseRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InternalHandlerCopyKnowledgeBaseRequest() # InternalHandlerCopyKnowledgeBaseRequest | 复制请求

    try:
        # 复制知识库
        api_response = api_instance.knowledge_bases_copy_post(request)
        print("The response of DefaultApi->knowledge_bases_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalHandlerCopyKnowledgeBaseRequest**](InternalHandlerCopyKnowledgeBaseRequest.md)| 复制请求 | 

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
**200** | 任务ID |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_copy_progress_task_id_get**
> Dict[str, object] knowledge_bases_copy_progress_task_id_get(task_id)

获取知识库复制进度

获取知识库复制任务的进度

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    task_id = 'task_id_example' # str | 任务ID

    try:
        # 获取知识库复制进度
        api_response = api_instance.knowledge_bases_copy_progress_task_id_get(task_id)
        print("The response of DefaultApi->knowledge_bases_copy_progress_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_copy_progress_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| 任务ID | 

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
**200** | 进度信息 |  -  |
**404** | 任务不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_get**
> Dict[str, object] knowledge_bases_get()

获取知识库列表

获取当前租户的所有知识库

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取知识库列表
        api_response = api_instance.knowledge_bases_get()
        print("The response of DefaultApi->knowledge_bases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_get: %s\n" % e)
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
**200** | 知识库列表 |  -  |
**500** | 服务器错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_delete**
> Dict[str, object] knowledge_bases_id_delete(id)

删除知识库

删除指定的知识库及其所有内容

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID

    try:
        # 删除知识库
        api_response = api_instance.knowledge_bases_id_delete(id)
        print("The response of DefaultApi->knowledge_bases_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 

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
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_get**
> Dict[str, object] knowledge_bases_id_get(id)

获取知识库详情

根据ID获取知识库详情

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID

    try:
        # 获取知识库详情
        api_response = api_instance.knowledge_bases_id_get(id)
        print("The response of DefaultApi->knowledge_bases_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 

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
**200** | 知识库详情 |  -  |
**400** | 请求参数错误 |  -  |
**404** | 知识库不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_hybrid_search_get**
> Dict[str, object] knowledge_bases_id_hybrid_search_get(id, request)

混合搜索

在知识库中执行向量和关键词混合搜索

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_search_params import GithubComTencentWeKnoraInternalTypesSearchParams
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesSearchParams() # GithubComTencentWeKnoraInternalTypesSearchParams | 搜索参数

    try:
        # 混合搜索
        api_response = api_instance.knowledge_bases_id_hybrid_search_get(id, request)
        print("The response of DefaultApi->knowledge_bases_id_hybrid_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_hybrid_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesSearchParams**](GithubComTencentWeKnoraInternalTypesSearchParams.md)| 搜索参数 | 

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
**200** | 搜索结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_knowledge_file_post**
> Dict[str, object] knowledge_bases_id_knowledge_file_post(id, file, file_name=file_name, metadata=metadata, enable_multimodel=enable_multimodel)

从文件创建知识

上传文件并创建知识条目

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    file = None # bytearray | 上传的文件
    file_name = 'file_name_example' # str | 自定义文件名 (optional)
    metadata = 'metadata_example' # str | 元数据JSON (optional)
    enable_multimodel = True # bool | 启用多模态处理 (optional)

    try:
        # 从文件创建知识
        api_response = api_instance.knowledge_bases_id_knowledge_file_post(id, file, file_name=file_name, metadata=metadata, enable_multimodel=enable_multimodel)
        print("The response of DefaultApi->knowledge_bases_id_knowledge_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_knowledge_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **file** | **bytearray**| 上传的文件 | 
 **file_name** | **str**| 自定义文件名 | [optional] 
 **metadata** | **str**| 元数据JSON | [optional] 
 **enable_multimodel** | **bool**| 启用多模态处理 | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 创建的知识 |  -  |
**400** | 请求参数错误 |  -  |
**409** | 文件重复 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_knowledge_get**
> Dict[str, object] knowledge_bases_id_knowledge_get(id, page=page, page_size=page_size, tag_id=tag_id, keyword=keyword, file_type=file_type)

获取知识列表

获取知识库下的知识列表，支持分页和筛选

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    page = 56 # int | 页码 (optional)
    page_size = 56 # int | 每页数量 (optional)
    tag_id = 'tag_id_example' # str | 标签ID筛选 (optional)
    keyword = 'keyword_example' # str | 关键词搜索 (optional)
    file_type = 'file_type_example' # str | 文件类型筛选 (optional)

    try:
        # 获取知识列表
        api_response = api_instance.knowledge_bases_id_knowledge_get(id, page=page, page_size=page_size, tag_id=tag_id, keyword=keyword, file_type=file_type)
        print("The response of DefaultApi->knowledge_bases_id_knowledge_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_knowledge_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **page** | **int**| 页码 | [optional] 
 **page_size** | **int**| 每页数量 | [optional] 
 **tag_id** | **str**| 标签ID筛选 | [optional] 
 **keyword** | **str**| 关键词搜索 | [optional] 
 **file_type** | **str**| 文件类型筛选 | [optional] 

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
**200** | 知识列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_knowledge_manual_post**
> Dict[str, object] knowledge_bases_id_knowledge_manual_post(id, request)

手工创建知识

手工录入Markdown格式的知识内容

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_manual_knowledge_payload import GithubComTencentWeKnoraInternalTypesManualKnowledgePayload
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesManualKnowledgePayload() # GithubComTencentWeKnoraInternalTypesManualKnowledgePayload | 手工知识内容

    try:
        # 手工创建知识
        api_response = api_instance.knowledge_bases_id_knowledge_manual_post(id, request)
        print("The response of DefaultApi->knowledge_bases_id_knowledge_manual_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_knowledge_manual_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesManualKnowledgePayload**](GithubComTencentWeKnoraInternalTypesManualKnowledgePayload.md)| 手工知识内容 | 

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
**200** | 创建的知识 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_knowledge_url_post**
> Dict[str, object] knowledge_bases_id_knowledge_url_post(id, request)

从URL创建知识

从指定URL抓取内容并创建知识条目

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.knowledge_bases_id_knowledge_url_post_request import KnowledgeBasesIdKnowledgeUrlPostRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora_sdk.KnowledgeBasesIdKnowledgeUrlPostRequest() # KnowledgeBasesIdKnowledgeUrlPostRequest | URL请求

    try:
        # 从URL创建知识
        api_response = api_instance.knowledge_bases_id_knowledge_url_post(id, request)
        print("The response of DefaultApi->knowledge_bases_id_knowledge_url_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_knowledge_url_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**KnowledgeBasesIdKnowledgeUrlPostRequest**](KnowledgeBasesIdKnowledgeUrlPostRequest.md)| URL请求 | 

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
**201** | 创建的知识 |  -  |
**400** | 请求参数错误 |  -  |
**409** | URL重复 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_put**
> Dict[str, object] knowledge_bases_id_put(id, request)

更新知识库

更新知识库的名称、描述和配置

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_update_knowledge_base_request import InternalHandlerUpdateKnowledgeBaseRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora_sdk.InternalHandlerUpdateKnowledgeBaseRequest() # InternalHandlerUpdateKnowledgeBaseRequest | 更新请求

    try:
        # 更新知识库
        api_response = api_instance.knowledge_bases_id_put(id, request)
        print("The response of DefaultApi->knowledge_bases_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**InternalHandlerUpdateKnowledgeBaseRequest**](InternalHandlerUpdateKnowledgeBaseRequest.md)| 更新请求 | 

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
**200** | 更新后的知识库 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_tags_get**
> Dict[str, object] knowledge_bases_id_tags_get(id, page=page, page_size=page_size, keyword=keyword)

获取标签列表

获取知识库下的所有标签及统计信息

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    page = 56 # int | 页码 (optional)
    page_size = 56 # int | 每页数量 (optional)
    keyword = 'keyword_example' # str | 关键词搜索 (optional)

    try:
        # 获取标签列表
        api_response = api_instance.knowledge_bases_id_tags_get(id, page=page, page_size=page_size, keyword=keyword)
        print("The response of DefaultApi->knowledge_bases_id_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **page** | **int**| 页码 | [optional] 
 **page_size** | **int**| 每页数量 | [optional] 
 **keyword** | **str**| 关键词搜索 | [optional] 

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
**200** | 标签列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_tags_post**
> Dict[str, object] knowledge_bases_id_tags_post(id, request)

创建标签

在知识库下创建新标签

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.knowledge_bases_id_tags_post_request import KnowledgeBasesIdTagsPostRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora_sdk.KnowledgeBasesIdTagsPostRequest() # KnowledgeBasesIdTagsPostRequest | 标签信息

    try:
        # 创建标签
        api_response = api_instance.knowledge_bases_id_tags_post(id, request)
        print("The response of DefaultApi->knowledge_bases_id_tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**KnowledgeBasesIdTagsPostRequest**](KnowledgeBasesIdTagsPostRequest.md)| 标签信息 | 

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
**200** | 创建的标签 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_tags_tag_id_delete**
> Dict[str, object] knowledge_bases_id_tags_tag_id_delete(id, tag_id, force=force, content_only=content_only)

删除标签

删除标签，可使用force=true强制删除被引用的标签，content_only=true仅删除标签下的内容而保留标签本身

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    tag_id = 'tag_id_example' # str | 标签ID
    force = True # bool | 强制删除 (optional)
    content_only = True # bool | 仅删除内容，保留标签 (optional)

    try:
        # 删除标签
        api_response = api_instance.knowledge_bases_id_tags_tag_id_delete(id, tag_id, force=force, content_only=content_only)
        print("The response of DefaultApi->knowledge_bases_id_tags_tag_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_tags_tag_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **tag_id** | **str**| 标签ID | 
 **force** | **bool**| 强制删除 | [optional] 
 **content_only** | **bool**| 仅删除内容，保留标签 | [optional] 

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
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_tags_tag_id_put**
> Dict[str, object] knowledge_bases_id_tags_tag_id_put(id, tag_id, request)

更新标签

更新标签信息

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识库ID
    tag_id = 'tag_id_example' # str | 标签ID
    request = None # object | 标签更新信息

    try:
        # 更新标签
        api_response = api_instance.knowledge_bases_id_tags_tag_id_put(id, tag_id, request)
        print("The response of DefaultApi->knowledge_bases_id_tags_tag_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_id_tags_tag_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **tag_id** | **str**| 标签ID | 
 **request** | **object**| 标签更新信息 | 

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
**200** | 更新后的标签 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_post**
> Dict[str, object] knowledge_bases_post(request)

创建知识库

创建新的知识库

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_knowledge_base import GithubComTencentWeKnoraInternalTypesKnowledgeBase
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesKnowledgeBase() # GithubComTencentWeKnoraInternalTypesKnowledgeBase | 知识库信息

    try:
        # 创建知识库
        api_response = api_instance.knowledge_bases_post(request)
        print("The response of DefaultApi->knowledge_bases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_bases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GithubComTencentWeKnoraInternalTypesKnowledgeBase**](GithubComTencentWeKnoraInternalTypesKnowledgeBase.md)| 知识库信息 | 

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
**201** | 创建的知识库 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_batch_get**
> Dict[str, object] knowledge_batch_get(ids)

批量获取知识

根据ID列表批量获取知识条目

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    ids = ['ids_example'] # List[str] | 知识ID列表

    try:
        # 批量获取知识
        api_response = api_instance.knowledge_batch_get(ids)
        print("The response of DefaultApi->knowledge_batch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_batch_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| 知识ID列表 | 

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
**200** | 知识列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_id_delete**
> Dict[str, object] knowledge_id_delete(id)

删除知识

根据ID删除知识条目

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识ID

    try:
        # 删除知识
        api_response = api_instance.knowledge_id_delete(id)
        print("The response of DefaultApi->knowledge_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识ID | 

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
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_id_download_get**
> bytearray knowledge_id_download_get(id)

下载知识文件

下载知识条目关联的原始文件

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识ID

    try:
        # 下载知识文件
        api_response = api_instance.knowledge_id_download_get(id)
        print("The response of DefaultApi->knowledge_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识ID | 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 文件内容 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_id_get**
> Dict[str, object] knowledge_id_get(id)

获取知识详情

根据ID获取知识条目详情

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识ID

    try:
        # 获取知识详情
        api_response = api_instance.knowledge_id_get(id)
        print("The response of DefaultApi->knowledge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识ID | 

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
**200** | 知识详情 |  -  |
**400** | 请求参数错误 |  -  |
**404** | 知识不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_id_put**
> Dict[str, object] knowledge_id_put(id, request)

更新知识

更新知识条目信息

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_knowledge import GithubComTencentWeKnoraInternalTypesKnowledge
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识ID
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesKnowledge() # GithubComTencentWeKnoraInternalTypesKnowledge | 知识信息

    try:
        # 更新知识
        api_response = api_instance.knowledge_id_put(id, request)
        print("The response of DefaultApi->knowledge_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesKnowledge**](GithubComTencentWeKnoraInternalTypesKnowledge.md)| 知识信息 | 

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
**200** | 更新成功 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_image_id_chunk_id_put**
> Dict[str, object] knowledge_image_id_chunk_id_put(id, chunk_id, request)

更新图像信息

更新知识分块的图像信息

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.knowledge_image_id_chunk_id_put_request import KnowledgeImageIdChunkIdPutRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识ID
    chunk_id = 'chunk_id_example' # str | 分块ID
    request = weknora_sdk.KnowledgeImageIdChunkIdPutRequest() # KnowledgeImageIdChunkIdPutRequest | 图像信息

    try:
        # 更新图像信息
        api_response = api_instance.knowledge_image_id_chunk_id_put(id, chunk_id, request)
        print("The response of DefaultApi->knowledge_image_id_chunk_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_image_id_chunk_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识ID | 
 **chunk_id** | **str**| 分块ID | 
 **request** | [**KnowledgeImageIdChunkIdPutRequest**](KnowledgeImageIdChunkIdPutRequest.md)| 图像信息 | 

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
**200** | 更新成功 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_manual_id_put**
> Dict[str, object] knowledge_manual_id_put(id, request)

更新手工知识

更新手工录入的Markdown知识内容

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_manual_knowledge_payload import GithubComTencentWeKnoraInternalTypesManualKnowledgePayload
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 知识ID
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesManualKnowledgePayload() # GithubComTencentWeKnoraInternalTypesManualKnowledgePayload | 手工知识内容

    try:
        # 更新手工知识
        api_response = api_instance.knowledge_manual_id_put(id, request)
        print("The response of DefaultApi->knowledge_manual_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_manual_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesManualKnowledgePayload**](GithubComTencentWeKnoraInternalTypesManualKnowledgePayload.md)| 手工知识内容 | 

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
**200** | 更新后的知识 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_tags_put**
> Dict[str, object] knowledge_tags_put(request)

批量更新知识标签

批量更新知识条目的标签

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = None # object | 标签更新请求

    try:
        # 批量更新知识标签
        api_response = api_instance.knowledge_tags_put(request)
        print("The response of DefaultApi->knowledge_tags_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->knowledge_tags_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **object**| 标签更新请求 | 

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
**200** | 更新成功 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_session_id_id_delete**
> Dict[str, object] messages_session_id_id_delete(session_id, id)

删除消息

从会话中删除指定消息

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 会话ID
    id = 'id_example' # str | 消息ID

    try:
        # 删除消息
        api_response = api_instance.messages_session_id_id_delete(session_id, id)
        print("The response of DefaultApi->messages_session_id_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->messages_session_id_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| 会话ID | 
 **id** | **str**| 消息ID | 

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

# **messages_session_id_load_get**
> Dict[str, object] messages_session_id_load_get(session_id, limit=limit, before_time=before_time)

加载消息历史

加载会话的消息历史，支持分页和时间筛选

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 会话ID
    limit = 20 # int | 返回数量 (optional) (default to 20)
    before_time = 'before_time_example' # str | 在此时间之前的消息（RFC3339Nano格式） (optional)

    try:
        # 加载消息历史
        api_response = api_instance.messages_session_id_load_get(session_id, limit=limit, before_time=before_time)
        print("The response of DefaultApi->messages_session_id_load_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->messages_session_id_load_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| 会话ID | 
 **limit** | **int**| 返回数量 | [optional] [default to 20]
 **before_time** | **str**| 在此时间之前的消息（RFC3339Nano格式） | [optional] 

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
**200** | 消息列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get**
> Dict[str, object] models_get()

获取模型列表

获取当前租户的所有模型

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取模型列表
        api_response = api_instance.models_get()
        print("The response of DefaultApi->models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->models_get: %s\n" % e)
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
**200** | 模型列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_id_delete**
> Dict[str, object] models_id_delete(id)

删除模型

删除指定的模型

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 模型ID

    try:
        # 删除模型
        api_response = api_instance.models_id_delete(id)
        print("The response of DefaultApi->models_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->models_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 模型ID | 

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
**404** | 模型不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_id_get**
> Dict[str, object] models_id_get(id)

获取模型详情

根据ID获取模型详情

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 模型ID

    try:
        # 获取模型详情
        api_response = api_instance.models_id_get(id)
        print("The response of DefaultApi->models_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->models_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 模型ID | 

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
**200** | 模型详情 |  -  |
**404** | 模型不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_id_put**
> Dict[str, object] models_id_put(id, request)

更新模型

更新模型配置信息

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_update_model_request import InternalHandlerUpdateModelRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 模型ID
    request = weknora_sdk.InternalHandlerUpdateModelRequest() # InternalHandlerUpdateModelRequest | 更新信息

    try:
        # 更新模型
        api_response = api_instance.models_id_put(id, request)
        print("The response of DefaultApi->models_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->models_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 模型ID | 
 **request** | [**InternalHandlerUpdateModelRequest**](InternalHandlerUpdateModelRequest.md)| 更新信息 | 

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
**200** | 更新后的模型 |  -  |
**404** | 模型不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_post**
> Dict[str, object] models_post(request)

创建模型

创建新的模型配置

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_create_model_request import InternalHandlerCreateModelRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InternalHandlerCreateModelRequest() # InternalHandlerCreateModelRequest | 模型信息

    try:
        # 创建模型
        api_response = api_instance.models_post(request)
        print("The response of DefaultApi->models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalHandlerCreateModelRequest**](InternalHandlerCreateModelRequest.md)| 模型信息 | 

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
**201** | 创建的模型 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_get**
> Dict[str, object] sessions_get(page=page, page_size=page_size)

获取会话列表

获取当前租户的会话列表，支持分页

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    page = 56 # int | 页码 (optional)
    page_size = 56 # int | 每页数量 (optional)

    try:
        # 获取会话列表
        api_response = api_instance.sessions_get(page=page, page_size=page_size)
        print("The response of DefaultApi->sessions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| 页码 | [optional] 
 **page_size** | **int**| 每页数量 | [optional] 

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
**200** | 会话列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_id_delete**
> Dict[str, object] sessions_id_delete(id)

删除会话

删除指定的会话

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 会话ID

    try:
        # 删除会话
        api_response = api_instance.sessions_id_delete(id)
        print("The response of DefaultApi->sessions_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 会话ID | 

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
**404** | 会话不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_id_get**
> Dict[str, object] sessions_id_get(id)

获取会话详情

根据ID获取会话详情

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 会话ID

    try:
        # 获取会话详情
        api_response = api_instance.sessions_id_get(id)
        print("The response of DefaultApi->sessions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 会话ID | 

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
**200** | 会话详情 |  -  |
**404** | 会话不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_id_put**
> Dict[str, object] sessions_id_put(id, request)

更新会话

更新会话属性

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_session import GithubComTencentWeKnoraInternalTypesSession
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 会话ID
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesSession() # GithubComTencentWeKnoraInternalTypesSession | 会话信息

    try:
        # 更新会话
        api_response = api_instance.sessions_id_put(id, request)
        print("The response of DefaultApi->sessions_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 会话ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesSession**](GithubComTencentWeKnoraInternalTypesSession.md)| 会话信息 | 

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
**200** | 更新后的会话 |  -  |
**404** | 会话不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_post**
> Dict[str, object] sessions_post(request)

创建会话

创建新的对话会话

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_session_create_session_request import InternalHandlerSessionCreateSessionRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InternalHandlerSessionCreateSessionRequest() # InternalHandlerSessionCreateSessionRequest | 会话创建请求

    try:
        # 创建会话
        api_response = api_instance.sessions_post(request)
        print("The response of DefaultApi->sessions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalHandlerSessionCreateSessionRequest**](InternalHandlerSessionCreateSessionRequest.md)| 会话创建请求 | 

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
**201** | 创建的会话 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_search_post**
> Dict[str, object] sessions_search_post(request)

知识搜索

在知识库中搜索（不使用LLM总结）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_session_search_knowledge_request import InternalHandlerSessionSearchKnowledgeRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.InternalHandlerSessionSearchKnowledgeRequest() # InternalHandlerSessionSearchKnowledgeRequest | 搜索请求

    try:
        # 知识搜索
        api_response = api_instance.sessions_search_post(request)
        print("The response of DefaultApi->sessions_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalHandlerSessionSearchKnowledgeRequest**](InternalHandlerSessionSearchKnowledgeRequest.md)| 搜索请求 | 

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
**200** | 搜索结果 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_agent_qa_post**
> Dict[str, object] sessions_session_id_agent_qa_post(session_id, request)

Agent问答

基于Agent的智能问答，支持多轮对话和SSE流式响应

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_session_create_knowledge_qa_request import InternalHandlerSessionCreateKnowledgeQARequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 会话ID
    request = weknora_sdk.InternalHandlerSessionCreateKnowledgeQARequest() # InternalHandlerSessionCreateKnowledgeQARequest | 问答请求

    try:
        # Agent问答
        api_response = api_instance.sessions_session_id_agent_qa_post(session_id, request)
        print("The response of DefaultApi->sessions_session_id_agent_qa_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_session_id_agent_qa_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| 会话ID | 
 **request** | [**InternalHandlerSessionCreateKnowledgeQARequest**](InternalHandlerSessionCreateKnowledgeQARequest.md)| 问答请求 | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 问答结果（SSE流） |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_continue_get**
> Dict[str, object] sessions_session_id_continue_get(session_id, message_id)

继续流式响应

继续获取正在进行的流式响应

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 会话ID
    message_id = 'message_id_example' # str | 消息ID

    try:
        # 继续流式响应
        api_response = api_instance.sessions_session_id_continue_get(session_id, message_id)
        print("The response of DefaultApi->sessions_session_id_continue_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_session_id_continue_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| 会话ID | 
 **message_id** | **str**| 消息ID | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 流式响应 |  -  |
**404** | 会话或消息不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_knowledge_qa_post**
> Dict[str, object] sessions_session_id_knowledge_qa_post(session_id, request)

知识问答

基于知识库的问答（使用LLM总结），支持SSE流式响应

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_session_create_knowledge_qa_request import InternalHandlerSessionCreateKnowledgeQARequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 会话ID
    request = weknora_sdk.InternalHandlerSessionCreateKnowledgeQARequest() # InternalHandlerSessionCreateKnowledgeQARequest | 问答请求

    try:
        # 知识问答
        api_response = api_instance.sessions_session_id_knowledge_qa_post(session_id, request)
        print("The response of DefaultApi->sessions_session_id_knowledge_qa_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_session_id_knowledge_qa_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| 会话ID | 
 **request** | [**InternalHandlerSessionCreateKnowledgeQARequest**](InternalHandlerSessionCreateKnowledgeQARequest.md)| 问答请求 | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 问答结果（SSE流） |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_stop_post**
> Dict[str, object] sessions_session_id_stop_post(session_id, request)

停止生成

停止当前正在进行的生成任务

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_session_stop_session_request import InternalHandlerSessionStopSessionRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 会话ID
    request = weknora_sdk.InternalHandlerSessionStopSessionRequest() # InternalHandlerSessionStopSessionRequest | 停止请求

    try:
        # 停止生成
        api_response = api_instance.sessions_session_id_stop_post(session_id, request)
        print("The response of DefaultApi->sessions_session_id_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_session_id_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| 会话ID | 
 **request** | [**InternalHandlerSessionStopSessionRequest**](InternalHandlerSessionStopSessionRequest.md)| 停止请求 | 

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
**200** | 停止成功 |  -  |
**404** | 会话或消息不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_title_post**
> Dict[str, object] sessions_session_id_title_post(session_id, request)

生成会话标题

根据消息内容自动生成会话标题

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.internal_handler_session_generate_title_request import InternalHandlerSessionGenerateTitleRequest
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 会话ID
    request = weknora_sdk.InternalHandlerSessionGenerateTitleRequest() # InternalHandlerSessionGenerateTitleRequest | 生成请求

    try:
        # 生成会话标题
        api_response = api_instance.sessions_session_id_title_post(session_id, request)
        print("The response of DefaultApi->sessions_session_id_title_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sessions_session_id_title_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| 会话ID | 
 **request** | [**InternalHandlerSessionGenerateTitleRequest**](InternalHandlerSessionGenerateTitleRequest.md)| 生成请求 | 

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
**200** | 生成的标题 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_info_get**
> InternalHandlerGetSystemInfoResponse system_info_get()

获取系统信息

获取系统版本、构建信息和引擎配置

### Example


```python
import weknora_sdk
from weknora_sdk.models.internal_handler_get_system_info_response import InternalHandlerGetSystemInfoResponse
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取系统信息
        api_response = api_instance.system_info_get()
        print("The response of DefaultApi->system_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->system_info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalHandlerGetSystemInfoResponse**](InternalHandlerGetSystemInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 系统信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_all_get**
> Dict[str, object] tenants_all_get()

获取所有租户列表

获取系统中所有租户（需要跨租户访问权限）

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取所有租户列表
        api_response = api_instance.tenants_all_get()
        print("The response of DefaultApi->tenants_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_all_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 所有租户列表 |  -  |
**403** | 权限不足 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_get**
> Dict[str, object] tenants_get()

获取租户列表

获取当前用户可访问的租户列表

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取租户列表
        api_response = api_instance.tenants_get()
        print("The response of DefaultApi->tenants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 租户列表 |  -  |
**500** | 服务器错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_id_delete**
> Dict[str, object] tenants_id_delete(id)

删除租户

删除指定的租户

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 56 # int | 租户ID

    try:
        # 删除租户
        api_response = api_instance.tenants_id_delete(id)
        print("The response of DefaultApi->tenants_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 租户ID | 

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 删除成功 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_id_get**
> Dict[str, object] tenants_id_get(id)

获取租户详情

根据ID获取租户详情

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 56 # int | 租户ID

    try:
        # 获取租户详情
        api_response = api_instance.tenants_id_get(id)
        print("The response of DefaultApi->tenants_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 租户ID | 

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
**200** | 租户详情 |  -  |
**400** | 请求参数错误 |  -  |
**404** | 租户不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_id_put**
> Dict[str, object] tenants_id_put(id, request)

更新租户

更新租户信息

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_tenant import GithubComTencentWeKnoraInternalTypesTenant
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    id = 56 # int | 租户ID
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesTenant() # GithubComTencentWeKnoraInternalTypesTenant | 租户信息

    try:
        # 更新租户
        api_response = api_instance.tenants_id_put(id, request)
        print("The response of DefaultApi->tenants_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 租户ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesTenant**](GithubComTencentWeKnoraInternalTypesTenant.md)| 租户信息 | 

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 更新后的租户 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_kv_agent_config_get**
> Dict[str, object] tenants_kv_agent_config_get()

获取租户Agent配置

获取租户的全局Agent配置（默认应用于所有会话）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取租户Agent配置
        api_response = api_instance.tenants_kv_agent_config_get()
        print("The response of DefaultApi->tenants_kv_agent_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_kv_agent_config_get: %s\n" % e)
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
**200** | Agent配置 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_kv_conversation_config_get**
> Dict[str, object] tenants_kv_conversation_config_get()

获取租户对话配置

获取租户的全局对话配置（默认应用于普通模式会话）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取租户对话配置
        api_response = api_instance.tenants_kv_conversation_config_get()
        print("The response of DefaultApi->tenants_kv_conversation_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_kv_conversation_config_get: %s\n" % e)
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
**200** | 对话配置 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_kv_key_get**
> Dict[str, object] tenants_kv_key_get(key)

获取租户KV配置

获取租户级别的KV配置（支持agent-config、web-search-config、conversation-config）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    key = 'key_example' # str | 配置键名

    try:
        # 获取租户KV配置
        api_response = api_instance.tenants_kv_key_get(key)
        print("The response of DefaultApi->tenants_kv_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_kv_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| 配置键名 | 

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
**200** | 配置值 |  -  |
**400** | 不支持的键 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_kv_key_put**
> Dict[str, object] tenants_kv_key_put(key, request)

更新租户KV配置

更新租户级别的KV配置（支持agent-config、web-search-config、conversation-config）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    key = 'key_example' # str | 配置键名
    request = None # object | 配置值

    try:
        # 更新租户KV配置
        api_response = api_instance.tenants_kv_key_put(key, request)
        print("The response of DefaultApi->tenants_kv_key_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_kv_key_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| 配置键名 | 
 **request** | **object**| 配置值 | 

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
**200** | 更新成功 |  -  |
**400** | 不支持的键 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_kv_web_search_config_get**
> Dict[str, object] tenants_kv_web_search_config_get()

获取租户网络搜索配置

获取租户的网络搜索配置

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)

    try:
        # 获取租户网络搜索配置
        api_response = api_instance.tenants_kv_web_search_config_get()
        print("The response of DefaultApi->tenants_kv_web_search_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_kv_web_search_config_get: %s\n" % e)
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
**200** | 网络搜索配置 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_post**
> Dict[str, object] tenants_post(request)

创建租户

创建新的租户

### Example

* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_tenant import GithubComTencentWeKnoraInternalTypesTenant
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    request = weknora_sdk.GithubComTencentWeKnoraInternalTypesTenant() # GithubComTencentWeKnoraInternalTypesTenant | 租户信息

    try:
        # 创建租户
        api_response = api_instance.tenants_post(request)
        print("The response of DefaultApi->tenants_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GithubComTencentWeKnoraInternalTypesTenant**](GithubComTencentWeKnoraInternalTypesTenant.md)| 租户信息 | 

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 创建的租户 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_search_get**
> Dict[str, object] tenants_search_get(keyword=keyword, tenant_id=tenant_id, page=page, page_size=page_size)

搜索租户

分页搜索租户（需要跨租户访问权限）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora_sdk
from weknora_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora_sdk.Configuration(
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
with weknora_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora_sdk.DefaultApi(api_client)
    keyword = 'keyword_example' # str | 搜索关键词 (optional)
    tenant_id = 56 # int | 租户ID筛选 (optional)
    page = 1 # int | 页码 (optional) (default to 1)
    page_size = 20 # int | 每页数量 (optional) (default to 20)

    try:
        # 搜索租户
        api_response = api_instance.tenants_search_get(keyword=keyword, tenant_id=tenant_id, page=page, page_size=page_size)
        print("The response of DefaultApi->tenants_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tenants_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| 搜索关键词 | [optional] 
 **tenant_id** | **int**| 租户ID筛选 | [optional] 
 **page** | **int**| 页码 | [optional] [default to 1]
 **page_size** | **int**| 每页数量 | [optional] [default to 20]

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
**200** | 搜索结果 |  -  |
**403** | 权限不足 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

