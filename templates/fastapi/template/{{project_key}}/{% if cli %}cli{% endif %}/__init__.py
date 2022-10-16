import click

from {{project_key}}.cli import cmd_version

@click.group()
def CLI():
    """CLI description"""
