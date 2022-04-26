import os.path

from kigo_etl.etl.runtime.registry import reader
from kigo_etl.etl.file import FileReader
from kigo_etl.etl.file import ReaderType
import logging

@reader
class TextReader(FileReader):

    __reader_type__ = ReaderType.TEXT

    def __init__(self, path):
        self.path = path
        self.file_name = os.path.basename(path)

    def read(self):
        with open(self.path, "r") as f:
            check=100000
            for num, line in enumerate(f):
                if check == 0:
                    logging.info(f'File {self.file_name} Read {num:,} lines.')
                    check = 100000
                check -= 1
                yield num, line


@reader
class TextBlockReader(FileReader):

    __reader_type__ = ReaderType.TEXT

    def __init__(self, path, length):
        self.path = path
        self.length = length
        self.file_name = os.path.basename(path)

    def read(self):
        with open(self.path, "r") as f:
            check = 100000
            num = 0
            while line := f.read(self.length):
                if check == 0:
                    logging.info(f'File {self.file_name} Read {num:,} lines.')
                    check = 100000
                check -= 1
                yield num, line