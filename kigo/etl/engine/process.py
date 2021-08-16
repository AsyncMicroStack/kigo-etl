import os
import glob
import logging


from kigo.etl.engine.mapping import ID_CLASS_MAP


RAW_DATA = {}


def start(files_dir):
    if not ID_CLASS_MAP:
        logging.error("Mappings not found, please use proper annotations.")
        return

    load_files(files_dir)


def load_files(files_dir):
    for path in glob.glob(os.path.join(files_dir, '*')):
        if os.path.isfile(path):
            file_name = os.path.basename(path)
            if file_name not in RAW_DATA:
                RAW_DATA[file_name] = []
            with open(path) as f:
                for line in f:
                    RAW_DATA[file_name].append(line.strip())
