generate_pb2:
	python -m grpc_tools.protoc --proto_path=proto/ --python_out=source/ --grpc_python_out=source/  proto/foxy_grpc/pb2/strings.proto
