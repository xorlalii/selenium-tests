import time

from tests.base import MystoreBaseTestCase


class TestPages(MystoreBaseTestCase):

    def test_home_page(self):
        self.visit("index.php")
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        self.assertEqual("My Store", text)


class TestSearch(MystoreBaseTestCase):

    def test_valid_search_input(self):
        self.visit("index.php")
        # find search box and fill it with 'shirts'
        search_box = self.driver.find_element_by_name("search_query")
        search_box.send_keys("shirts")
        search_box.submit()
        # click on search icon
        #self.driver.find_element_by_name("submit_search").click()
        time.sleep(2)
        search_header = self.driver.find_element_by_xpath(
            "//div[@id='center_column']/h1/span"
        )
        self.assertIn("shirts", search_header.text.lower())
        for el in self.driver.find_elements_by_xpath("//h5[@itemprop='name']"):
            self.assertIn("shirts", el.text.lower())

    def test_invalid_search_input(self):
        self.visit("index.php")
        # find search box and fill it with '1213'
        search_box = self.driver.find_element_by_name("search_query")
        test_data= 234
        search_box.send_keys(test_data)
        # click on search icon
        self.driver.find_element_by_name("submit_search").click()
        time.sleep(2)
        search_alert_box = self.driver.find_element_by_xpath("//div[@id='center_column']/p")
        expected = f'No results were found for your search "{test_data}"'
        self.assertEqual(expected, search_alert_box.text)

    def test_empty_search_input(self):
        self.visit("index.php")
        # find search box and fill it with '1213'
        search_box = self.driver.find_element_by_name("search_query")
        test_data = ""
        search_box.send_keys(test_data)
        # click on search icon
        self.driver.find_element_by_name("submit_search").click()
        time.sleep(2)
        search_alert_box = self.driver.find_element_by_xpath("//div[@id='center_column']/p")
        expected = "Please enter a search keyword"
        self.assertEqual(expected, search_alert_box.text)


class TestProduct(MystoreBaseTestCase):

    def test_product_view(self):
        self.visit("index.php")

        list_name = self.driver.find_element_by_xpath("//h5[@itemprop='name']").text
        list_price = self.driver.find_element_by_xpath("//ul[@id='homefeatured']/li/div/div[2]/div/span").text

        first_product = self.driver.find_element_by_css_selector(f"#homefeatured li")
        first_product.click()

        detail_name = self.driver.find_element_by_xpath("//h1[@itemprop='name']").text
        detail_price = self.driver.find_element_by_id("our_price_display").text
        self.assertEqual(list_name, detail_name)
        self.assertEqual(list_price, detail_price)
        self.assertTrue(self.driver.find_element_by_name("Submit").is_displayed())

    def test_cart(self):
        self.visit("index.php")
        first_product = self.driver.find_element_by_css_selector(f"#homefeatured li")
        first_product.click()
        # add to cart
        self.driver.find_element_by_name("Submit").click()
        time.sleep(2)
        success_popup_message = self.driver.find_element_by_xpath("//div[@id='layer_cart']/div/div/h2").text
        success_popup_product_name = self.driver.find_element_by_xpath("//div[@id='layer_cart']/div/div/div/span").text

        expected_message = "Product successfully added to your shopping cart"
        detail_name = self.driver.find_element_by_xpath("//h1[@itemprop='name']").text

        self.assertEqual(expected_message, success_popup_message)
        self.assertEqual(success_popup_product_name, detail_name)

