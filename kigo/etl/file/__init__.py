__all__ = []

import abc
from enum import Enum

class ReaderType(Enum):
    ABC  = "ABC"
    TEXT = "TEXT"
    CSV  = "CSV"
    XML  = "XML"
    JSON = "JSON"

class FileReader(abc.ABC):

    __reader_type__ = ReaderType.ABC

    @abc.abstractmethod
    def __init__(self, path):
        self.path = path

    @classmethod
    @property
    def type(clr) -> ReaderType:
        return clr.__reader_type__

    def read(self):
        with open(self.path, "r") as f:
            for num, line in enumerate(f.readline()):
                if self.on_read():
                    yield line

    def on_read(self) -> bool:
        """
        For each consistent piece of data.
        If False is returned, the data fragment will be skipped
        :return:
        """
        return True
