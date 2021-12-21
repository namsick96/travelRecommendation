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
from random import randrange


def start_search(driver, place_info):
    url = "https://www.google.com/maps/"
    #driverPath = "C:/venvs/travelRecomendation/chromedriver.exe"
    #driver = webdriver.Chrome(driverPath)
    driver.get(url)
    # result = requests.get(url=url) # 응답

    search = driver.find_element_by_css_selector("#searchboxinput")
    driver.implicitly_wait(10)

    search.clear()
    search.send_keys(place_info.get("name"))
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    return get_store_review_data(driver, place_info)


def get_store_review_data(driver, place_info):
    while True:
        try:
            time.sleep(randrange(3,7,1))
            # 더보기 = driver.find_element_by_css_selector('#pane > div > div.widget-pane-content.scrollable-y > div > div > div:nth-child(44) > div > div > button')
            더보기 = driver.find_element_by_css_selector("button[aria-label*='리뷰 더보기']")
            더보기.send_keys(Keys.ENTER)
            dirver.implicitly_wait(15)
            # 더보기 = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[41]/div/div/button')
            # time.sleep(1)
            # 더보기.click()
        except Exception as e:
            print(e)
            break

    for i in range(15):
        # 스크롤 : 마지막까지
        # reviews = driver.find_elements_by_css_selector('span.section-review-text')
        # for review in reviews:
        #     print(review.text)
        # print(
        #     "========================================================================================================")

        try:
            driver.implicitly_wait(10)
            scrollable_div = driver.find_element_by_css_selector('div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc')
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
            time.sleep(randrange(2,5,1))
            
        except Exception as e:
            print(e)
            break

        time.sleep(randrange(2,6,1))

    # 스크롤 끝났으니 수집
    reviews = driver.find_elements_by_xpath('.//span[@class="ODSEW-ShBeI-text"]')
    stars = driver.find_elements_by_xpath('.//span[@class="ODSEW-ShBeI-H1e3jb"]')
    result = [
        [
            place_info.get("subcategory"),
            place_info.get("real_name"),
            re.search(r"[0-9]", star.get_attribute("aria-label")).group(),
            review.text.replace("\n", " "),
        ]
        for star, review in zip(stars, reviews)
    ]
    return result


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
    options.add_argument('--disable-dev-shm-usage') 
    options.add_argument( 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chromedriver_path = "chromedriver"
    driver = webdriver.Chrome(
        os.path.join(os.getcwd(), chromedriver_path), options=options)
    
    # r"C:/venvs/travelRecomendation/cafe.csv"
    df = pd.read_csv('sampled_cafe.csv',
        encoding="utf-8-sig",
        sep="|",
    )
    subcategory = df["분류"]
    place_name = df["이름"]
    place_addr = df["주소"]
    #cafe_tel = df["전화번호"].astype(str)
    place_len = len(place_name)
    search_name = []
    for i in range(place_len):
        name = place_name[i] + " " + str(place_addr[i][:11]) 
        search_name.append({"subcategory" : subcategory[i], "name": name, "real_name": place_name[i]}) 

    for i in range(place_len):

        result = start_search(driver, search_name[i])

        # 구, ID, stars, 리뷰
        # result = get_store_review_data(driver)
        data = pd.DataFrame(result)
        # data.columns = ['stars', 'reviews']
        # data.columns = ['stars', 'reviews']
        # data = pd.concat([search_name[i].get("gu") + search_name[i].get("cafe_id"), data], axis=1)
        # 누적
        if not os.path.exists("cafe_reviews.csv"):
            data.to_csv("cafe_reviews.csv", index=False, sep="|", mode="w")
        else:
            data.to_csv(
                "cafe_reviews.csv", index=False, sep="|", mode="a", header=False
            )


if __name__ == "__main__":
    main()