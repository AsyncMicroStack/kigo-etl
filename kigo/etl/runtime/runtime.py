from kigo.etl.runtime.registry import MappingRegistry


def process(config={}):
    print(MappingRegistry.mappings)
    print("process")
