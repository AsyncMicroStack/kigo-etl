__all__ = []

import abc

class Extractor(abc.ABC):

    @abc.abstractmethod
    def call(self, num, raw, obj):
        pass
