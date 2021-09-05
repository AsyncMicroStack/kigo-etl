from kigo.etl.mapper.mapping import mapping
from kigo.etl.extractors.fabric import Extract


@mapping
class SomeClass:
    data_1 = Extract.TextSlice[31:43]
    data_2 = Extract.TextSlice[49:61]

