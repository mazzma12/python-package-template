"""CLI interface for {{ cookiecutter.package_name }}."""

import sys
from pathlib import Path
from typing import Annotated, Optional

import typer

from {{ cookiecutter.package_name }}.alpacas import AlpacaType, get_alpaca_art, get_available_alpacas
from {{ cookiecutter.package_name }}.formatter import format_message


app = typer.Typer(
    name="{{ cookiecutter.cli_name }}",
    help="{{ cookiecutter.project_name }} - Display messages with ASCII alpacas!",
    add_completion=False,
)


def version_callback(value: bool) -> None:
    """Show version and exit."""
    if value:
        typer.echo("{{ cookiecutter.package_name }} version {{ cookiecutter.version }}")
        raise typer.Exit()


@app.command()
def main(
    message: Annotated[Optional[str], typer.Argument(help="Message to display")] = None,
    alpaca: Annotated[
        str,
        typer.Option(
            "--alpaca",
            "-a",
            help="Choose alpaca type",
        ),
    ] = "default",
    color: Annotated[
        Optional[str],
        typer.Option(
            "--color",
            "-c",
            help="Text color",
        ),
    ] = None,
    width: Annotated[
        int,
        typer.Option(
            "--width",
            "-w",
            help="Maximum width of the speech bubble",
        ),
    ] = 40,
    safer_together: Annotated[
        bool,
        typer.Option(
            "--safer-together",
            help='Display the special "Safer, Together!" message',
        ),
    ] = False,
    file: Annotated[
        Optional[Path],
        typer.Option(
            "--file",
            "-f",
            help="Read message from file",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ] = None,
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            callback=version_callback,
            is_eager=True,
            help="Show version and exit",
        ),
    ] = None,
) -> None:
    """
    {{ cookiecutter.project_name }} - Display messages with ASCII alpacas!

    Examples:

        {{ cookiecutter.cli_name }} "Hello World!"

        {{ cookiecutter.cli_name }} --alpaca happy --color green "I'm happy!"

        {{ cookiecutter.cli_name }} --safer-together

        echo "Hello" | {{ cookiecutter.cli_name }}
    """
    # Validate alpaca type
    available_alpacas = get_available_alpacas()
    if alpaca not in available_alpacas:
        typer.echo(
            f"Error: Invalid alpaca type '{alpaca}'. Available types: {', '.join(available_alpacas)}",
            err=True,
        )
        raise typer.Exit(1)

    # Validate color
    valid_colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]
    if color and color not in valid_colors:
        typer.echo(
            f"Error: Invalid color '{color}'. Available colors: {', '.join(valid_colors)}",
            err=True,
        )
        raise typer.Exit(1)

    # Determine the message source
    if safer_together:
        text = "Safer, Together!"
    elif file:
        try:
            text = file.read_text(encoding="utf-8").strip()
        except Exception as e:
            typer.echo(f"Error reading file: {e}", err=True)
            raise typer.Exit(1)
    elif message:
        text = message
    elif not sys.stdin.isatty():
        # Read from stdin
        text = sys.stdin.read().strip()
    else:
        typer.echo("Error: No message provided. Use --help for usage information.", err=True)
        raise typer.Exit(1)

    if not text:
        typer.echo("Error: Empty message.", err=True)
        raise typer.Exit(1)

    # Get the alpaca type
    try:
        alpaca_type = AlpacaType(alpaca.lower())
    except ValueError:
        typer.echo(f"Error: Invalid alpaca type '{alpaca}'", err=True)
        raise typer.Exit(1)

    # Format the message
    formatted_message = format_message(text, width=width, color=color)

    # Get alpaca art
    alpaca_art = get_alpaca_art(alpaca_type)

    # Display the result
    typer.echo(formatted_message)
    typer.echo(alpaca_art)


if __name__ == "__main__":
    app()
