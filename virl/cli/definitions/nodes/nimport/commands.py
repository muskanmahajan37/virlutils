import click
import os
from virl.api import VIRLServer
from virl.helpers import get_cml_client


@click.command()
@click.argument("node", nargs=1)
@click.option("-f", "--filename", required=True, metavar="<filename>", help="path to the local node definition file")
def nimport(node, filename):
    """
    import a node definition
    """

    server = VIRLServer()
    client = get_cml_client(server)

    if not os.path.isfile(filename):
        click.secho("Node definition file {} does not exist or is not a file", fg="red")
    else:
        defs = client.definitions
        contents = None

        with open(filename, "r") as fd:
            contents = fd.read()

        try:
            defs.upload_node_definition(node, contents)
        except Exception as e:
            click.secho("Failed to import node definition for {}: {}".format(node, e), fg="red")