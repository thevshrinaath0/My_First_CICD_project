#!/usr/bin/env python

"""
Main cli or app entry point
"""

from mylib.calculator import add, subtract
import click


@click.group()
def cli():
    """Simple calculator app"""
    pass

@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    """Add two numbers together

    Example:
        ./main.py add 1 2
    """

    click.echo(click.style(str(add(a, b)), fg="green"))


@click.command("subtract")
@click.argument("a", type=int)
@click.argument("b", type=int)
def sub_cli(a, b):
    """Subtract two numbers together

    Example:
        ./main.py subtract 1 2
    """

    click.echo(click.style(str(subtract(a, b)), fg="green"))


@cli.command("both")
@click.argument("a", type=int)
@click.argument("b", type=int)
def both_cli(a, b):
    """Show both addition and subtraction results

    Example:
        python main.py both 5 3
    """
    add_result = add(a, b)
    sub_result = subtract(a, b)

    click.echo(click.style(f"Sum: {add_result}", fg="green"))
    click.echo(click.style(f"Difference: {sub_result}", fg="yellow"))
if __name__ == "__main__":
    cli()

    # pylint: disable=no-value-for-parameter
