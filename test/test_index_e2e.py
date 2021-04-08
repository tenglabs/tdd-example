import unittest
from selenium import webdriver


class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:5000')

        def tearDown(self):
            self.driver.quit()


        def test_browser_title_contains_app_name(self):
            self.assertIn('Named Entity', self.driver.title)

        
        def test_page_head_named(self):
            heading = self._find("heading")
            self.assertEqual('Named Entity')



        def test_page_has_input_for_text(self):
            input_element = self.find('input-text')
            self.assertIsNotNone(input_element)



        def test_page_has_table(self):
            input_element = self._find('input-text')
            submit_button = self._find('find-button')
            input_element.send_keys('France and Germany share a border in Europe')
            submit_button.click()
            table = self._find('ner-table')
            self.assertIsNotNone(table)

        
        def _find(self, val):
            return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')

        
        