import concurrent.futures

import click
import foxy_grpc.server
import grpc


@click.group()
@click.pass_context
def main(context):
    context.ensure_object(dict)


@main.command()
@click.pass_context
@click.option("--port", default=3333, type=int, help="Port to listen on")
def server(port):
    grpc_server = grpc.server(concurrent.futures.ThreadPoolExecutor())
    servicer = foxy_grpc.server.Server()
    foxy_grpc.pb2.protocol_pb2_grpc.add_StringServiceServicer_to_server(servicer, grpc_server)
    grpc_server.add_insecure_port(f"[::]:{port}")
    grpc_server.start()
    grpc_server.wait_for_termination()


@main.command()
@click.pass_context
@click.argument("server_url", type=str)
def client(server_url):
    pass
