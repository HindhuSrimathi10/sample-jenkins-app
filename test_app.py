import unittest
import os

class TestApp(unittest.TestCase):
    
    def test_index_html_exists(self):
        """Test that index.html file exists"""
        self.assertTrue(os.path.exists('index.html'))
    
    def test_requirements_exists(self):
        """Test that requirements.txt exists"""
        self.assertTrue(os.path.exists('requirements.txt'))
    
    def test_app_py_has_content(self):
        """Test that app.py is not empty"""
        file_size = os.path.getsize('app.py')
        self.assertGreater(file_size, 0)
    
    def test_that_will_pass(self):
        """This test will pass"""
        self.assertEqual(1, 1)
    
    # This test will fail - uncomment it later to test failure
    # def test_that_will_fail(self):
    #     """This test will fail"""
    #     self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
