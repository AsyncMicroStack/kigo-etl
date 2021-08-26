def reader(clazz):
    Container.register_reader(clazz)
    return clazz


def extractor(clazz):
    Container.register_extractor(clazz)
    return clazz


class Container:
    __MAPPINGS   = {}
    __READERS    = {}
    __EXTRACTORS = {}

    @staticmethod
    def register_map(map_reference):
        print(map_reference)
        if map_reference.clazz.__qualname__ not in Container.__MAPPINGS:
            Container.__MAPPINGS[map_reference.clazz.__qualname__] = map_reference
        else:
            raise Exception(f"Duplicate reader name <{map_reference.clazz.__qualname__}>!")

    @staticmethod
    def register_reader(clazz):
        if clazz.__qualname__ not in Container.__READERS:
            Container.__READERS[clazz.__qualname__] = clazz
        else:
            raise Exception(f"Duplicate reader name <{clazz.__qualname__}>!")

    @staticmethod
    def register_extractor(clazz):
        if clazz.__qualname__ not in Container.__EXTRACTORS:
            Container.__EXTRACTORS[clazz.__qualname__] = clazz
        else:
            raise Exception(f"Duplicate extractor name <{clazz.__qualname__}>!")

    @classmethod
    @property
    def extractors(cls):
        return Container.__EXTRACTORS


class StaticExtractorAttribute(type):
    def __getattr__(cls, name):
        if name in Container.extractors:
            return FabricExtractors(Container.extractors[name])
        raise Exception(f"Not found extractor <{name}>. Available extractors: {tuple(Container.extractors.keys())}")


class FabricExtractors(metaclass=StaticExtractorAttribute):
    def __init__(self, clazz):
        self.clazz = clazz

    def __getitem__(self, item):
        return self.clazz(item)

    def __call__(self, *args, **kwargs):
        return self.clazz(*args, **kwargs)
