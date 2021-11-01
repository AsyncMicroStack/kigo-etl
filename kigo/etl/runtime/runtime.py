from kigo.etl.runtime.registry import MappingRegistry


def process(config: dict = {}):
    print(MappingRegistry.mappings)
    print("process")
