#!/bin/zsh
python -m grpc_tools.protoc --python_out=. --proto_path=protos/ protos/**/*.proto
python -m grpc_tools.protoc --grpc_python_out=. --proto_path=protos/ protos/**/*.proto