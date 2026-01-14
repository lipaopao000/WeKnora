"""
WeKnora SDK 快捷导入
提供简短的模型类别名，避免使用过长的类名
"""

# 导入所有模型类并创建别名
from weknora_sdk import (
    GithubComTencentWeKnoraInternalTypesAgentConfig as AgentConfig,
    GithubComTencentWeKnoraInternalTypesAgentStep as AgentStep,
    GithubComTencentWeKnoraInternalTypesAnswerStrategy as AnswerStrategy,
    GithubComTencentWeKnoraInternalTypesChunkingConfig as ChunkingConfig,
    GithubComTencentWeKnoraInternalTypesContextCompressionStrategy as ContextCompressionStrategy,
    GithubComTencentWeKnoraInternalTypesContextConfig as ContextConfig,
    GithubComTencentWeKnoraInternalTypesConversationConfig as ConversationConfig,
    GithubComTencentWeKnoraInternalTypesEmbeddingParameters as EmbeddingParameters,
    GithubComTencentWeKnoraInternalTypesExtractConfig as ExtractConfig,
    GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload as FAQBatchUpsertPayload,
    GithubComTencentWeKnoraInternalTypesFAQConfig as FAQConfig,
    GithubComTencentWeKnoraInternalErrorsAppError as AppError,
    GithubComTencentWeKnoraInternalErrorsErrorCode as ErrorCode,
)

# 导出所有别名
__all__ = [
    'AgentConfig',
    'AgentStep',
    'AnswerStrategy',
    'ChunkingConfig',
    'ContextCompressionStrategy',
    'ContextConfig',
    'ConversationConfig',
    'EmbeddingParameters',
    'ExtractConfig',
    'FAQBatchUpsertPayload',
    'FAQConfig',
    'AppError',
    'ErrorCode',
]
