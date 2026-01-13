#!/bin/bash

# 设置路径
SWAGGER_FILE="WeKnora/docs/swagger.json"
OUTPUT_DIR="WeKnora/python-sdk"

# 检查 Swagger 文件是否存在
if [ ! -f "$SWAGGER_FILE" ]; then
    echo "Error: Swagger file not found at $SWAGGER_FILE"
    exit 1
fi

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 执行生成命令
# packageName: weknora
# projectName: weknora-python-sdk
openapi-generator-cli generate \
    -i "$SWAGGER_FILE" \
    -g python \
    -o "$OUTPUT_DIR" \
    --additional-properties=packageName=weknora,projectName=weknora-python-sdk,packageVersion=1.0.0

echo "Python SDK has been generated in $OUTPUT_DIR"
