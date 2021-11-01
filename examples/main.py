from kigo.etl.runtime import runtime
from kigo.etl.configuration import Config
import examples.etl.load


conf = Config.load("load.json")
for mapping_info in conf.mapping:
    print(mapping_info)
