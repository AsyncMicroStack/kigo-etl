from kigo.etl.runtime import runtime
from kigo.etl.configuration import Config
import etl.load



conf = Config.load("load.json")
runtime.process(conf)



