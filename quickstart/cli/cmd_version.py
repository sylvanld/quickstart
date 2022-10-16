import click

from quickstart.__about__ import __version__


@click.command("version", help="Get quickstart CLI version")
@click.option("--short", is_flag=True, help="Print only semantic version")
def command(short: bool):
    if short:
        print(__version__)
    else:
        print(__version__ + " +details")
