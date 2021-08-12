from kigo.etl.engine.mapping import bind_id


@bind_id(object_id='input_1')
class SomeClass:
    data_1 = '[31:43]'
    data_2 = '[49:61]'
