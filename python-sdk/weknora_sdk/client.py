"""
WeKnora高级客户端封装
提供更友好和易用的API接口
"""

from typing import List, Optional, Dict, Any
from weknora_sdk import ApiClient, Configuration, DefaultApi, FAQApi, KnowledgeApi
from weknora_sdk.exceptions import ApiException


class WeKnoraClient:
    """
    WeKnora高级客户端
    
    提供简化的API接口，隐藏底层复杂性
    
    示例:
        >>> client = WeKnoraClient(host="http://localhost:8080/api/v1")
        >>> client.login("username", "password")
        >>> knowledge_bases = client.get_knowledge_bases()
        >>> session = client.create_session([kb.id for kb in knowledge_bases])
        >>> response = client.send_message(session.id, "你好")
    """
    
    def __init__(
        self,
        host: str = "http://localhost:8080/api/v1",
        token: Optional[str] = None,
        verify_ssl: bool = True,
        debug: bool = False
    ):
        """
        初始化WeKnora客户端
        
        Args:
            host: WeKnora服务器地址
            token: 认证token（可选，如果已有token）
            verify_ssl: 是否验证SSL证书
            debug: 是否启用调试模式
        """
        self.config = Configuration()
        self.config.host = host
        self.config.verify_ssl = verify_ssl
        self.config.debug = debug
        
        if token:
            self.config.api_key = {"Authorization": f"Bearer {token}"}
        
        self.api_client = ApiClient(configuration=self.config)
        self.default_api = DefaultApi(self.api_client)
        self.faq_api = FAQApi(self.api_client)
        self.knowledge_api = KnowledgeApi(self.api_client)
        
        self._token = token
    
    @property
    def token(self) -> Optional[str]:
        """获取当前token"""
        return self._token
    
    # ==================== 认证相关 ====================
    
    def login(self, username: str, password: str) -> Dict[str, Any]:
        """
        用户登录
        
        Args:
            username: 用户名
            password: 密码
            
        Returns:
            登录响应，包含token等信息
            
        Raises:
            ApiException: 登录失败
        """
        try:
            response = self.default_api.auth_login_post(body={
                "username": username,
                "password": password
            })
            
            # 更新token
            if hasattr(response, 'token'):
                self._token = response.token
                self.config.api_key = {"Authorization": f"Bearer {response.token}"}
            
            return response
        except ApiException as e:
            raise ApiException(f"登录失败: {e}")
    
    def logout(self) -> None:
        """用户登出"""
        try:
            self.default_api.auth_logout_post()
            self._token = None
            self.config.api_key = {}
        except ApiException as e:
            raise ApiException(f"登出失败: {e}")
    
    def get_current_user(self) -> Dict[str, Any]:
        """
        获取当前用户信息
        
        Returns:
            用户信息
        """
        return self.default_api.auth_me_get()
    
    def refresh_token(self, refresh_token: str) -> Dict[str, Any]:
        """
        刷新token
        
        Args:
            refresh_token: 刷新token
            
        Returns:
            新的token信息
        """
        response = self.default_api.auth_refresh_post(body={
            "refresh_token": refresh_token
        })
        
        if hasattr(response, 'token'):
            self._token = response.token
            self.config.api_key = {"Authorization": f"Bearer {response.token}"}
        
        return response
    
    # ==================== 知识库管理 ====================
    
    def get_knowledge_bases(
        self,
        page: int = 1,
        page_size: int = 20,
        keyword: Optional[str] = None
    ) -> List[Any]:
        """
        获取知识库列表
        
        Args:
            page: 页码
            page_size: 每页数量
            keyword: 搜索关键词
            
        Returns:
            知识库列表
        """
        return self.default_api.knowledge_bases_get(
            page=page,
            page_size=page_size,
            keyword=keyword
        )
    
    def get_knowledge_base(self, kb_id: str) -> Dict[str, Any]:
        """
        获取知识库详情
        
        Args:
            kb_id: 知识库ID
            
        Returns:
            知识库详情
        """
        return self.default_api.knowledge_bases_id_get(id=kb_id)
    
    def create_knowledge_base(
        self,
        name: str,
        description: Optional[str] = None,
        kb_type: str = "document",
        **kwargs
    ) -> Dict[str, Any]:
        """
        创建知识库
        
        Args:
            name: 知识库名称
            description: 知识库描述
            kb_type: 知识库类型（document或faq）
            **kwargs: 其他配置参数
            
        Returns:
            创建的知识库信息
        """
        body = {
            "name": name,
            "type": kb_type,
            **kwargs
        }
        
        if description:
            body["description"] = description
        
        return self.default_api.knowledge_bases_post(body=body)
    
    def update_knowledge_base(
        self,
        kb_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        更新知识库
        
        Args:
            kb_id: 知识库ID
            name: 新名称
            description: 新描述
            **kwargs: 其他更新参数
            
        Returns:
            更新后的知识库信息
        """
        body = {**kwargs}
        
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        
        return self.default_api.knowledge_bases_id_put(id=kb_id, body=body)
    
    def delete_knowledge_base(self, kb_id: str) -> None:
        """
        删除知识库
        
        Args:
            kb_id: 知识库ID
        """
        self.default_api.knowledge_bases_id_delete(id=kb_id)
    
    # ==================== 会话管理 ====================
    
    def create_session(
        self,
        knowledge_base_ids: Optional[List[str]] = None,
        mode: str = "agent",
        **kwargs
    ) -> Dict[str, Any]:
        """
        创建会话
        
        Args:
            knowledge_base_ids: 知识库ID列表
            mode: 会话模式（agent或normal）
            **kwargs: 其他配置参数
            
        Returns:
            会话信息
        """
        body = {
            "mode": mode,
            **kwargs
        }
        
        if knowledge_base_ids:
            body["knowledge_base_ids"] = knowledge_base_ids
        
        return self.default_api.sessions_post(body=body)
    
    def get_sessions(
        self,
        page: int = 1,
        page_size: int = 20
    ) -> List[Any]:
        """
        获取会话列表
        
        Args:
            page: 页码
            page_size: 每页数量
            
        Returns:
            会话列表
        """
        return self.default_api.sessions_get(page=page, page_size=page_size)
    
    def get_session(self, session_id: str) -> Dict[str, Any]:
        """
        获取会话详情
        
        Args:
            session_id: 会话ID
            
        Returns:
            会话详情
        """
        return self.default_api.sessions_id_get(id=session_id)
    
    def delete_session(self, session_id: str) -> None:
        """
        删除会话
        
        Args:
            session_id: 会话ID
        """
        self.default_api.sessions_id_delete(id=session_id)
    
    # ==================== 消息管理 ====================
    
    def send_message(
        self,
        session_id: str,
        content: str,
        stream: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        发送消息
        
        Args:
            session_id: 会话ID
            content: 消息内容
            stream: 是否使用流式响应
            **kwargs: 其他参数
            
        Returns:
            响应消息
        """
        body = {
            "content": content,
            "stream": stream,
            **kwargs
        }
        
        return self.default_api.sessions_id_messages_post(
            id=session_id,
            body=body
        )
    
    def get_messages(
        self,
        session_id: str,
        page: int = 1,
        page_size: int = 50
    ) -> List[Any]:
        """
        获取会话消息列表
        
        Args:
            session_id: 会话ID
            page: 页码
            page_size: 每页数量
            
        Returns:
            消息列表
        """
        return self.default_api.messages_session_id_load_get(
            session_id=session_id,
            page=page,
            page_size=page_size
        )
    
    # ==================== 知识文档管理 ====================
    
    def upload_knowledge(
        self,
        kb_id: str,
        file_path: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        上传知识文档
        
        Args:
            kb_id: 知识库ID
            file_path: 文件路径
            **kwargs: 其他参数
            
        Returns:
            上传结果
        """
        # 注意：实际实现需要处理文件上传
        # 这里只是示例接口
        raise NotImplementedError("文件上传功能需要根据实际API实现")
    
    def get_knowledge_list(
        self,
        kb_id: str,
        page: int = 1,
        page_size: int = 20
    ) -> List[Any]:
        """
        获取知识文档列表
        
        Args:
            kb_id: 知识库ID
            page: 页码
            page_size: 每页数量
            
        Returns:
            知识文档列表
        """
        return self.knowledge_api.knowledge_get(
            knowledge_base_id=kb_id,
            page=page,
            page_size=page_size
        )
    
    def delete_knowledge(self, knowledge_id: str) -> None:
        """
        删除知识文档
        
        Args:
            knowledge_id: 知识文档ID
        """
        self.knowledge_api.knowledge_id_delete(id=knowledge_id)
    
    # ==================== FAQ管理 ====================
    
    def add_faq(
        self,
        kb_id: str,
        question: str,
        answer: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        添加FAQ
        
        Args:
            kb_id: FAQ知识库ID
            question: 问题
            answer: 答案
            **kwargs: 其他参数
            
        Returns:
            添加的FAQ信息
        """
        body = {
            "knowledge_base_id": kb_id,
            "question": question,
            "answer": answer,
            **kwargs
        }
        
        return self.faq_api.faq_post(body=body)
    
    def get_faq_list(
        self,
        kb_id: str,
        page: int = 1,
        page_size: int = 20
    ) -> List[Any]:
        """
        获取FAQ列表
        
        Args:
            kb_id: FAQ知识库ID
            page: 页码
            page_size: 每页数量
            
        Returns:
            FAQ列表
        """
        return self.faq_api.faq_get(
            knowledge_base_id=kb_id,
            page=page,
            page_size=page_size
        )
    
    def update_faq(
        self,
        faq_id: str,
        question: Optional[str] = None,
        answer: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        更新FAQ
        
        Args:
            faq_id: FAQ ID
            question: 新问题
            answer: 新答案
            **kwargs: 其他参数
            
        Returns:
            更新后的FAQ信息
        """
        body = {**kwargs}
        
        if question:
            body["question"] = question
        if answer:
            body["answer"] = answer
        
        return self.faq_api.faq_id_put(id=faq_id, body=body)
    
    def delete_faq(self, faq_id: str) -> None:
        """
        删除FAQ
        
        Args:
            faq_id: FAQ ID
        """
        self.faq_api.faq_id_delete(id=faq_id)


# 导出
__all__ = ['WeKnoraClient']
