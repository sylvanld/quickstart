import click

from quickstart.cli import (
    project,
    template,
    cmd_version,
)


@click.group()
def CLI():
    """Command line interface to create projects from templates!"""

CLI.add_command(project.namespace)
CLI.add_command(template.namespace)
CLI.add_command(cmd_version.command)
