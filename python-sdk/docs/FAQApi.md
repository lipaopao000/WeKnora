# weknora.FAQApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**faq_import_progress_task_id_get**](FAQApi.md#faq_import_progress_task_id_get) | **GET** /faq/import/progress/{task_id} | 获取FAQ导入进度
[**knowledge_bases_id_faq_entries_delete**](FAQApi.md#knowledge_bases_id_faq_entries_delete) | **DELETE** /knowledge-bases/{id}/faq/entries | 批量删除FAQ条目
[**knowledge_bases_id_faq_entries_entry_id_get**](FAQApi.md#knowledge_bases_id_faq_entries_entry_id_get) | **GET** /knowledge-bases/{id}/faq/entries/{entry_id} | 获取FAQ条目详情
[**knowledge_bases_id_faq_entries_entry_id_put**](FAQApi.md#knowledge_bases_id_faq_entries_entry_id_put) | **PUT** /knowledge-bases/{id}/faq/entries/{entry_id} | 更新FAQ条目
[**knowledge_bases_id_faq_entries_export_get**](FAQApi.md#knowledge_bases_id_faq_entries_export_get) | **GET** /knowledge-bases/{id}/faq/entries/export | 导出FAQ条目
[**knowledge_bases_id_faq_entries_fields_put**](FAQApi.md#knowledge_bases_id_faq_entries_fields_put) | **PUT** /knowledge-bases/{id}/faq/entries/fields | 批量更新FAQ字段
[**knowledge_bases_id_faq_entries_get**](FAQApi.md#knowledge_bases_id_faq_entries_get) | **GET** /knowledge-bases/{id}/faq/entries | 获取FAQ条目列表
[**knowledge_bases_id_faq_entries_post**](FAQApi.md#knowledge_bases_id_faq_entries_post) | **POST** /knowledge-bases/{id}/faq/entries | 批量更新/插入FAQ条目
[**knowledge_bases_id_faq_entries_tags_put**](FAQApi.md#knowledge_bases_id_faq_entries_tags_put) | **PUT** /knowledge-bases/{id}/faq/entries/tags | 批量更新FAQ标签
[**knowledge_bases_id_faq_entry_post**](FAQApi.md#knowledge_bases_id_faq_entry_post) | **POST** /knowledge-bases/{id}/faq/entry | 创建单个FAQ条目
[**knowledge_bases_id_faq_search_post**](FAQApi.md#knowledge_bases_id_faq_search_post) | **POST** /knowledge-bases/{id}/faq/search | 搜索FAQ


# **faq_import_progress_task_id_get**
> Dict[str, object] faq_import_progress_task_id_get(task_id)

获取FAQ导入进度

获取FAQ导入任务的进度

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
    api_instance = weknora.FAQApi(api_client)
    task_id = 'task_id_example' # str | 任务ID

    try:
        # 获取FAQ导入进度
        api_response = api_instance.faq_import_progress_task_id_get(task_id)
        print("The response of FAQApi->faq_import_progress_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->faq_import_progress_task_id_get: %s\n" % e)
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
**200** | 导入进度 |  -  |
**404** | 任务不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_faq_entries_delete**
> Dict[str, object] knowledge_bases_id_faq_entries_delete(id, request)

批量删除FAQ条目

批量删除指定的FAQ条目

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.models.knowledge_bases_id_faq_entries_delete_request import KnowledgeBasesIdFaqEntriesDeleteRequest
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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora.KnowledgeBasesIdFaqEntriesDeleteRequest() # KnowledgeBasesIdFaqEntriesDeleteRequest | 要删除的FAQ ID列表

    try:
        # 批量删除FAQ条目
        api_response = api_instance.knowledge_bases_id_faq_entries_delete(id, request)
        print("The response of FAQApi->knowledge_bases_id_faq_entries_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entries_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**KnowledgeBasesIdFaqEntriesDeleteRequest**](KnowledgeBasesIdFaqEntriesDeleteRequest.md)| 要删除的FAQ ID列表 | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_faq_entries_entry_id_get**
> Dict[str, object] knowledge_bases_id_faq_entries_entry_id_get(id, entry_id)

获取FAQ条目详情

根据ID获取单个FAQ条目的详情

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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    entry_id = 'entry_id_example' # str | FAQ条目ID

    try:
        # 获取FAQ条目详情
        api_response = api_instance.knowledge_bases_id_faq_entries_entry_id_get(id, entry_id)
        print("The response of FAQApi->knowledge_bases_id_faq_entries_entry_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entries_entry_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **entry_id** | **str**| FAQ条目ID | 

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
**200** | FAQ条目详情 |  -  |
**400** | 请求参数错误 |  -  |
**404** | 条目不存在 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_faq_entries_entry_id_put**
> Dict[str, object] knowledge_bases_id_faq_entries_entry_id_put(id, entry_id, request)

更新FAQ条目

更新指定的FAQ条目

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.models.github_com_tencent_we_knora_internal_types_faq_entry_payload import GithubComTencentWeKnoraInternalTypesFAQEntryPayload
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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    entry_id = 'entry_id_example' # str | FAQ条目ID
    request = weknora.GithubComTencentWeKnoraInternalTypesFAQEntryPayload() # GithubComTencentWeKnoraInternalTypesFAQEntryPayload | FAQ条目

    try:
        # 更新FAQ条目
        api_response = api_instance.knowledge_bases_id_faq_entries_entry_id_put(id, entry_id, request)
        print("The response of FAQApi->knowledge_bases_id_faq_entries_entry_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entries_entry_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **entry_id** | **str**| FAQ条目ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesFAQEntryPayload**](GithubComTencentWeKnoraInternalTypesFAQEntryPayload.md)| FAQ条目 | 

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

# **knowledge_bases_id_faq_entries_export_get**
> bytearray knowledge_bases_id_faq_entries_export_get(id)

导出FAQ条目

将所有FAQ条目导出为CSV文件

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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID

    try:
        # 导出FAQ条目
        api_response = api_instance.knowledge_bases_id_faq_entries_export_get(id)
        print("The response of FAQApi->knowledge_bases_id_faq_entries_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entries_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV文件 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_faq_entries_fields_put**
> Dict[str, object] knowledge_bases_id_faq_entries_fields_put(id, request)

批量更新FAQ字段

批量更新FAQ条目的多个字段（is_enabled, is_recommended, tag_id）

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.models.github_com_tencent_we_knora_internal_types_faq_entry_fields_batch_update import GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate
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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora.GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate() # GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate | 字段更新请求

    try:
        # 批量更新FAQ字段
        api_response = api_instance.knowledge_bases_id_faq_entries_fields_put(id, request)
        print("The response of FAQApi->knowledge_bases_id_faq_entries_fields_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entries_fields_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate**](GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate.md)| 字段更新请求 | 

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

# **knowledge_bases_id_faq_entries_get**
> Dict[str, object] knowledge_bases_id_faq_entries_get(id, page=page, page_size=page_size, tag_id=tag_id, keyword=keyword, search_field=search_field, sort_order=sort_order)

获取FAQ条目列表

获取知识库下的FAQ条目列表，支持分页和筛选

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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    page = 56 # int | 页码 (optional)
    page_size = 56 # int | 每页数量 (optional)
    tag_id = 'tag_id_example' # str | 标签ID筛选 (optional)
    keyword = 'keyword_example' # str | 关键词搜索 (optional)
    search_field = 'search_field_example' # str | 搜索字段: standard_question(标准问题), similar_questions(相似问法), answers(答案), 默认搜索全部 (optional)
    sort_order = 'sort_order_example' # str | 排序方式: asc(按更新时间正序), 默认按更新时间倒序 (optional)

    try:
        # 获取FAQ条目列表
        api_response = api_instance.knowledge_bases_id_faq_entries_get(id, page=page, page_size=page_size, tag_id=tag_id, keyword=keyword, search_field=search_field, sort_order=sort_order)
        print("The response of FAQApi->knowledge_bases_id_faq_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **page** | **int**| 页码 | [optional] 
 **page_size** | **int**| 每页数量 | [optional] 
 **tag_id** | **str**| 标签ID筛选 | [optional] 
 **keyword** | **str**| 关键词搜索 | [optional] 
 **search_field** | **str**| 搜索字段: standard_question(标准问题), similar_questions(相似问法), answers(答案), 默认搜索全部 | [optional] 
 **sort_order** | **str**| 排序方式: asc(按更新时间正序), 默认按更新时间倒序 | [optional] 

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
**200** | FAQ列表 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_faq_entries_post**
> Dict[str, object] knowledge_bases_id_faq_entries_post(id, request)

批量更新/插入FAQ条目

异步批量更新或插入FAQ条目

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.models.github_com_tencent_we_knora_internal_types_faq_batch_upsert_payload import GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload
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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora.GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload() # GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload | 批量操作请求

    try:
        # 批量更新/插入FAQ条目
        api_response = api_instance.knowledge_bases_id_faq_entries_post(id, request)
        print("The response of FAQApi->knowledge_bases_id_faq_entries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload**](GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload.md)| 批量操作请求 | 

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

# **knowledge_bases_id_faq_entries_tags_put**
> Dict[str, object] knowledge_bases_id_faq_entries_tags_put(id, request)

批量更新FAQ标签

批量更新FAQ条目的标签

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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = None # object | 标签更新请求

    try:
        # 批量更新FAQ标签
        api_response = api_instance.knowledge_bases_id_faq_entries_tags_put(id, request)
        print("The response of FAQApi->knowledge_bases_id_faq_entries_tags_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entries_tags_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
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

# **knowledge_bases_id_faq_entry_post**
> Dict[str, object] knowledge_bases_id_faq_entry_post(id, request)

创建单个FAQ条目

同步创建单个FAQ条目

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.models.github_com_tencent_we_knora_internal_types_faq_entry_payload import GithubComTencentWeKnoraInternalTypesFAQEntryPayload
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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora.GithubComTencentWeKnoraInternalTypesFAQEntryPayload() # GithubComTencentWeKnoraInternalTypesFAQEntryPayload | FAQ条目

    try:
        # 创建单个FAQ条目
        api_response = api_instance.knowledge_bases_id_faq_entry_post(id, request)
        print("The response of FAQApi->knowledge_bases_id_faq_entry_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_entry_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesFAQEntryPayload**](GithubComTencentWeKnoraInternalTypesFAQEntryPayload.md)| FAQ条目 | 

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
**200** | 创建的FAQ条目 |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_bases_id_faq_search_post**
> Dict[str, object] knowledge_bases_id_faq_search_post(id, request)

搜索FAQ

使用混合搜索在FAQ中搜索

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.models.github_com_tencent_we_knora_internal_types_faq_search_request import GithubComTencentWeKnoraInternalTypesFAQSearchRequest
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
    api_instance = weknora.FAQApi(api_client)
    id = 'id_example' # str | 知识库ID
    request = weknora.GithubComTencentWeKnoraInternalTypesFAQSearchRequest() # GithubComTencentWeKnoraInternalTypesFAQSearchRequest | 搜索请求

    try:
        # 搜索FAQ
        api_response = api_instance.knowledge_bases_id_faq_search_post(id, request)
        print("The response of FAQApi->knowledge_bases_id_faq_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FAQApi->knowledge_bases_id_faq_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 知识库ID | 
 **request** | [**GithubComTencentWeKnoraInternalTypesFAQSearchRequest**](GithubComTencentWeKnoraInternalTypesFAQSearchRequest.md)| 搜索请求 | 

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

