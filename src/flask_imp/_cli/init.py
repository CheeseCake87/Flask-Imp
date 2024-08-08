import os
import typing as t
from pathlib import Path

import click

from .blueprint import add_blueprint
from .filelib.favicon import favicon
from .filelib.flask_imp_logo import flask_imp_logo
from .filelib.head_tag_generator import head_tag_generator
from .filelib.water_css import water_css
from .helpers import Sprinkles as Sp


def build(folders: t.Dict[str, t.Any], files: t.Dict[str, t.Any]) -> None:
    for folder, path in folders.items():
        if not path.exists():
            path.mkdir(parents=True)
            click.echo(f"{Sp.OKGREEN}App folder: {folder}, created{Sp.END}")
        else:
            click.echo(
                f"{Sp.WARNING}App folder already exists: {folder}, skipping{Sp.END}"
            )

    for file, (path, content) in files.items():
        if not path.exists():
            if (
                file == "resources/static/favicon.ico"
                or file == "resources/static/img/flask-imp-logo.png"
            ):
                path.write_bytes(bytes.fromhex(content))
                continue

            path.write_text(content, encoding="utf-8")

            click.echo(f"{Sp.OKGREEN}App file: {file}, created{Sp.END}")
        else:
            click.echo(f"{Sp.WARNING}App file already exists: {file}, skipping{Sp.END}")


def minimal_app(app_folder: Path) -> None:
    from .filelib.init import init_minimal_py
    from .filelib.templates import templates_minimal_index_html
    from .filelib.resources import resources_minimal_routes_py

    # Folders
    folders = {
        "root": app_folder,
        "resources": app_folder / "resources",
        "resources/static": app_folder / "resources" / "static",
        "resources/static/css": app_folder / "resources" / "static" / "css",
        "resources/static/img": app_folder / "resources" / "static" / "img",
        "resources/templates": app_folder / "resources" / "templates",
    }

    files = {
        "root/__init__.py": (
            folders["root"] / "__init__.py",
            init_minimal_py(secret_key=os.urandom(24).hex()),
        ),
        "resources/static/favicon.ico": (
            folders["resources/static"] / "favicon.ico",
            favicon,
        ),
        "resources/static/css/main.css": (
            folders["resources/static/css"] / "water.css",
            water_css,
        ),
        "resources/static/img/flask-imp-logo.png": (
            folders["resources/static/img"] / "flask-imp-logo.png",
            flask_imp_logo,
        ),
        "resources/templates/index.html": (
            folders["resources/templates"] / "index.html",
            templates_minimal_index_html(
                head_tag=head_tag_generator(
                    no_js=True,
                ),
                static_path="static",
                index_py=str(folders["resources"] / "index.py"),
                index_html=str(folders["resources/templates"] / "index.html"),
                init_py=str(folders["root"] / "__init__.py"),
            ),
        ),
        "resources/routes.py": (
            folders["resources"] / "routes.py",
            resources_minimal_routes_py(),
        ),
    }

    build(folders, files)


def slim_app(app_folder: Path) -> None:
    from .filelib.init import init_slim_py
    from .filelib.extensions import extensions_init_slim_py
    from .filelib.resources import resources_cli_py
    from .filelib.resources import resources_error_handlers_py
    from .filelib.templates import templates_error_html

    app_name = app_folder.name

    folders = {
        "root": app_folder,
        "extensions": app_folder / "extensions",
        "resources": app_folder / "resources",
        "resources/cli": app_folder / "resources" / "cli",
        "resources/error_handlers": app_folder / "resources" / "error_handlers",
        "resources/static": app_folder / "resources" / "static",
        "resources/static/css": app_folder / "resources" / "static" / "css",
        "resources/static/img": app_folder / "resources" / "static" / "img",
        "resources/templates": app_folder / "resources" / "templates",
    }

    files = {
        "root/__init__.py": (
            folders["root"] / "__init__.py",
            init_slim_py(app_name=app_name, secret_key=os.urandom(24).hex()),
        ),
        "extensions/__init__.py": (
            folders["extensions"] / "__init__.py",
            extensions_init_slim_py(),
        ),
        "resources/cli/cli.py": (
            folders["resources/cli"] / "cli.py",
            resources_cli_py(),
        ),
        "resources/error_handlers/error_handlers.py": (
            folders["resources/error_handlers"] / "error_handlers.py",
            resources_error_handlers_py(),
        ),
        "resources/static/favicon.ico": (
            folders["resources/static"] / "favicon.ico",
            favicon,
        ),
        "resources/templates/error.html": (
            folders["resources/templates"] / "error.html",
            templates_error_html(),
        ),
    }

    build(folders, files)

    add_blueprint(
        name="www",
        _init_app=True,
        _cwd=app_folder,
        _url_prefix="/",
    )


