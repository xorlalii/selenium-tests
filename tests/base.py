import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    base_url = None
    driver = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # create a new Firefox session
        cls.driver = webdriver.Firefox(executable_path="drivers/geckodriver")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def get_url(self, path):
        """
        Takes a path name and return absolute url by concatenating base url and the path name
        :param str path: Path to join to base url
        :return:
        """
        # return "{}/{}".format(self.base_url, path)
        return f"{self.base_url}/{path}"

    def visit(self, path):
        self.driver.get(self.get_url(path))


class DeezerBaseTestCase(BaseTestCase):
    base_url = "https://www.deezer.com/en"


class MystoreBaseTestCase(BaseTestCase):
    base_url = "http://automationpractice.com"


class EbayBaseTestCase(BaseTestCase):
    base_url = "https://www.ebay.co.uk"