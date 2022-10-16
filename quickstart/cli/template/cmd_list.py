import os

import click
import yaml

from quickstart.models import TemplateConfig
from quickstart.settings import TEMPLATES_FOLDER, VERBOSE


@click.command("list", help="List available project templates")
def command():
    templates = {}

    for template_name in os.listdir(TEMPLATES_FOLDER):
        folder_name = os.path.join(TEMPLATES_FOLDER, template_name)
        template_config_path = os.path.join(folder_name, "template.yml")

        try:
            config = TemplateConfig.from_yaml_file(template_config_path)
        except FileNotFoundError:
            if VERBOSE:
                click.echo(
                    "Missing template config file: %s" % template_config_path, err=True
                )
            continue

        templates[template_name] = {
            "description": config.description,
            "version": config.version,
        }

    print(yaml.safe_dump(templates))
