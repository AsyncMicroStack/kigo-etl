from kigo.etl.mapping import mapping
from kigo.etl.runtime.container import FabricExtractors as Extract
from kigo.etl.file.loader import FileLoader
import kigo.etl.runtime

from kigo.etl.runtime.container import FabricExtractors

kigo.etl.runtime.init()

print(Extract.Expr)

@mapping(name='input_1')
class SomeClass:
    data_1 = Extract.TextSlice[31:43]
    data_2 = Extract.TextSlice[49:61]
    d = Extract.Expr("raw[1:5]")


FileLoader.set("input_1", "./data/input_1")

