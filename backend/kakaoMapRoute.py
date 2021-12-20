import os
import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from selenium.webdriver.common.keys import Keys

KAKAO_API_KEY = ""


class KakaoRouteFinder:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

        # self.df = pd.read_excel(file_path)

    def _search_and_select_address(self, target, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()
        element.send_keys(target)
        element.send_keys(Keys.ENTER)
        time.sleep(1)
        # try:
        #     address_selector = (
        #         "#info\.flagsearch\.address\.list > li > span.name"
        #     )
        #     self.driver.find_element_by_css_selector(address_selector).click()
        # except:
        #     address_selector = (
        #         "#info\.flagsearch\.place\.list > "
        #         "li.PlaceFlagItem.clickArea.PlaceFlagItem-ACTIVE > "
        #         "div.infopanel.clickArea > strong"
        #     )
        #     self.driver.find_element_by_css_selector(address_selector).click()

        time.sleep(1)

    def get_distance(self, origin, dest):
        origin = origin.replace("\xa0", " ")
        dest = dest.replace("\xa0", " ")

        base_url = "https://map.kakao.com/?map_type=TYPE_MAP&target=car"
        self.driver.get(base_url)
        time.sleep(1)

        # Preventing clicking not working
        try:
            dimmed_layer_selector = "#dimmedLayer"
            self.driver.find_element_by_css_selector(
                dimmed_layer_selector
            ).click()
        except ElementNotInteractableException:
            pass

        # Inputs origin and destination
        origin_xpath = '//*[@id="info.route.waypointSuggest.input0"]'

        dest_xpath = '//*[@id="info.route.waypointSuggest.input1"]'
        self._search_and_select_address(origin, origin_xpath)
        print("good")
        self._search_and_select_address(dest, dest_xpath)
        print("good2")
        # Route by car
        car_selector = "#cartab"
        self.driver.find_element_by_css_selector(car_selector).click()
        time.sleep(1)

        # Select shortest route
        option_list_selector = (
            "#info\.flagsearch > div.CarRouteResultView > "
            "div.info_pathfind > div > div.opt_pathfind"
        )
        self.driver.find_element_by_css_selector(option_list_selector).click()
        option_selector = (
            "#info\.flagsearch > div.CarRouteResultView > div.info_pathfind > "
            "div > div.opt_pathfind > ul > li:nth-child(3) > a"
        )
        self.driver.find_element_by_css_selector(option_selector).click()

        # Get distance
        selector = (
            "#info\.flagsearch > div.CarRouteResultView > ul > li > "
            "div.summary > div > div.contents > p > span.distance > span.num"
        )
        try:
            element = self.driver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            print(f"Invalid address: {origin} -> {dest}")
            return None
        return element.text

    def find_routes(self):

        try:
            distance = self.get_distance("제주동백수목원","제주시청")
        except Exception as exc:
            distance = None

        return distance

    def __del__(self):
        self.driver.close()

if __name__ == '__main__':
    # 주소 리스트 컬럼은 start, arrive, distance 3개로 구성됨
    driver_path = os.path.join(os.getcwd(), "chromedriver")

    kakao_route_fidner = KakaoRouteFinder(driver_path)
    print(kakao_route_fidner.find_routes())


