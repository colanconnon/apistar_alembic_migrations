from apistar.backends.sqlalchemy_backend import SQLAlchemyBackend
from typing import Callable
from alembic import command
from alembic.config import Config
from apistar import Command


PRELOAD = True
LOADED = False
MIGRATIONS_DIRECTORY = "migrations"

def init_migrations():
    try:
        os.system("alembic init migrations")
    catch:
        print('please install alembic and run command "apistar initialize"')

def create_revision(db_backend: SQLAlchemyBackend, message: str):
    _run_alembic_command(command.revision,db_backend.engine, db_backend.metadata, message=message, autogenerate=True)

def downgrade(db_backend: SQLAlchemyBackend, revision):
    _run_alembic_command(command.downgrade, db_backend.engine, db_backend.metadata, revision=revision)

def upgrade(db_backend: SQLAlchemyBackend, revision):
    _run_alembic_command(command.upgrade, db_backend.engine, db_backend.metadata, revision=revision)

def show(db_backend: SQLAlchemyBackend, revision):
    _run_alembic_command(command.show, db_backend.engine, db_backend.metadata, rev=revision)


commands = [
    Command('initialize', init_migrations),
    Command('create_revision', create_revision),
    Command('upgrade', upgrade),
    Command('downgrade', downgrade),
    Command('show', show)
]
__version__ = '0.0.6'
