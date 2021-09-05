__all__ = []

import abc
from kigo.etl.runtime.registry import  MappingRegistry

class Extractor(abc.ABC):

    @abc.abstractmethod
    def call(self, num, raw, obj):
        pass
