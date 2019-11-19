from dateutil import parser
from abc import ABCMeta


class BaseData(metaclass=ABCMeta):
    def __init__(self):
        self._lastmod = None
        self._loc = None

    @property
    def lastmod(self):
        return self._lastmod

    @lastmod.setter
    def lastmod(self, value):
        self._lastmod = parser.isoparse(value) if value is not None else None
