from selenium import webdriver
import time
import unittest

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_equals(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.skip("Testing skip")
    def test_fail(self):
        self.assertEqual(1, 5)

    def test_search_in_python_org(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--log-level=3')

        self.driver.set_window_size(1920, 1080)

        driver = self.driver
        driver.get("https://www.geeksforgeeks.org")
        # self.assertIn("GeeksforGeeks | A computer science portal for geeks", driver.title)
        self.assertIn("GeeksforGeeks | ", driver.title)
        #elem = driver.find_element(By.NAME, "q")
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Done")


if __name__ == "__main__":
    unittest.main()