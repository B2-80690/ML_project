from selenium import webdriver
from selenium.webdriver.common.by import By
finder = webdriver.Chrome()
import numpy as np
import time


import json

link_list = []
def all_link_scrapper():
    url = "https://www.imdb.com/search/title/?genres=comedy"
    finder.get(url)
    btn = finder.find_element(By.CSS_SELECTOR,
                               ".ipc-btn.ipc-btn--single-padding.ipc-btn--center-align-content.ipc-btn--default-height.ipc-btn--core-base.ipc-btn--theme-base.ipc-btn--on-accent2.ipc-text-button.ipc-see-more__button")
    print(btn)
    btn.click()
    btn.click()

    #time.sleep(15)

    #print(btn.click())

    #
    # finder.get("https://www.imdb.com/search/title/?genres=action&ref_=adv_prv")

    arrange_ = np.arange(101,152,50)
    # print(arrange_)

    # for val in arrange_:
    #     print(val)
    #     url_given = f"https://www.imdb.com/search/title/?genres=Comedy&start={101}&ref_=adv_nxt"
    #     print(url_given)

        # finder.get(url_given)
        # h3_tag = finder.find_elements(By.CLASS_NAME, "lister-item-header")
        # for index in range(2, len(h3_tag)):
        #     a_tag = h3_tag[index].find_element(By.TAG_NAME, 'a')
        #     href_value = a_tag.get_attribute("href")
        #     print(href_value)
        #     link_list.append(href_value)



all_link_scrapper()

# with open("all_action_links_to_new.json","a") as file:
#     file.write(json.dumps(link_list))
