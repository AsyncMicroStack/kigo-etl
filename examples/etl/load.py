from kigo.etl.mapper.mapping import mapping
from kigo.etl.mapper.archetype import Archetype
from kigo.etl.extractors.fabric import Extract
from kigo.etl.extractors.operators import ExtractorOperator
from kigo.etl.mapper.keys import Key
import kigo.etl.mapper.typeof as typeof


@mapping
class SomeClass1(ExtractorOperator):
    data_1: Archetype(typeof=typeof.String,
                      key=Key.PrimaryKey
                      ).sql(table="myTable",
                            field="id")       = Extract.TextSlice[31:43]
    data_2                                    = Extract.TextSlice[49:61]

@mapping
class SomeClass2(ExtractorOperator):
    data_1                 = Extract.TextSlice[31:43]
    data_2                 = Extract.TextSlice[49:61]


print(SomeClass1.data_1+SomeClass2.data_2)