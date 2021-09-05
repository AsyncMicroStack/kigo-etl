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
        cname = next(iter(conf["class"]))Ramzes#2001

        mapping_info = MappingRegistry.mappings[cname]
        return mapping_info

        self.mapping[self._iter_pos]
        self._iter_pos += 1
        return res

    def __iter__(self):
        self._iter_pos = 0
        return self





