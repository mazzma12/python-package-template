"""CLI interface for {{ cookiecutter.package_name }}."""

import sys
from pathlib import Path

import click

from .alpacas import AlpacaType, get_alpaca_art, get_available_alpacas
from .formatter import format_message


@click.command()
@click.argument("message", required=False)
@click.option(
    "--alpaca",
    "-a",
    type=click.Choice(get_available_alpacas(), case_sensitive=False),
    default="default",
    help="Choose alpaca type",
)
@click.option(
    "--color",
    "-c",
    type=click.Choice(["red", "green", "blue", "yellow", "magenta", "cyan", "white"]),
    help="Text color",
)
@click.option("--width", "-w", type=int, default=40, help="Maximum width of the speech bubble")
@click.option("--safer-together", is_flag=True, help='Display the special "Safer, Together!" message')
@click.option("--file", "-f", type=click.Path(exists=True, path_type=Path), help="Read message from file")
@click.version_option()
def main(
    message: str | None, alpaca: str, color: str | None, width: int, safer_together: bool, file: Path | None
) -> None:
    """
    {{ cookiecutter.project_name }} - Display messages with ASCII alpacas!

    Examples:
        {{ cookiecutter.cli_name }} "Hello World!"
        {{ cookiecutter.cli_name }} --alpaca happy --color green "I'm happy!"
        {{ cookiecutter.cli_name }} --safer-together
        echo "Hello" | {{ cookiecutter.cli_name }}
    """
    # Determine the message source
    if safer_together:
        text = "Safer, Together!"
    elif file:
        text = file.read_text(encoding="utf-8").strip()
    elif message:
        text = message
    elif not sys.stdin.isatty():
        # Read from stdin
        text = sys.stdin.read().strip()
    else:
        click.echo("Error: No message provided. Use --help for usage information.", err=True)
        sys.exit(1)

    if not text:
        click.echo("Error: Empty message.", err=True)
        sys.exit(1)

    # Get the alpaca type
    try:
        alpaca_type = AlpacaType(alpaca.lower())
    except ValueError:
        click.echo(f"Error: Invalid alpaca type '{alpaca}'", err=True)
        sys.exit(1)

    # Format the message
    formatted_message = format_message(text, width=width, color=color)

    # Get alpaca art
    alpaca_art = get_alpaca_art(alpaca_type)

    # Display the result
    click.echo(formatted_message)
    click.echo(alpaca_art)


if __name__ == "__main__":
    main()
