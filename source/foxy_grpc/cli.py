import click


@click.group()
@click.pass_context
def main(context):
    context.ensure_object(dict)


@main.command()
@click.pass_context
@click.option("--port", default=3333, type=int, help="Port to listen on")
def server():
    pass

@main.command()
@click.pass_context
@click.argument("server_url", type=str)
def client(server_url):
    pass
