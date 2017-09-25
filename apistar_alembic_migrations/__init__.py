from .commands import create_revision, initialize, downgrade, upgrade, show
from apistar import Command


commands = [
    Command('initialize', initialize),
    Command('create_revision', create_revision),
    Command('upgrade', upgrade),
    Command('downgrade', downgrade),
    Command('show', show)
]

__version__ = '0.0.3'