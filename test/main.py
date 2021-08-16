from test.example_class import *
from kigo.etl.engine.process import start
from kigo.etl.engine.storage import get_objects

start('data')

print(get_objects())
