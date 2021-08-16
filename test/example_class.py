from kigo.etl.engine.mapping import mapping, Expression


@mapping(object_id='input_1')
class SomeClass:
    data_1 = Expression('[31:43]')
    data_2 = Expression('[49:61]')
