import pprint
import examples.etl.load

from kigo.etl.runtime import runtime
from kigo.etl.configuration import Config


conf = Config.load("load.json")
db = runtime.process(conf)
pprint.pprint(db.data)
