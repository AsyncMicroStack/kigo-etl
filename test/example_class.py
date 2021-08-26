from kigo.etl.mapping import mapping
from kigo.etl.runtime.container import FabricExtractors as Extract
from kigo.etl.file.loader import FileLoader
from kigo.etl.file.readers import TextReader
import kigo.etl.runtime

kigo.etl.runtime.init()


@mapping(reader=TextReader)
class SomeClass:
    data_1 = Extract.TextSlice[31:43]
    data_2 = Extract.TextSlice[49:61]


FileLoader.set(SomeClass, "./data/input_1")

