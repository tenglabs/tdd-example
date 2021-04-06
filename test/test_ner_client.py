import unittest
from ner_client import NamedEntityClient


class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dic_emp_inp(self):

        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents,dict)

