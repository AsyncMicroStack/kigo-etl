import json
from kigo.etl.runtime.registry import MappingRegistry
from kigo.etl.mapper.mapping import MappingInfo


class Config:
    __config = {}

    @classmethod
    def load(cls, file_path):
        with open(file_path, "r") as f:
            Config.__config = json.load(f)
        return Config()

    @property
    def mapping(self):
        return Mapping(Config.__config["mapping"])

    def __repr__(self):
        return json.dumps(Config.__config)


class Mapping:
    def __init__(self, mapping):
        self._iter_pos = 0
        self.mapping = mapping

    def __repr__(self):
        return str(self.mapping)

    def __next__(self) -> MappingInfo:
        if not self._iter_pos < len(self.mapping):
            raise StopIteration
        conf = self.mapping[self._iter_pos]
        cname = next(iter(conf["class"]))

        mapping_info = MappingRegistry.mappings[cname]
        self._iter_pos += 1
        return mapping_info

    def __iter__(self):
        self._iter_pos = 0
        return self





