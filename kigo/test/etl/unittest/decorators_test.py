import unittest
import kigo.test.etl.unittest.resources.entities

from kigo.etl.configuration import Config
from kigo.etl.runtime.registry import MappingRegistry
from kigo.etl.unittest.decorators import set_reader
from kigo.etl.file.readers import TextReader


class MyTestCase(unittest.TestCase):

    def test_proper_mapping(self):
        # GIVEN
        result = []

        # WHEN
        conf = Config.load("resources/load.json")
        for mapping_key in MappingRegistry.mappings:
            result.append(str(MappingRegistry.mappings[mapping_key]))

        # THEN
        self.assertListEqual(["MappingInfo <[<class 'kigo.test.etl.unittest.resources.entities.SomeClass'>, {}]> readers: [(<class 'kigo.etl.file.readers.TextReader'>, {'path': './data/input_1'})]>",
                              "MappingInfo <[<class 'kigo.test.etl.unittest.resources.entities.SomeClass2'>, {}]> readers: [(<class 'kigo.etl.file.readers.TextReader'>, {'path': './data/input_1'})]>"],
                             result)

    @set_reader(TextReader, init_values={'path': './data/input_2'})
    def test_proper_mapping_with_set_reader(self):
        # GIVEN
        result = []

        # WHEN
        conf = Config.load("resources/load.json")
        for mapping_key in MappingRegistry.mappings:
            result.append(str(MappingRegistry.mappings[mapping_key]))

        # THEN
        self.assertListEqual(["MappingInfo <[<class 'kigo.test.etl.unittest.resources.entities.SomeClass'>, {}]> readers: [(<class 'kigo.etl.file.readers.TextReader'>, {'path': './data/input_2'})]>",
                              "MappingInfo <[<class 'kigo.test.etl.unittest.resources.entities.SomeClass2'>, {}]> readers: [(<class 'kigo.etl.file.readers.TextReader'>, {'path': './data/input_2'})]>"],
                             result)


if __name__ == '__main__':
    unittest.main()
