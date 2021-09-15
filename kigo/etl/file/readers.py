from kigo.etl.runtime.registry import reader
from kigo.etl.file import FileReader
from kigo.etl.file import ReaderType


@reader
class TextReader(FileReader):

    __reader_type__ = ReaderType.TEXT

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, "r") as f:
            for num, line in enumerate(f):
                yield num, line
