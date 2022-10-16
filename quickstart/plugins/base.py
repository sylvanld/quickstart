from typing import Callable, List

import click


class CLIPlugin:
    key: str
    help: str

    def get_command(self):
        ...


def plugin_based_command(
    name: str,
    plugins: List[CLIPlugin],
    validators: List[Callable] = None,
    help: str = None,
):
    plugins_keys = set(plugin.key for plugin in plugins)

    if validators is None:
        validators = []

    @click.command(name, help=help)
    def command(**options):
        selected_plugins = set(
            option
            for option, value in options.items()
            if value is not None and option in plugins_keys
        )
        if len(selected_plugins) == 0:
            click.echo(
                "You must specify at least one of: %s"
                % ", ".join(("--" + value for value in plugins_keys)),
                err=True,
            )
            exit(1)
        elif len(selected_plugins) > 1:
            click.echo(
                "You must select only one of: %s"
                % ", ".join(("--" + value for value in selected_plugins)),
                err=True,
            )
            exit(1)

        selected_plugin_key = tuple(selected_plugins)[0]
        plugin_command = next(
            plugin for plugin in plugins if plugin.key == selected_plugin_key
        )

        plugin_argument = options.pop(selected_plugin_key)
        for validator in validators:
            validator(**options)
        plugin_command(plugin_argument, **options)

    for plugin in plugins:
        command = click.option("--" + plugin.key, help=plugin.help)(command)

    return command
