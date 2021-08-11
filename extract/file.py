
class file_mapping:
    def __init__(self, file_name):
        self.input_file = file_name

    def __call__(self, original_class):
        original_class.__input_file__ = self.input_file
        return original_class
