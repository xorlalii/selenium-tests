import time
from tests.base import DeezerBaseTestCase


class TestPages(DeezerBaseTestCase):

    def test_home(self):
        self.visit("")
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

    def test_download(self):
        self.driver.get(self.get_url("download"))
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual("Deezer", text)

    def test_plans(self):
        self.driver.get(self.get_url("offers"))
        time.sleep(5)
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual("Plans", text)

    def test_login(self):
        self.driver.get(self.get_url("login"))
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual(
            "Deezer - music streaming | Try Flow, download & listen to free music",
            text)

    def test_register(self):
        self.driver.get(self.get_url("register"))
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual(
            "Deezer - music streaming | Try Flow, download & listen to free music",
            text)

    def test_features(self):
        self.driver.get(self.get_url("features"))
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual("Features", text)

    def test_press(self):
        self.driver.get(self.get_url("company/press"))
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual("Press", text)
