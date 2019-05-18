import unittest
from selenium import webdriver


class DeezerBaseTestCase(unittest.TestCase):
    base_url = "https://www.deezer.com/en"
    driver = None

    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox(executable_path="drivers/geckodriver")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    # def setUp(self):
    #     # create a new Firefox session
    #     self.driver = webdriver.Firefox(executable_path="drivers/geckodriver")
    #     self.driver.implicitly_wait(5)
    #     self.driver.maximize_window()

    # def tearDown(self):
    #     self.driver.quit()

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


class TestPages(DeezerBaseTestCase):

    def test_home(self):
        self.driver.get(self.base_url)
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual(
            "Deezer - music streaming | Try Flow, download & listen to free music",
            text
        )

    def test_about_us(self):
        self.driver.get(self.get_url("company"))
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual("About us", text)
