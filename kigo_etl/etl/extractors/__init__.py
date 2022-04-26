__all__ = []

from kigo_etl.etl.runtime.registry import  MappingRegistry
from kigo_etl.etl.extractors.operators import ExtractorOperator


class Extractor(ExtractorOperator):

    def call(self, num, raw, obj):
        raise Exception("Not implemented!")
