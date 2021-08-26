from test.example_class import *
from kigo.etl.runtime.process import start
from kigo.etl.runtime.storage import get_objects

start('data')

print(get_objects())
