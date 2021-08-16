import abc


ID_CLASS_MAP = {}


def mapping(object_id, *args, **kwargs):
    def wrapper(class_ref, *args, **kwargs):
        if object_id not in ID_CLASS_MAP:
            ID_CLASS_MAP[object_id] = []
        ID_CLASS_MAP[object_id].append(class_ref)
    return wrapper


class BaseExpression(abc.ABC):
    @abc.abstractmethod
    def get_expression(self):
        pass


class Expression(BaseExpression):
    def __init__(self, expression='', base_object_name='data'):
        self.expression = expression
        self.base_object_name = base_object_name

    def get_expression(self):
        def f(_l):
            return eval(f'{self.base_object_name}{self.expression}', None, _l)
        return f
