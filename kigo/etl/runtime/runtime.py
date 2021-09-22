from kigo.etl.storage.memdb import MemoryDB


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
    db = MemoryDB()
    for mapp in conf.mapping:
        for init_reader in mapp.readers:
            typeof_reader, init = init_reader
            r = typeof_reader(**init)
            for line in r:
                data = ExtractData.extract(mapp.clazz[0], *line)
                db.store(mapp.clazz[0], data)
    return db

def process(conf)->MemoryDB:
    db = process_mapping(conf)
    return db