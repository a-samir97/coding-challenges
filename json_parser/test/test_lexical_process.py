from unittest import TestCase
from main import lexical_part


class TestLexicalProcess(TestCase):
    def setUp(self) -> None:
        self.json_list = [
            '{"key": "value",}',

            '{ \
            "key": "value", \
            key2: "value"\
            }',

            '{"key": "value"}',

            '{ \
            "key": "value",\
            "key2": "value"\
            }'

        ]

    def test_lexical_process(self):
        result_1 = lexical_part(self.json_list[0])
        # result_2 = lexical_part(self.json_list[1])
        result_3 = lexical_part(self.json_list[2])
        result_4 = lexical_part(self.json_list[3])

        self.assertEqual(result_1, ["key", ":", "value", ","])
        # self.assertEqual(result_2, ["key", ":", "value", ",", "key2", ":", "value"])
        self.assertEqual(result_3, ["key", ":", "value"])
        self.assertEqual(result_4, ["key", ":", "value", ",", "key2", ":", "value"])
