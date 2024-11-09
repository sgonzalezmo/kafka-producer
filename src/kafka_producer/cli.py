from typing import Optional

import typer

from kafka_producer import __app_name__, __version__
from kafka_producer.arithmetic.cli import app as arithmetic_app

app = typer.Typer(pretty_exceptions_enable=False)
app.add_typer(arithmetic_app, name="arithmetic")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(  # pylint: disable=W0613
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
