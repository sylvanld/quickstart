import click

from quickstart.cli.template import cmd_describe, cmd_install, cmd_list, cmd_uninstall

@click.group("template")
def namespace():
    """Namespace that contains commands related to templates"""

namespace.add_command(cmd_describe.command)
namespace.add_command(cmd_install.command)
namespace.add_command(cmd_list.command)
namespace.add_command(cmd_uninstall.command)
