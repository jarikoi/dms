"""The hub command."""


from json import dumps

from .base import Base


class Hub(Base):
    """Say hub, world!"""

    def run(self):
        print 'Hub, world!'
        print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
