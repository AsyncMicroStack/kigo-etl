from kigo.etl.runtime.container import reader
from kigo.etl.file import FileReader
from kigo.etl.file import ReaderType


@reader
class TextReader(FileReader):

    __reader_type__ = ReaderType.TEXT

    def read(self):
        with open(self.path, "r") as f:
            for num, line in enumerate(f.readline()):
                if self.on_read():
                    yield line
