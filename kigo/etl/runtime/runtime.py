from kigo.etl.runtime.registry import MappingRegistry


class MetaReflection:
    OPERATIONS = {}

    @classmethod
    def operations(cls, clazz):
        if clazz in MetaReflection.OPERATIONS:
            return MetaReflection.OPERATIONS[clazz]
        else:
            MetaReflection.OPERATIONS[clazz] = {}

        for field, oper in clazz.__dict__.items():
            if not field.startswith("__"):
                MetaReflection.OPERATIONS[clazz][field] = oper
        return MetaReflection.OPERATIONS[clazz]


class ExtractData:

    @classmethod
    def extract(cls, clazz, num, data) -> dict:
        unit = {}
        for field, operation in MetaReflection.operations(clazz).items():
            unit[field] = operation.call(num, data, unit)
        return unit

def process_mapping(conf):
    for mapp in conf.mapping:
        for reader in mapp.readers:
            zlass, init = reader
            r = zlass(**init)
            for line in r:
                print(ExtractData.extract(mapp.clazz[0], *line))

def process(conf):
    process_mapping(conf)