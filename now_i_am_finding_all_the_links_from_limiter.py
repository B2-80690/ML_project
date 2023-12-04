from selenium import webdriver
from selenium.webdriver.common.by import By
finder = webdriver.Chrome()
import numpy as np

import json

link_list = []
def all_link_scrapper():
    #
    # finder.get("https://www.imdb.com/search/title/?genres=action&ref_=adv_prv")

    arrange_ = np.arange(101,1000,50)
    # print(arrange_)

    for val in arrange_:
        print(val)
        url_given = f"https://www.imdb.com/search/title/?genres=action&start={val}&ref_=adv_nxt"
        print(url_given)

        finder.get(url_given)
        h3_tag = finder.find_elements(By.CLASS_NAME, "lister-item-header")
        for index in range(2, len(h3_tag)):
            a_tag = h3_tag[index].find_element(By.TAG_NAME, 'a')
            href_value = a_tag.get_attribute("href")
            print(href_value)
            link_list.append(href_value)

all_link_scrapper()

with open("all_action_links_to_new.json","a") as file:
    file.write(json.dumps(link_list))
