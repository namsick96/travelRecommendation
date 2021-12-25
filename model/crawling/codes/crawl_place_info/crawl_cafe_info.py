import os
from time import sleep
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

gu_list = ["서귀포시", "제주시"]


# csv 파일에 헤더 만들어 주기
for index, gu_name in enumerate(gu_list):
    fileName = 'cafe' + '.'+'csv'

    if index==0:
        file = open(fileName, "w", encoding="utf-8-sig")
    else:
        file = open(fileName, "a", encoding="utf-8-sig")
    file.write("분류" + "|" + "이름" + "|" + "주소" + "|" + "전화번호" + "|" + "대표사진주소" + "\n")
    file.close()  # 처음에 csv파일에 칼럼명 만들어주기

    options = webdriver.ChromeOptions()
    options.add_argument("lang=ko_KR")
    chromedriver_path = "chromedriver"
    driver = webdriver.Chrome(
        os.path.join(os.getcwd(), chromedriver_path), options=options
    )  # chromedriver 열기
    driver.get("https://map.kakao.com/")  # 주소 가져오기
    search_area = driver.find_element_by_xpath(
        '//*[@id="search.keyword.query"]'
    )  # 검색 창
    search_area.send_keys(gu_name + " 카페")  # 검색어 입력
    driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(
        Keys.ENTER
    )  # Enter로 검색
    driver.implicitly_wait(3)  # 기다려 주자
    more_page = driver.find_element_by_id("info.search.place.more")
    # more_page.click()
    more_page.send_keys(Keys.ENTER)  # 더보기 누르고
    # 첫 번째 검색 페이지 끝
    # driver.implicitly_wait(5) # 기다려 주자
    time.sleep(1)

    # next 사용 가능?
    next_btn = driver.find_element_by_id("info.search.page.next")
    has_next = "disabled" not in next_btn.get_attribute("class").split(" ")
    Page = 1
    while has_next:  # 다음 페이지가 있으면 loop
        # for i in range(2, 6): # 2, 3, 4, 5
        file = open(fileName, "a", encoding="utf-8")
        time.sleep(1)
        # place_lists = driver.find_elements_by_css_selector('#info\.search\.place\.list > li:nth-child(1)')
        # 페이지 루프
        # info\.search\.page\.no1 ~ .no5
        page_links = driver.find_elements_by_css_selector("#info\.search\.page a")
        pages = [
            link
            for link in page_links
            if "HIDDEN" not in link.get_attribute("class").split(" ")
        ]
        # print(len(pages), "개의 페이지 있음")
        # pages를 하나씩 클릭하면서
        for i in range(1, 6):
            xPath = '//*[@id="info.search.page.no' + str(i) + '"]'
            try:
                page = driver.find_element_by_xpath(xPath)
                page.send_keys(Keys.ENTER)
            except ElementNotInteractableException:
                print("End of Page")
                break
            sleep(3)
            place_lists = driver.find_elements_by_css_selector(
                "#info\.search\.place\.list > li"
            )
            for p in place_lists:  # WebElement
                # print(p.get_attribute('innerHTML'))
                # print("type of p:", type(p))
                store_html = p.get_attribute("innerHTML")
                store_info = BeautifulSoup(store_html, "html.parser")
                # BS -> 분석
                #
                place_name = store_info.select(".head_item > .tit_name > .link_name")
                # place_address = store_info.select('.info_item > .addr > p')
                # place_hour = store_info.select('.info_item > .openhour > p > a')
                # place_tel = store_info.select('.info_item > .contact > span')
                # print("length:", len(place_name))
                if len(place_name) == 0:
                    continue  # 광고 
                place_subcategory = store_info.select(".head_item > span")[0].text
                place_name = store_info.select(".head_item > .tit_name > .link_name")[0].text
                place_address = store_info.select(".info_item > .addr > p")[0].text
                #place_hour = store_info.select(".info_item > .openhour > p > a")[0].text
                place_tel = store_info.select(".info_item > .contact > span")[0].text

                # 사진url 수집
                detail = p.find_element_by_css_selector(
                    "div.info_item > div.contact > a.moreview"
                )
                detail.send_keys(Keys.ENTER)

                driver.switch_to.window(driver.window_handles[-1])

                place_photo = ""
                try:
                    photo = driver.find_element_by_css_selector("span.bg_present")
                    photo_url = photo.get_attribute("style")
                    m = re.search('"(.+?)"', photo_url)
                    if m:
                        place_photo = m.group(1)
                    else:
                        place_photo = ""
                except:
                    place_photo = ""
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print(place_name, place_photo)

                file.write(
                    place_subcategory
                    + "|"
                    + place_name
                    + "|"
                    + place_address
                    + "|"
                    #+ place_hour
                    #+ "|"
                    + place_tel
                    + "|"
                    + place_photo
                    + "\n"
                )
            print(i, " of", " [ ", Page, " ] ")
        next_btn = driver.find_element_by_id("info.search.page.next")
        has_next = "disabled" not in next_btn.get_attribute("class").split(" ")
        if not has_next:
            print("Arrow is Disabled")
            driver.close()
            file.close()
            break  # 다음 페이지 없으니까 종료
        else:  # 다음 페이지 있으면
            Page += 1
            next_btn.send_keys(Keys.ENTER)
    print("End of Crawl")
