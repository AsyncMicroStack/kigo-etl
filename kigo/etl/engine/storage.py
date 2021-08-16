import inspect

from kigo.etl.engine.mapping import ID_CLASS_MAP, Expression
from kigo.etl.engine.process import RAW_DATA


def get_objects():
    res = {}
    for object_id in ID_CLASS_MAP:
        for class_key in ID_CLASS_MAP[object_id]:
            if class_key not in res:
                res[class_key] = []

    for object_id in ID_CLASS_MAP:
        for class_key in ID_CLASS_MAP[object_id]:
            res[class_key].extend(__map_raw_data(class_key, input_data=RAW_DATA[object_id]))

    return res


def __map_raw_data(class_key, input_data):
    res = []
    attrs = [elem for elem in class_key.__dict__ if isinstance(class_key.__dict__[elem], Expression)]
    attrs_map = {}
    for attr in attrs:
        attrs_map[attr] = class_key.__dict__[attr].get_expression()

    for line in input_data:
        res.append(
            {attr: attrs_map[attr]({'data': line}) for attr in attrs_map}
        )

    return res