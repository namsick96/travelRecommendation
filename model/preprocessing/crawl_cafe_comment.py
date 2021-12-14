import os
import re
from time import sleep
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests


def start_search(driver, cafe_info):
    url = "https://www.google.com/maps/"
    driverPath = "chromedriver"
    # driver = webdriver.Chrome(driverPath)
    driver.get(url)
    # result = requests.get(url=url) # 응답

    # search = driver.find_element_by_css_selector("input#searchboxinput.tactile-searchbox-input")
    search = driver.find_element_by_css_selector("#searchboxinput")
    time.sleep(1)

    search.clear()
    search.send_keys(cafe_info.get("name"))
    search.send_keys(Keys.ENTER)
    # driver.implicitly_wait(3)

    return get_store_review_data(driver, cafe_info)


def get_store_review_data(driver, cafe_info):
    while True:
        try:
            time.sleep(5)
            # 더보기 = driver.find_element_by_css_selector('#pane > div > div.widget-pane-content.scrollable-y > div > div > div:nth-child(44) > div > div > button')
            더보기 = driver.find_element_by_css_selector("button[aria-label*='리뷰 더보기']")
            더보기.send_keys(Keys.ENTER)
            # 더보기 = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[41]/div/div/button')
            # time.sleep(1)
            # 더보기.click()
        except Exception as e:
            print(e)
            break

    # last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(100):
        # 스크롤 : 마지막까지
        # reviews = driver.find_elements_by_css_selector('span.section-review-text')
        # for review in reviews:
        #     print(review.text)
        # print(
        #     "========================================================================================================")

        try:
            scroll = driver.find_element_by_css_selector(
                "div.section-layout.section-scrollbox.scrollable-y.scrollable-show"
            )
            time.sleep(1)
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll
            )
            location1 = scroll.location_once_scrolled_into_view
            print(i, location1)
        except Exception as e:
            print(e)
            break

        time.sleep(1)

    # 스크롤 끝났으니 수집
    reviews = driver.find_elements_by_css_selector("span.section-review-text")
    stars = driver.find_elements_by_css_selector("span.section-review-stars")
    result = [
        [
            cafe_info.get("gu"),
            cafe_info.get("cafe_id"),
            re.search(r"[0-9]", star.get_attribute("aria-label")).group(),
            review.text.replace("\n", " "),
        ]
        for star, review in zip(stars, reviews)
    ]
    return result

    # return (stars.get_attribute("aria-label"), reviews.text)
    # print(stars.get_attribute("aria-label"), reviews.text)


def main():

    driverPath = "chromdriver"
    driver = webdriver.Chrome(driverPath)

    # 카페 1개의 정보 구, ID, 카페명, 주소 ...
    # df = pd.read_csv(r'C:\Users\USER\Desktop\cafe_list\result_gu.csv')
    # df['검색어'] = df['카페명'] + df['주소']
    df = pd.read_csv(
        r"C:\Users\USER\Desktop\cafe_list\CAFE\XIN_result_gu2.csv",
        encoding="utf-8-sig",
        sep="|",
    )
    gu = df["구"]
    cafe_id = df["ID"]
    cafe_name = df["카페명"]
    cafe_addr = df["주소"]
    cafe_tel = df["전화번호"].astype(str)
    cafe_len = len(cafe_name)
    search_name = []
    for i in range(cafe_len):
        name = cafe_name[i] + " " + cafe_addr[i] + " " + cafe_tel[i]
        search_name.append({"name": name, "gu": gu[i], "cafe_id": cafe_id[i]})

    for i in range(cafe_len):

        result = start_search(driver, search_name[i])

        # 구, ID, stars, 리뷰
        # result = get_store_review_data(driver)
        data = pd.DataFrame(result)
        # data.columns = ['stars', 'reviews']
        # data.columns = ['stars', 'reviews']
        # data = pd.concat([search_name[i].get("gu") + search_name[i].get("cafe_id"), data], axis=1)
        # 누적
        if not os.path.exists("cafe_reviews_GA_GC.csv"):
            data.to_csv("cafe_reviews.csv", index=False, sep="|", mode="w")
        else:
            data.to_csv(
                "cafe_reviews.csv", index=False, sep="|", mode="a", header=False
            )


"""
1. 카페 정보 불러오기
2. 한라인씩 읽으면 -> 해당 카페의 식별정보(구, ID)
3. 수집 -> [구, ID, stars, review]
"""


if __name__ == "__main__":
    main()
