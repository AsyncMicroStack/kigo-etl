import os.path
import logging

from kigo_etl.etl.storage.memdb import MemoryDB
from kigo_etl.etl.runtime.registry import MappingRegistry
from kigo_etl.etl.extractors import Extractor
from kigo_persistence.persistence.sql.sqlite.query import SQLiteDB, SQLitePool, SQLiteQuery


class MetaReflection:
    OPERATIONS = {}

    @classmethod
    def operations(cls, clazz):
        if clazz in MetaReflection.OPERATIONS:
            return MetaReflection.OPERATIONS[clazz]
        else:
            MetaReflection.OPERATIONS[clazz] = {}

        for field, oper in clazz.__dict__.items():
            if not field.startswith("__"):
                MetaReflection.OPERATIONS[clazz][field] = oper
        return MetaReflection.OPERATIONS[clazz]


class ExtractData:

    @classmethod
    def extract(cls, clazz, num, data) -> dict:
        unit = {}
        for field, operation in MetaReflection.operations(clazz).items():
            unit[field] = ExtractData.__evaluate_operation__(operation, num, data, unit)
        return unit

    @staticmethod
    def __evaluate_operation__(operations, num, data, unit):
        if isinstance(operations, tuple):
            return operations[0](ExtractData.__evaluate_operation__(operations[1], num, data, unit),
                                   ExtractData.__evaluate_operation__(operations[2], num, data, unit))

        elif isinstance(operations, Extractor):
            return operations.call(num, data, unit)

        return operations


def check_readers():
    non_existing_file = []
    for mapp in MappingRegistry.mappings:
        for init_reader in MappingRegistry.mappings[mapp].readers:
            typeof_reader, init = init_reader
            if not os.path.exists(init["path"]):
                non_existing_file.append(init['path'])
    return non_existing_file


def process_mapping(process_data_callback, finalize_callback):
    """
    Example declare fun_callback: def fun_callback(num:int, mapp:str, data: T[list, dict])
    :param process_data_callback:
    :return:
    """
    non_existing_file = check_readers()
    logging.debug(f"non-existing files: {non_existing_file}")

    for mapp in MappingRegistry.mappings:
        logging.info(mapp)
        for init_reader in MappingRegistry.mappings[mapp].readers:
            typeof_reader, init = init_reader
            if init["path"] in non_existing_file:
                continue
            reader = typeof_reader(**init)
            num = 0
            for num, line in enumerate(reader):
                data = ExtractData.extract(MappingRegistry.mappings[mapp].clazz[0], *line)
                process_data_callback(num, mapp, data, line)
            if finalize_callback:
                finalize_callback(num, mapp)


def process(process_data_callback, finalize_callback = None, config = None):
    """
    Example declare fun_callback: def fun_callback(num:int, mapp:str, data: T[list, dict])
    :param fun_callback:
    :param config:
    :return:
    """
    process_mapping(process_data_callback, finalize_callback)

