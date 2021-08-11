from extract.file import file_mapping


@file_mapping(file_name='input_1')
class SomeClass:
    data_1 = '[31:43]'
    data_2 = '[49:61]'
