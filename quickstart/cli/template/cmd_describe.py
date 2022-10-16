import os

import click

from quickstart.settings import TEMPLATES_FOLDER


@click.command("describe", help="List available project templates")
@click.argument("template_name")
def command(template_name: str):
    templates = {}

    folder_name = os.path.join(TEMPLATES_FOLDER, template_name)
    template_config_path = os.path.join(folder_name, "template.yml")

    try:
        with open(template_config_path, "r") as template_config_file:
            template_raw_config = template_config_file.read()
    except FileNotFoundError:
        click.echo("Missing template config file: %s" % template_config_path, err=True)
        exit(1)

    print(template_raw_config)
