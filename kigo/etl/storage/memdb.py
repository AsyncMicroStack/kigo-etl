from kigo.etl.mapper.archetype import Archetype

class MemoryDB:

    def __init__(self):
        self.__typeof = {}
        self.__data = {}

    @property
    def data(self):
        return self.__data

    def store(self, typeof, object):
        self.__init_typeof(typeof)
        typeof_keys = self.__typeof[typeof]["keys"]
        if typeof_keys:
            for key_name in typeof_keys:
                self.__append_data(typeof, key_name, object)
        else:
            self.__append_data(typeof, None, object)

    def __append_data(self, typeof, key_name, object):
        if not key_name:
            self.__data[typeof].append(object)
            return
        current = self.__data[typeof][key_name].get(object[key_name], None)
        if not current:
            self.__data[typeof][key_name][object[key_name]] = object
        elif isinstance(current, list):
            self.__data[typeof][key_name][object[key_name]].append(object)
        else:
            self.__data[typeof][key_name][object[key_name]] = [current, object]

    def __init_typeof(self, typeof):
        if typeof not in self.__typeof:
            self.__typeof[typeof] = {"keys": []}
            self.__data[typeof] = {}
            annotations = typeof.__dict__.get("__annotations__", {})
            for key_name, archetype in annotations.items():
                if archetype.key != None:
                    self.__data[typeof][key_name] = {}
                    self.__typeof[typeof]["keys"].append(key_name)
            if not self.__typeof[typeof]["keys"]:
                self.__data[typeof] = []

