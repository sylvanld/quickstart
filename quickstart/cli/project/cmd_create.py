import os
import click
from quickstart.helpers import ensure_template_exists
from quickstart.prompt import prompt_missing_variables

from quickstart.settings import CONFIG_FILE
from quickstart.models import Context, TemplateConfig
from quickstart.templating import FolderTemplatingEngine

@click.command("create", help="Create a new project from template")
@click.argument("project_name")
@click.option(
    "--from", "template_name", required=True, help="Name of the template to be used"
)
@click.option(
    "--path",
    "project_path",
    help="Override default project path (./{project_name})",
)
def command(project_name: str, template_name: str, project_path: str = None):
    template_path = ensure_template_exists(template_name)
    template = TemplateConfig.from_yaml_file(os.path.join(template_path, "template.yml"))
    default_context = Context.from_yaml_file(CONFIG_FILE)
    
    context = prompt_missing_variables(template.variables, default_context)
    context["project_name"] = project_name
    context["project_key"] = project_name.lower().replace("-", "_").replace("-", "_")
    engine = FolderTemplatingEngine(os.path.join(template_path, "template"), context)
    
    if project_path is None:
        project_path = project_name
    
    engine.render_template_folder(project_path)