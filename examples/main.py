from kigo.etl.runtime import runtime
from kigo.etl.configuration import Config
import etl.load


conf = Config.load("load.json")
for mapping_info in conf.mapping:
    print(mapping_info)
    c = mapp.classified
    print(c)




