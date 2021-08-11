
class file_mapping:
    def __init__(self, file_id):
        self.file_id = file_id

    def __call__(self, original_class):
        original_class.__file_id__ = self.file_id
        return original_class
