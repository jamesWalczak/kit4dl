import importlib.resources
import logging
import os
import shutil

import toml
import typer
from typing_extensions import Annotated

from mlkit.nn.confmodels import Conf
from mlkit.nn.trainer import Trainer

_app = typer.Typer(name="MLKit")

log = logging.getLogger("MLKit.CLI")


@_app.command()
def init(
    name: Annotated[
        str, typer.Option(help="The name of your new project")
    ] = "new_mlkit_project"
) -> None:
    """Create a new MLKit project."""
    log.info("MLKit Creating a new skeleton for the project: << %s >>", name)
    empty_proj_path = importlib.resources.path(
        "mlkit.cli._templates", "project"
    )
    shutil.copytree(empty_proj_path, name)


def _get_conf_from_file(conf):
    with open(conf, "rt") as file:
        return Conf(**toml.load(file))


@_app.command()
def train(
    conf: Annotated[
        str, typer.Option(help="Path to the configuration TOML file")
    ] = None
) -> None:
    """Train using the configuration file"""
    log.info("Attept to run training...")
    if not conf:
        log.info(
            (
                "--conf argument was not specified. looking for `conf.toml`"
                " file in the current directory: %s"
            ),
            os.getcwd(),
        )
        conf = os.path.join(".", "conf.toml")
        if not os.path.exists(conf):
            raise RuntimeError(
                "you haven't specified --conf argument and no `conf.toml`"
                f" file was found in the current directory: {os.getcwd()}"
            )
    else:
        if not os.path.exists(conf):
            raise RuntimeError(
                f"the conf file you specified: {conf} does not exist"
            )
    conf_ = _get_conf_from_file(conf)
    log.info("Running trainer...")
    Trainer(conf=conf_).prepare().fit()
    log.info("Training finished")


def run():
    _app()