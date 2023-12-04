
from selenium import  webdriver

from selenium.webdriver.common.by import By

import json

finder = webdriver.Chrome()


def url_finder():
    url_given = f"https://www.imdb.com/search/title/?genres=comady&start='{51}'&ref_=adv_nxt"



    finder.get("https://m.imdb.com/chart/top/")

    block = finder.find_element(By.XPATH , "/html/body/div[2]/main/div/div[3]/section/div/div[2]")

    ul = block.find_element(By.TAG_NAME , "ul")

    li  = ul.find_elements(By.TAG_NAME , "li")

    list_of_all_anchor = list()

    list_of_all_url = list()



    for a in li:


        # print(a.find_element(By.TAG_NAME , "a"))

        list_of_all_anchor.append(a.find_element(By.TAG_NAME , "a"))


    for an in list_of_all_anchor:
        # print(an.get_attribute("href"))
        list_of_all_url.append(an.get_attribute("href"))



    with open("unique_list_of_url.json" , "w") as FILE:
        FILE.write(json.dumps(list_of_all_url))









url_finder()