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
    def register_class(name, clazz):
        if name not in Container.__MAPPINGS:
            Container.__MAPPINGS[name] = [clazz]
        else:
            Container.__MAPPINGS[name].append(clazz)

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


class StaticAttribute(type):
    def __getattr__(cls, name):
        if name in Container.extractors:
            return FabricExtractors(Container.extractors[name])
        raise Exception(f"Not found extractor <{name}>. Available extractors: {tuple(Container.extractors.keys())}")


class FabricExtractors(metaclass=StaticAttribute):
    def __init__(self, clazz):
        self.clazz = clazz

    def __getitem__(self, item):
        return self.clazz(item)

    def __getattr__(self, item):
        print(item)
        return self.clazz(item)
