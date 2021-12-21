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


def start_search(driver, place_info):
    url = "https://www.google.com/maps/"
    #driverPath = "C:/venvs/travelRecomendation/chromedriver.exe"
    #driver = webdriver.Chrome(driverPath)
    driver.get(url)
    # result = requests.get(url=url) # 응답

    # search = driver.find_element_by_css_selector("input#searchboxinput.tactile-searchbox-input")
    search = driver.find_element_by_css_selector("#searchboxinput")
    time.sleep(1)

    search.clear()
    search.send_keys(place_info.get("name"))
    search.send_keys(Keys.ENTER)
    # driver.implicitly_wait(3)

    return get_store_review_data(driver, place_info)


def get_store_review_data(driver, place_info):
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
            place_info.get("subcategory"),
            re.search(r"[0-9]", star.get_attribute("aria-label")).group(),
            review.text.replace("\n", " "),
        ]
        for star, review in zip(stars, reviews)
    ]
    return result

    # return (stars.get_attribute("aria-label"), reviews.text)
    # print(stars.get_attribute("aria-label"), reviews.text)


def main():

    #driverPath = "C:/venvs/travelRecomendation/chromedriver.exe"
    #driver = webdriver.Chrome(driverPath)
    options = webdriver.ChromeOptions()
    options.add_argument("lang=ko_KR")
    #options.add_argument('--headless')  # >> 주석처리시 작동창 안나타남
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
    options.add_argument("window-size=1920x1080")
    options.add_argument("no-sandbox")
    options.add_argument("disable-gpu")
    options.add_argument( 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chromedriver_path = "chromedriver"
    driver = webdriver.Chrome(
        os.path.join(os.getcwd(), chromedriver_path), options=options)
    
    # r"C:/venvs/travelRecomendation/tourism.csv"
    df = pd.read_csv('food.csv',
        encoding="utf-8-sig",
        sep="|",
    )
    subcategory = df["분류"]
    place_name = df["이름"]
    place_addr = df["주소"]
    #tourism_tel = df["전화번호"].astype(str)
    place_len = len(place_name)
    search_name = []
    for i in range(place_len):
        name = place_name[i] + " " + place_addr[i] 
        search_name.append({"subcategory" : subcategory[i], "name": name}) 

    for i in range(place_len):

        result = start_search(driver, search_name[i])

        # 구, ID, stars, 리뷰
        # result = get_store_review_data(driver)
        data = pd.DataFrame(result)
        # data.columns = ['stars', 'reviews']
        # data.columns = ['stars', 'reviews']
        # data = pd.concat([search_name[i].get("gu") + search_name[i].get("tourism_id"), data], axis=1)
        # 누적
        if not os.path.exists("food_reviews_GA_GC.csv"):
            data.to_csv("food_reviews.csv", index=False, sep="|", mode="w")
        else:
            data.to_csv(
                "food_reviews.csv", index=False, sep="|", mode="a", header=False
            )


if __name__ == "__main__":
    main()