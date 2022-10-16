import click

from quickstart.cli.project import cmd_create

@click.group("project")
def namespace():
    """Namespace that contains commands related to namespace"""

namespace.add_command(cmd_create.command)
