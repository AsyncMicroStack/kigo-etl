import unittest
import kigo.test.etl.unittest.resources.entities

from kigo.etl.configuration import Config


class MyTestCase(unittest.TestCase):

    def test_proper_mapping(self):
        # GIVEN
        result = []

        # WHEN
        conf = Config.load("resources/load.json")
        for mapping_info in conf.mapping:
            result.append(str(mapping_info))

        # THEN
        self.assertListEqual(["MappingInfo <[<class 'kigo.test.etl.unittest.resources.entities.SomeClass'>, {}]> readers: [(<class 'kigo.etl.file.readers.TextReader'>, {'path': './data/input_1'})]>",
                              "MappingInfo <[<class 'kigo.test.etl.unittest.resources.entities.SomeClass2'>, {}]> readers: [(<class 'kigo.etl.file.readers.TextReader'>, {'path': './data/input_1'})]>"],
                             result)


if __name__ == '__main__':
    unittest.main()
