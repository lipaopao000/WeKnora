# WeKnora Python SDK 使用指南

## 目录

- [安装](#安装)
- [快速开始](#快速开始)
- [认证](#认证)
- [知识库管理](#知识库管理)
- [会话管理](#会话管理)
- [消息发送](#消息发送)
- [FAQ管理](#faq管理)
- [高级用法](#高级用法)
- [错误处理](#错误处理)
- [常见问题](#常见问题)

## 安装

### 从源码安装

```bash
cd python-sdk
pip install -e .
```

### 安装依赖

SDK依赖以下包：
- urllib3 >= 2.1.0, < 3.0.0
- python_dateutil >= 2.8.2
- pydantic >= 2
- typing-extensions >= 4.7.1

这些依赖会在安装SDK时自动安装。

## 快速开始

### 方式1: 使用高级客户端（推荐）

```python
from weknora_sdk.client import WeKnoraClient

# 创建客户端
client = WeKnoraClient(host="http://localhost:8080/api/v1")

# 登录
client.login("username", "password")

# 获取知识库列表
knowledge_bases = client.get_knowledge_bases()
print(f"共有 {len(knowledge_bases)} 个知识库")

# 创建会话
session = client.create_session(
    knowledge_base_ids=[kb.id for kb in knowledge_bases],
    mode="agent"
)

# 发送消息
response = client.send_message(
    session_id=session.id,
    content="你好，请帮我查询相关信息"
)
print(f"回复: {response.content}")
```

### 方式2: 使用原生API

```python
from weknora_sdk import ApiClient, Configuration, DefaultApi

# 配置
config = Configuration()
config.host = "http://localhost:8080/api/v1"

# 创建客户端
api_client = ApiClient(configuration=config)
api = DefaultApi(api_client)

# 登录
login_response = api.auth_login_post(body={
    "username": "username",
    "password": "password"
})

# 设置认证token
config.api_key = {"Authorization": f"Bearer {login_response.token}"}

# 调用API
knowledge_bases = api.knowledge_bases_get()
```

## 认证

### 用户登录

```python
from weknora_sdk.client import WeKnoraClient

client = WeKnoraClient(host="http://localhost:8080/api/v1")

# 登录
response = client.login("username", "password")
print(f"登录成功，Token: {response.token}")
```

### 使用已有Token

```python
client = WeKnoraClient(
    host="http://localhost:8080/api/v1",
    token="your_existing_token"
)
```

### Token刷新

```python
# 刷新token
new_token_response = client.refresh_token(refresh_token="your_refresh_token")
print(f"新Token: {new_token_response.token}")
```

### 获取当前用户信息

```python
user_info = client.get_current_user()
print(f"用户名: {user_info.username}")
print(f"邮箱: {user_info.email}")
```

### 登出

```python
client.logout()
```

## 知识库管理

### 获取知识库列表

```python
# 获取所有知识库
knowledge_bases = client.get_knowledge_bases()

# 分页获取
knowledge_bases = client.get_knowledge_bases(page=1, page_size=10)

# 搜索知识库
knowledge_bases = client.get_knowledge_bases(keyword="技术文档")

# 遍历知识库
for kb in knowledge_bases:
    print(f"ID: {kb.id}")
    print(f"名称: {kb.name}")
    print(f"类型: {kb.type}")
    print(f"描述: {kb.description}")
    print("---")
```

### 获取知识库详情

```python
kb = client.get_knowledge_base(kb_id="kb_123456")
print(f"知识库名称: {kb.name}")
print(f"文档数量: {kb.knowledge_count}")
```

### 创建知识库

```python
# 创建文档知识库
kb = client.create_knowledge_base(
    name="技术文档库",
    description="存储所有技术文档",
    kb_type="document"
)
print(f"创建成功，ID: {kb.id}")

# 创建FAQ知识库
faq_kb = client.create_knowledge_base(
    name="常见问题",
    description="FAQ知识库",
    kb_type="faq"
)
```

### 更新知识库

```python
updated_kb = client.update_knowledge_base(
    kb_id="kb_123456",
    name="新名称",
    description="新描述"
)
```

### 删除知识库

```python
client.delete_knowledge_base(kb_id="kb_123456")
print("知识库已删除")
```

## 会话管理

### 创建会话

```python
# 创建Agent模式会话
session = client.create_session(
    knowledge_base_ids=["kb_123", "kb_456"],
    mode="agent"
)
print(f"会话ID: {session.id}")

# 创建普通模式会话
session = client.create_session(
    knowledge_base_ids=["kb_123"],
    mode="normal"
)
```

### 获取会话列表

```python
sessions = client.get_sessions(page=1, page_size=20)

for session in sessions:
    print(f"会话ID: {session.id}")
    print(f"创建时间: {session.created_at}")
    print(f"模式: {session.mode}")
```

### 获取会话详情

```python
session = client.get_session(session_id="session_123")
print(f"会话模式: {session.mode}")
print(f"关联知识库: {session.knowledge_base_ids}")
```

### 删除会话

```python
client.delete_session(session_id="session_123")
```

## 消息发送

### 发送普通消息

```python
response = client.send_message(
    session_id="session_123",
    content="什么是RAG？"
)
print(f"回复: {response.content}")
```

### 发送流式消息

```python
# 注意：流式响应需要特殊处理
response = client.send_message(
    session_id="session_123",
    content="请详细解释一下",
    stream=True
)
# 流式响应的处理需要根据实际API返回格式
```

### 获取历史消息

```python
messages = client.get_messages(
    session_id="session_123",
    page=1,
    page_size=50
)

for msg in messages:
    print(f"[{msg.role}] {msg.content}")
```

## FAQ管理

### 添加FAQ

```python
faq = client.add_faq(
    kb_id="faq_kb_123",
    question="如何重置密码？",
    answer="请点击登录页面的'忘记密码'链接，按照提示操作。"
)
print(f"FAQ ID: {faq.id}")
```

### 获取FAQ列表

```python
faqs = client.get_faq_list(
    kb_id="faq_kb_123",
    page=1,
    page_size=20
)

for faq in faqs:
    print(f"Q: {faq.question}")
    print(f"A: {faq.answer}")
    print("---")
```

### 更新FAQ

```python
updated_faq = client.update_faq(
    faq_id="faq_123",
    question="如何重置密码？（更新）",
    answer="新的答案内容"
)
```

### 删除FAQ

```python
client.delete_faq(faq_id="faq_123")
```

## 高级用法

### 使用模型类别名

```python
from weknora_sdk.shortcuts import AgentConfig, ConversationConfig

# 创建Agent配置
agent_config = AgentConfig(
    max_iterations=10,
    temperature=0.7,
    web_search_enabled=True,
    reflection_enabled=True
)

# 创建会话配置
conversation_config = ConversationConfig(
    agent_config=agent_config,
    max_context_length=4096
)
```

### 配置SSL和调试

```python
client = WeKnoraClient(
    host="https://your-domain.com/api/v1",
    verify_ssl=True,  # 验证SSL证书
    debug=True  # 启用调试模式，打印详细日志
)
```

### 自定义超时

```python
from weknora_sdk import Configuration, ApiClient

config = Configuration()
config.host = "http://localhost:8080/api/v1"

# 设置超时（秒）
api_client = ApiClient(configuration=config)
api_client.rest_client.pool_manager.connection_pool_kw['timeout'] = 30
```

### 使用代理

```python
config = Configuration()
config.proxy = "http://proxy.example.com:8080"
```

## 错误处理

### 捕获API异常

```python
from weknora_sdk.exceptions import ApiException

try:
    response = client.send_message(
        session_id="invalid_session",
        content="测试消息"
    )
except ApiException as e:
    print(f"API错误: {e.status}")
    print(f"错误信息: {e.reason}")
    print(f"响应体: {e.body}")
```

### 常见错误码

| 错误码 | 说明 | 处理方式 |
|-------|------|---------|
| 400 | 请求参数错误 | 检查请求参数是否正确 |
| 401 | 未授权 | 检查token是否有效，重新登录 |
| 403 | 禁止访问 | 检查权限设置 |
| 404 | 资源不存在 | 检查资源ID是否正确 |
| 429 | 请求过于频繁 | 实现重试机制，添加延迟 |
| 500 | 服务器错误 | 联系管理员或稍后重试 |

### 实现重试机制

```python
import time
from weknora_sdk.exceptions import ApiException

def send_message_with_retry(client, session_id, content, max_retries=3):
    """带重试的消息发送"""
    for attempt in range(max_retries):
        try:
            return client.send_message(session_id, content)
        except ApiException as e:
            if e.status == 429:  # Rate limit
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # 指数退避
                    print(f"请求过于频繁，等待 {wait_time} 秒后重试...")
                    time.sleep(wait_time)
                    continue
            raise
    
    raise Exception("重试次数已用尽")
```

## 常见问题

### Q1: 如何处理长类名？

**A:** 使用shortcuts模块：

```python
from weknora_sdk.shortcuts import AgentConfig, ConversationConfig
# 而不是
# from weknora_sdk import GithubComTencentWeKnoraInternalTypesAgentConfig
```

### Q2: 如何查看所有可用的API方法？

**A:** 使用Python的dir()函数：

```python
from weknora_sdk import DefaultApi
api = DefaultApi()
methods = [m for m in dir(api) if not m.startswith('_')]
print(methods)
```

### Q3: 为什么需要手动设置host？

**A:** 因为swagger.json中没有定义默认服务器地址，所以需要在代码中设置：

```python
config.host = "http://your-server:8080/api/v1"
```

### Q4: 如何处理流式响应？

**A:** 流式响应需要特殊处理，具体取决于API的返回格式。通常需要迭代响应对象：

```python
response = api.sessions_id_messages_post(
    id=session_id,
    body={"content": content, "stream": True}
)
# 根据实际返回格式处理流式数据
```

### Q5: 如何上传文件？

**A:** 文件上传需要使用multipart/form-data格式，具体实现取决于API定义：

```python
# 示例（需要根据实际API调整）
with open('document.pdf', 'rb') as f:
    response = api.knowledge_upload_post(
        knowledge_base_id="kb_123",
        file=f
    )
```

### Q6: 如何启用日志？

**A:** 设置debug模式：

```python
client = WeKnoraClient(debug=True)
```

或使用Python logging：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 最佳实践

1. **使用高级客户端**: 优先使用`WeKnoraClient`而不是直接使用API类
2. **错误处理**: 始终使用try-except捕获ApiException
3. **Token管理**: 实现token刷新机制，避免token过期
4. **连接池**: 复用ApiClient实例，避免频繁创建
5. **超时设置**: 根据网络情况设置合理的超时时间
6. **日志记录**: 在生产环境中启用适当的日志级别
7. **资源清理**: 及时删除不需要的会话和资源

## 更多资源

- [WeKnora官方文档](https://weknora.weixin.qq.com)
- [API参考文档](./docs/)
- [GitHub仓库](https://github.com/Tencent/WeKnora)
- [问题反馈](https://github.com/Tencent/WeKnora/issues)
