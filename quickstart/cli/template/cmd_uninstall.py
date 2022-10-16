import os
import shutil

import click
from quickstart.helpers import ensure_template_exists

from quickstart.settings import TEMPLATES_FOLDER


@click.command("uninstall", help="Uninstall a template")
@click.argument("template_name")
def command(template_name: str):
    template_path = ensure_template_exists(template_name)
    shutil.rmtree(template_path)
    click.echo("Template %s uninstalled!" % template_name)
