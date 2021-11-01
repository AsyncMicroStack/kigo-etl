from functools import wraps
from kigo.etl.file.readers import FileReader


class set_reader:
    def __init__(self, init_values:dict = {}, safe_init=True):
        self.init_values = init_values
        self.safe_init = safe_init

    def __call__(self, fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            # Save original Reader Settings
            original_init_values = FileReader.__init_values__
            original_safe_init = FileReader.__safe_init__

            # Set desired Reader Settings
            FileReader.__init_values__ = self.init_values
            FileReader.__safe_init__ = self.safe_init

            # Execute Function
            result = fun(*args, **kwargs)

            # Revert original Reader Settings
            FileReader.__init_values__ = original_init_values
            FileReader.__safe_init__ = original_safe_init

            # Return execution result
            return result
        return wrapper
#def set_reader(fun):
#    @wraps(fun)
#    def wrapper(*args, **kwargs):