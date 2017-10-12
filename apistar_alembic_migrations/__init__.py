from apistar.backends.sqlalchemy_backend import SQLAlchemyBackend
from typing import Callable
from alembic import command
from alembic.config import Config
from apistar import Command


PRELOAD = True
LOADED = False
MIGRATIONS_DIRECTORY = "migrations"

def _get_alembic_config(engine, config_file="alembic.ini"):
    alembic_cfg = Config(config_file)
    alembic_cfg.set_main_option("script_location",
                                MIGRATIONS_DIRECTORY)
    alembic_cfg.set_main_option("sqlalchemy.url", str(engine.url))
    return alembic_cfg

def _run_alembic_command(alembic_cmd: Callable, engine, metadata, *args, **kwargs):
    alembic_cfg = _get_alembic_config(engine)
    with engine.begin() as connection:
        alembic_cfg.attributes['target_metadata'] = metadata
        alembic_cfg.attributes['connection'] = connection
        alembic_cmd(alembic_cfg, *args, **kwargs)

def create_revision(db_backend: SQLAlchemyBackend, message: str):
    _run_alembic_command(command.revision,db_backend.engine, db_backend.metadata, message=message, autogenerate=True)

def initialize(db_backend: SQLAlchemyBackend):
    _run_alembic_command(command.init, db_backend.engine, db_backend.metadata, directory=MIGRATIONS_DIRECTORY)

def downgrade(db_backend: SQLAlchemyBackend, revision):
    _run_alembic_command(command.downgrade, db_backend.engine, db_backend.metadata, revision=revision)

def upgrade(db_backend: SQLAlchemyBackend, revision):
    _run_alembic_command(command.upgrade, db_backend.engine, db_backend.metadata, revision=revision)

def show(db_backend: SQLAlchemyBackend, revision):
    _run_alembic_command(command.show, db_backend.engine, db_backend.metadata, rev=revision)


commands = [
    Command('initialize', initialize),
    Command('create_revision', create_revision),
    Command('upgrade', upgrade),
    Command('downgrade', downgrade),
    Command('show', show)
]
__version__ = '0.0.3'