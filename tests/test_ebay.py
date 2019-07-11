import time

from selenium.webdriver.common.action_chains import ActionChains
from tests.base import EbayBaseTestCase


class TestHomePage(EbayBaseTestCase):

    def test_home_page(self):
        self.visit("")
        title = self.driver.find_element_by_tag_name("title")
        text = title.get_attribute("text")
        expected = "Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay"
        self.assertEqual(expected, text)


class TestSearch(EbayBaseTestCase):

    def do_search(self, query="macbook"):
        self.visit("")
        time.sleep(3)
        search_box = self.driver.find_element_by_id("gh-ac")
        search_box.send_keys(query)
        search_box.submit()

    def get_listings(self):
        results_list = self.driver.find_elements_by_xpath("//div[@id='ResultSetItems']/ul/li")
        # result_count = len(results_list)
        return results_list

    def test_search(self):
        self.do_search()
        # verify listings attr are present
        for item in self.get_listings():
            postage_price = item.find_element_by_xpath(".//li[@class='lvshipping']/span")
            bid_num = item.find_element_by_xpath(".//li[@class='lvformat']/span")
            price = item.find_element_by_xpath(".//li[contains(@class, 'lvprice')]/span")
            self.assertTrue(postage_price.is_displayed() or bid_num.is_displayed() or price.is_displayed())

    def test_lowest_price_sort(self):
        self.do_search()
        # time.sleep(5)
        sort_menu = self.driver.find_element_by_xpath("//div[@class='sort-menu-container']/a")
        sort_link = self.driver.find_element_by_xpath("//ul[@id='SortMenu']/li[4]/a")
        action = ActionChains(self.driver).move_to_element(sort_menu).click(sort_menu)
        action.perform()
        sort_link.click()
        price_list = []

        for item in self.get_listings():
            price = item.find_element_by_xpath(".//li[contains(@class, 'lvprice')]/span").text
            price = price.replace("£", "").replace(",", "")
            price_list.append(float(price))

        # print(price_list)
        self.assertEqual(sorted(price_list), price_list)

    def test_highest_price_sort(self):
        self.do_search()
        time.sleep(5)
        sort_menu = self.driver.find_element_by_xpath("//div[@class='sort-menu-container']/a")
        sort_link = self.driver.find_element_by_xpath("//ul[@id='SortMenu']/li[3]/a")
        action = ActionChains(self.driver).move_to_element(sort_menu).click(sort_menu)
        action.perform()
        sort_link.click()
        price_list = []

        for item in self.get_listings():
            price = item.find_element_by_xpath(".//li[contains(@class, 'lvprice')]/span").text
            price = price.replace("£", "").replace(",", "")
            price_list.append(float(price))

        self.assertEqual(sorted(price_list, reverse= True), price_list)

    def test_buy_it_now_filter(self):
        self.do_search()
        self.driver.find_element_by_xpath("//a[contains(text(),'Buy it now')]").click()

        for item in self.get_listings():
            buy_it_now_tag = item.find_element_by_xpath(".//li[@class='lvformat']/span/span[contains(@class, 'logoBin')]")
            self.assertTrue(buy_it_now_tag.is_displayed())


class TestSearchCategory(EbayBaseTestCase):
    pass