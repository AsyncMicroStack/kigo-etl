from kigo.etl.extractors import Extractor
from kigo.etl.runtime.container import extractor


@extractor
class TextSlice(Extractor):

    def __init__(self, segment):
        if type(segment) is slice:
            self.slice = segment
        else:
            self.slice = slice(segment)

    def call(self, num, raw, obj):
        return raw[self.slice]


@extractor
class Expr(Extractor):

    def __init__(self, expression):
        self.expression = expression

    def call(self, num, raw, obj):
        return eval(self.expression)
