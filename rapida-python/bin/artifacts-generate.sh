# python3 -m grpc_tools.protoc -I rapida/artifacts/protos --pyi_out=rapida/artifacts/protos --python_out=rapida/artifacts/protos/ --grpc_python_out=rapida/artifacts/protos/ rapida/artifacts/protos/*.proto


python3 -m grpc.tools.protoc \
    -I ./rapida/artifacts/protos \
    --pyi_out=./rapida/artifacts/protos \
    --python_out=./rapida/artifacts/protos \
    --grpc_python_out=./rapida/artifacts/protos \
    ./rapida/artifacts/protos/*.proto

# Find all .py files and replace the import statement
find "rapida/artifacts/protos/" -name '*.py' -exec sed -i.bak 's/import common_pb2 as common__pb2/import rapida.artifacts.protos.common_pb2 as common__pb2/g' {} +
find "rapida/artifacts/protos/" -name '*.pyi' -exec sed -i.bak 's/import common_pb2 as _common_pb2/import rapida.artifacts.protos.common_pb2 as _common_pb2/g' {} +

find "rapida/artifacts/protos/" -name '*.py' -exec sed -i.bak 's/import web_api_pb2 as web__api__pb2/import rapida.artifacts.protos.web_api_pb2 as web__api__pb2/g' {} +
find "rapida/artifacts/protos/" -name '*.py' -exec sed -i.bak 's/import provider_api_pb2 as provider__api__pb2/import rapida.artifacts.protos.provider_api_pb2 as provider__api__pb2/g' {} +
find "rapida/artifacts/protos/" -name '*.py' -exec sed -i.bak 's/import vault_api_pb2 as vault__api__pb2/import rapida.artifacts.protos.vault_api_pb2 as vault__api__pb2/g' {} +
find "rapida/artifacts/protos/" -name '*.py' -exec sed -i.bak 's/import integration_api_pb2 as integration__api__pb2/import rapida.artifacts.protos.integration_api_pb2 as integration__api__pb2/g' {} +
find "rapida/artifacts/protos/" -name '*.py' -exec sed -i.bak 's/import knowledge_api_pb2 as knowledge__api__pb2/import rapida.artifacts.protos.knowledge_api_pb2 as knowledge__api__pb2/g' {} +
find "rapida/artifacts/protos/" -name '*.py' -exec sed -i.bak 's/import invoker_api_pb2 as invoker__api__pb2/import rapida.artifacts.protos.invoker_api_pb2 as invoker__api__pb2/g' {} +
# Remove backup files created by sed


find "rapida/artifacts/protos/" -name '*.bak' -exec rm {} +