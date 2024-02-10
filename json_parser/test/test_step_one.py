from unittest import TestCase
from main import json_parser


class TestJsonParserStepOne(TestCase):

    def setUp(self) -> None:
        self.valid_json_file_path = 'examples/step1/valid.json'
        self.invalid_json_file_path = 'examples/step1/invalid.json'

    def test_valid_json_file(self):
        self.assertTrue(json_parser(self.valid_json_file_path))

    def test_invalid_json_file(self):
        self.assertFalse(json_parser(self.invalid_json_file_path))
