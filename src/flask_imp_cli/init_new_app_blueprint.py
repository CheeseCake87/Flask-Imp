from pathlib import Path
import click

from .helpers import to_snake_case
from .helpers import Sprinkles as Sp
from .filelib import BlueprintFileLib, flask_imp_logo
from .filelib import InitAppBlueprintFileLib


def init_new_app_blueprint(folder, name):
    cwd = Path.cwd()
    if folder != "Current Working Directory":
        cwd = Path(cwd / folder)
    if not cwd.exists():
        click.echo(
            f"{Sp.FAIL}{folder} does not exist.{Sp.END}")
        return

    name = to_snake_case(name)

    # Prepare blueprint folder structure
    bp_folder = cwd / name
    bp_routes_folder = bp_folder / "routes"
    bp_templates_folder = bp_folder / "templates" / name

    # Prepare blueprint files
    bp_init_py = bp_folder / "__init__.py"
    bp_config_toml = bp_folder / "config.toml"
    bp_routes_index_py = bp_routes_folder / "index.py"
    bp_templates_index_html = bp_templates_folder / "index.html"

    # Prepare blueprint folders for loop creation
    folders = (
        bp_folder,
        bp_routes_folder,
        bp_templates_folder,
    )

    # Loop create folders
    for folder in folders:
        if not folder.exists():
            folder.mkdir(parents=True)
            click.echo(f"{Sp.OKGREEN}Blueprint folder: {folder.name}, created{Sp.END}")
        else:
            click.echo(f"{Sp.WARNING}Blueprint folder already exists: {folder.name}, skipping{Sp.END}")

    # Create __init__.py
    if not bp_init_py.exists():
        bp_init_py.write_text(BlueprintFileLib.init_py, encoding="utf-8")
        click.echo(f"{Sp.OKGREEN}Blueprint __init__ created{Sp.END}")
    else:
        click.echo(f"{Sp.WARNING}Blueprint __init__ already exists, skipping{Sp.END}")

    # Create config.toml
    if not bp_config_toml.exists():
        bp_config_toml.write_text(
            InitAppBlueprintFileLib.config_toml.format(
                name=name,
                url_prefix="",
            ), encoding="utf-8"
        )
        click.echo(f"{Sp.OKGREEN}Blueprint config, created{Sp.END}")
    else:
        click.echo(f"{Sp.WARNING}Blueprint config already exists, skipping{Sp.END}")

    # Create blueprint index.py route
    if not bp_routes_index_py.exists():
        bp_routes_index_py.write_text(
            BlueprintFileLib.routes_index_py, encoding="utf-8")
        click.echo(f"{Sp.OKGREEN}Blueprint route: {bp_routes_index_py.name}, created{Sp.END}")
    else:
        click.echo(f"{Sp.WARNING}Blueprint route already exists: {bp_routes_index_py.name}, skipping{Sp.END}")

    # Create blueprint index.html template
    if not bp_templates_index_html.exists():
        bp_templates_index_html.write_text(
            InitAppBlueprintFileLib.templates_index_html.format(name=name, flask_imp_logo=flask_imp_logo), encoding="utf-8")
        click.echo(f"{Sp.OKGREEN}Blueprint template file: {bp_templates_index_html.name}, created{Sp.END}")
    else:
        click.echo(
            f"{Sp.WARNING}Blueprint template file already exists: {bp_templates_index_html.name}, skipping{Sp.END}")

    click.echo(f"{Sp.OKGREEN}Blueprint created: {bp_folder}{Sp.END}")



def slim_init_new_app_blueprint(folder, name):
    cwd = Path.cwd()
    if folder != "Current Working Directory":
        cwd = Path(cwd / folder)
    if not cwd.exists():
        click.echo(
            f"{Sp.FAIL}{folder} does not exist.{Sp.END}")
        return

    name = to_snake_case(name)

    # Prepare blueprint folder structure
    bp_folder = cwd / name
    bp_routes_folder = bp_folder / "routes"
    bp_templates_folder = bp_folder / "templates" / name

    # Prepare blueprint files
    bp_init_py = bp_folder / "__init__.py"
    bp_config_toml = bp_folder / "config.toml"
    bp_routes_index_py = bp_routes_folder / "index.py"
    bp_templates_index_html = bp_templates_folder / "index.html"

    # Prepare blueprint folders for loop creation
    folders = (
        bp_folder,
        bp_routes_folder,
        bp_templates_folder,
    )

    # Loop create folders
    for folder in folders:
        if not folder.exists():
            folder.mkdir(parents=True)
            click.echo(f"{Sp.OKGREEN}Blueprint folder: {folder.name}, created{Sp.END}")
        else:
            click.echo(f"{Sp.WARNING}Blueprint folder already exists: {folder.name}, skipping{Sp.END}")

    # Create __init__.py
    if not bp_init_py.exists():
        bp_init_py.write_text(BlueprintFileLib.init_py, encoding="utf-8")
        click.echo(f"{Sp.OKGREEN}Blueprint __init__ created{Sp.END}")
    else:
        click.echo(f"{Sp.WARNING}Blueprint __init__ already exists, skipping{Sp.END}")

    # Create config.toml
    if not bp_config_toml.exists():
        bp_config_toml.write_text(
            InitAppBlueprintFileLib.config_toml.format(
                name=name,
                url_prefix="",
            ), encoding="utf-8"
        )
        click.echo(f"{Sp.OKGREEN}Blueprint config, created{Sp.END}")
    else:
        click.echo(f"{Sp.WARNING}Blueprint config already exists, skipping{Sp.END}")

    # Create blueprint index.py route
    if not bp_routes_index_py.exists():
        bp_routes_index_py.write_text(
            BlueprintFileLib.routes_index_py, encoding="utf-8")
        click.echo(f"{Sp.OKGREEN}Blueprint route: {bp_routes_index_py.name}, created{Sp.END}")
    else:
        click.echo(f"{Sp.WARNING}Blueprint route already exists: {bp_routes_index_py.name}, skipping{Sp.END}")

    # Create blueprint index.html template
    if not bp_templates_index_html.exists():
        bp_templates_index_html.write_text(
            InitAppBlueprintFileLib.templates_index_html.format(name=name, flask_imp_logo=flask_imp_logo), encoding="utf-8")
        click.echo(f"{Sp.OKGREEN}Blueprint template file: {bp_templates_index_html.name}, created{Sp.END}")
    else:
        click.echo(
            f"{Sp.WARNING}Blueprint template file already exists: {bp_templates_index_html.name}, skipping{Sp.END}")

    click.echo(f"{Sp.OKGREEN}Blueprint created: {bp_folder}{Sp.END}")
