import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):


    def test_get_ents_returns_dic_emp_str(self):
        model = NerModelTestDouble('eng')
        model.return_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)


    def test_get_ents_ret_dic_nonempty(self):
        model = NerModelTestDouble('eng')
        model.return_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Data")
        self.assertIsInstance(ents, dict)


    def test_get_ents_g_s_PERSON_returned_serializes(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text':'Laurent Fressinet', 'label_':'PERSON'}]
        model.return_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('')
        expected_result = {'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], 'html': ""  }
        self.assertListEqual(result['ents'], expected_result['ents'])