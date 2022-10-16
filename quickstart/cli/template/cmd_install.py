import os

import click

from quickstart.plugins.base import plugin_based_command
from quickstart.plugins.install import GitIntallPlugin, TarIntallPlugin
from quickstart.settings import TEMPLATES_FOLDER


def ensure_template_folder_available(template_name: str, **options):
    template_path = os.path.join(TEMPLATES_FOLDER, template_name)
    if os.path.exists(template_path):
        click.echo(
            "Template '%s' already exists in: %s"
            % (template_name, os.path.abspath(TEMPLATES_FOLDER)),
            err=True,
        )
        click.echo("You can delete it running: template uninstall %s" % template_name)
        exit(1)


command = plugin_based_command(
    "install",
    help="Install a new template for subsequent usage",
    plugins=(
        TarIntallPlugin(),
        GitIntallPlugin(),
    ),
    validators=[ensure_template_folder_available],
)

command = click.argument("template_name")(command)
