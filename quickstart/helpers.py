import os

import click

from quickstart.settings import TEMPLATES_FOLDER

def ensure_template_exists(template_name: str, templates_folder: str = TEMPLATES_FOLDER):
    template_path = os.path.join(templates_folder, template_name)
    if not os.path.exists(template_path):
        click.echo("Template '%s' does not exists in: %s" % (template_name, os.path.abspath(templates_folder)))
        exit(1)
    return template_path
