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
    __init_values__ = {}
    __safe_init__   = True

    @abc.abstractmethod
    def __init__(self, path):
        if FileReader.__init_values__:
            if FileReader.__safe_init__:
                for key in FileReader.__init_values__:
                    self.__setattr__(key, FileReader.__init_values__[key])
            else:
                self.__dict__.update(FileReader.__init_values__)
        else:
            self.path = path

    @classmethod
    @property
    def type(cls) -> ReaderType:
        return cls.__reader_type__

    def read(self):
        with open(self.path, "r") as f:
            for num, line in enumerate(f.readline()):
                if self.on_read():
                    yield line

    def on_read(self) -> bool:
        """
        For each consistent piece of examples.
        If False is returned, the examples fragment will be skipped
        :return:
        """
        return True
