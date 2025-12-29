"""CLI interface for {{ cookiecutter.package_name }}."""

from typing import Annotated

import typer

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
    message: Annotated[str, typer.Argument(help="Message to display")] = "World!",
) -> None:
    typer.echo(f"Hello, {message.capitalize()}")


if __name__ == "__main__":
    app()
