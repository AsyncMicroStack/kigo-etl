from functools import wraps
from kigo.etl.runtime.registry import MappingRegistry


class set_reader:
    def __init__(self, reader, init_values: dict = {}, safe_init=True):
        self.reader = reader
        self.init_values = init_values
        self.safe_init = safe_init

    def __call__(self, fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            for mapping_key in MappingRegistry.mappings:
                for reader in MappingRegistry.mappings[mapping_key].readers:
                    if reader[0] == self.reader:
                        MappingRegistry.mappings[mapping_key].readers = (reader[0], self.init_values)
        return wrapper
