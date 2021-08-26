__all__ = []

from kigo.etl.runtime.container import Container

class MapReference:
    def __init__(self, clazz, reader):
        self.clazz = clazz
        self.reader = reader

    def __repr__(self):
        return f"MapReference<{self.clazz.__qualname__}, {self.reader}>"

def mapping(reader):
    def wrapper(clazz):
        Container.register_map(MapReference(clazz, reader))
        return clazz
    return wrapper