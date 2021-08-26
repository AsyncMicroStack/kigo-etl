import os

class FileLoader:
    __files__ = {}
    __reverse__ = {}

    @classmethod
    def set(cls, name, file_path):
        if not os.path.exists(file_path):
            raise Exception(f"File mapping <{name}>. File not found: <{file_path}>!")
        FileLoader.__files__[name] = file_path
        FileLoader.__reverse__[file_path] = name