__all__ = []
from kigo.etl.runtime.container import Container


def mapping(name, *args, **kwargs):
    def wrapper(class_ref, *args, **kwargs):
        Container.register_class(name, class_ref)
        return class_ref
    return wrapper