def full_app(app_folder: Path) -> None:
    from .filelib.init import init_full_py
    from .filelib.extensions import extensions_init_full_py
    from .filelib.models import models_example_user_table_py
    from .filelib.resources import resources_cli_py
    from .filelib.resources import resources_error_handlers_py
    from .filelib.resources import resources_context_processors_py
    from .filelib.resources import resources_filters_py
    from .filelib.resources import resources_routes_py

    from .filelib.templates import templates_error_html

    app_name = app_folder.name

    folders = {
        "root": app_folder,
        "blueprints": app_folder / "blueprints",
        "extensions": app_folder / "extensions",
        "models": app_folder / "models",
        "resources": app_folder / "resources",
        "resources/cli": app_folder / "resources" / "cli",
        "resources/context_processors": app_folder / "resources" / "context_processors",
        "resources/error_handlers": app_folder / "resources" / "error_handlers",
        "resources/filters": app_folder / "resources" / "filters",
        "resources/routes": app_folder / "resources" / "routes",
        "resources/static": app_folder / "resources" / "static",
        "resources/static/css": app_folder / "resources" / "static" / "css",
        "resources/static/img": app_folder / "resources" / "static" / "img",
        "resources/templates": app_folder / "resources" / "templates",
    }

    files = {
        "root/__init__.py": (
            folders["root"] / "__init__.py",
            init_full_py(app_name=app_name, secret_key=os.urandom(24).hex()),
        ),
        "extensions/__init__.py": (
            folders["extensions"] / "__init__.py",
            extensions_init_full_py(),
        ),
        "models/example_user_table.py": (
            folders["models"] / "example_user_table.py",
            models_example_user_table_py(app_name=app_name),
        ),
        "resources/cli/cli.py": (
            folders["resources/cli"] / "cli.py",
            resources_cli_py(),
        ),
        "resources/context_processors/context_processors.py": (
            folders["resources/context_processors"] / "context_processors.py",
            resources_context_processors_py(),
        ),
        "resources/error_handlers/error_handlers.py": (
            folders["resources/error_handlers"] / "error_handlers.py",
            resources_error_handlers_py(),
        ),
        "resources/filters/filters.py": (
            folders["resources/filters"] / "filters.py",
            resources_filters_py(),
        ),
        "resources/routes/routes.py": (
            folders["resources/routes"] / "routes.py",
            resources_routes_py(),
        ),
        "resources/static/favicon.ico": (
            folders["resources/static"] / "favicon.ico",
            favicon,
        ),
        "resources/templates/error.html": (
            folders["resources/templates"] / "error.html",
            templates_error_html(),
        ),
    }

    build(folders, files)

    add_blueprint(
        name="www",
        folder="blueprints",
        _init_app=True,
        _cwd=app_folder,
        _url_prefix="/",
    )


def init_app(
    name: str,
    _full: bool = False,
    _slim: bool = False,
    _minimal: bool = False,
) -> None:
    click.echo(f"{Sp.OKGREEN}Creating App: {name}")

    cwd = Path.cwd()

    app_folder = cwd / name

    if app_folder.exists():
        click.echo(f"{Sp.FAIL}{name} folder already exists!{Sp.END}")
        click.confirm("Are you sure you want to continue?", abort=True)

    if _minimal:
        minimal_app(app_folder)
    elif _slim:
        slim_app(app_folder)
    elif _full:
        full_app(app_folder)
    else:
        click.echo(f"{Sp.FAIL}No app type selected!{Sp.END}")
        click.echo(f"{Sp.FAIL}Use --minimal, --slim, or --full{Sp.END}")
        return

    click.echo(" ")
    click.echo(f"{Sp.OKBLUE}==================={Sp.END}")
    click.echo(f"{Sp.OKBLUE}Flask app deployed!{Sp.END}")
    click.echo(f"{Sp.OKBLUE}==================={Sp.END}")
    click.echo(" ")
    if name == "app":
        click.echo(f"{Sp.OKBLUE}Your app has the default name of 'app'{Sp.END}")
        click.echo(f"{Sp.OKBLUE}Flask will automatically look for this!{Sp.END}")
        click.echo(f"{Sp.OKBLUE}Run: flask run --debug{Sp.END}")
    else:
        click.echo(f"{Sp.OKBLUE}Your app has the name of '{name}'{Sp.END}")
        click.echo(f"{Sp.OKBLUE}Run: flask --app {name} run --debug{Sp.END}")
    click.echo(" ")
