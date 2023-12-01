import click

from .blueprint import add_blueprint as _add_blueprint
from .helpers import Sprinkles as Sp
from .init import init_app as _init_app


@click.group()
def cli():
    pass  # Entry Point


@cli.command("blueprint", help="Create a flask-imp blueprint")
@click.option(
    "-f",
    "--folder",
    nargs=1,
    default="Current Working Directory",
    prompt=(
        f"\n{Sp.WARNING}(Creation is relative to the current working directory){Sp.END}\n"
        f"Folder to create blueprint in"
    ),
    help="The from_folder to create the blueprint in, defaults to the current working directory",
)
@click.option(
    "-n",
    "--name",
    nargs=1,
    default="my_new_blueprint",
    prompt="Name of the blueprint to create",
    help="The name of the blueprint to create",
)
def add_blueprint(folder, name):
    _add_blueprint(folder, name)


@cli.command("init", help="Create a new flask-imp app")
@click.option(
    "-n",
    "--name",
    nargs=1,
    default="app",
    prompt="What would you like to call your app?",
    help="The name of the app folder that will be created",
)
@click.option("-s", "--slim", is_flag=True, default=False, help="Create a slim app")
@click.option(
    "-m", "--minimal", is_flag=True, default=False, help="Create a minimal app"
)
def init_new_app(name, slim, minimal):
    if minimal:
        slim = True
    _init_app(name, slim, minimal)