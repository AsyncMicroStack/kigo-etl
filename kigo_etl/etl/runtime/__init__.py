__all__ = []


def init():
    __import__("kigo_etl.etl.extractors.slicers", globals(), locals())
    __import__("kigo_etl.etl.file.readers", globals(), locals())
    __import__("kigo_etl.etl.mapper", globals(), locals())


init()
