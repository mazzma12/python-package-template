from importlib.metadata import version
from typing import Annotated

import typer

app = typer.Typer(
    name="{{ cookiecutter.cli_name }}",
    help="{{ cookiecutter.project_name }} - {{ cookiecutter.project_description }}",
    add_completion=False,
)


def version_callback(value: bool) -> None:
    """Show version and exit."""
    if value:
        app_version = version("lamasay")
        typer.echo(f"{{ cookiecutter.package_name }} version {app_version}")
        raise typer.Exit()


@app.command()
def main(
    message: Annotated[str, typer.Argument(help="Message to display")] = "World!",
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=version_callback,
            is_eager=True,
            help="Show version and exit.",
        ),
    ] = False,
) -> None:
    typer.echo(f"Hello, {message.capitalize()}")


if __name__ == "__main__":
    app()
