import concurrent.futures
import logging

import click
import foxy_grpc.pb2.strings_pb2_grpc
import foxy_grpc.server
import grpc


@click.group()
@click.pass_context
def main(context):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    context.ensure_object(dict)


@main.command()
@click.pass_context
@click.option("--port", default=3333, type=int, help="Port to listen on")
def server(context, port):
    grpc_server = grpc.server(concurrent.futures.ThreadPoolExecutor())
    servicer = foxy_grpc.server.Server()
    foxy_grpc.pb2.strings_pb2_grpc.add_StringServiceServicer_to_server(servicer, grpc_server)
    grpc_server.add_insecure_port(f"0.0.0.0:{port}")
    grpc_server.start()
    grpc_server.wait_for_termination()


@main.command()
@click.pass_context
@click.argument("server_url", type=str)
@click.argument("count", type=int)
@click.option("--forever", is_flag=True)
def client(context, server_url, count: int, forever: bool):
    channel = grpc.insecure_channel(server_url)
    stub = foxy_grpc.pb2.strings_pb2_grpc.StringServiceStub(channel)
    logging.info(f'Client stub is {stub}')
    response = stub.GetStrings(foxy_grpc.pb2.strings_pb2.StringRequest(count=5, forever=forever))
    logging.info(f"Response: {response}")
    for string in response:
        logging.info(f"Received string: {string.content}")


@main.command()
@click.pass_context
def sayhi(context):
    channel = grpc.insecure_channel("localhost:3333")
    stub = foxy_grpc.pb2.strings_pb2_grpc.StringServiceStub(channel)
    response = stub.SayHi(foxy_grpc.pb2.strings_pb2.EmptyMessage())
    logging.info(f"Response: {response}")
