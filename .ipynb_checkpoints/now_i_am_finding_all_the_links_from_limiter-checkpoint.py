from selenium import webdriver
from selenium.webdriver.common.by import By
finder = webdriver.Chrome()
import numpy as np

import json

link_list = []
def all_link_scrapper():
    #
    # finder.get("https://www.imdb.com/search/title/?genres=action&ref_=adv_prv")

    arrange_ = np.arange(101,152,50)
    # print(arrange_)

    for val in arrange_:
        # print(val)
        url_given = f"https://www.imdb.com/search/title/?genres=comedy&start={val}&ref_=adv_nxt"
        # print(url_given)

        finder.get(url_given)
        entire_box = finder.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul")
        all_box_in_which_it_require = entire_box.find_element(By.CLASS_NAME ,"ipc-lockup-overlay ipc-focusable").get_attribute("href")
       # for item in all_box_in_which_it_require:
          #  print(item.text)
        # h3_tag = finder.find_elements(By.CLASS_NAME, "lister-item-header")
        # print(h3_tag)
        # for index in range(2, len(h3_tag)):
        #     a_tag = h3_tag[index].find_element(By.TAG_NAME, 'a')
        #     href_value = a_tag.get_attribute("href")
        #     print(href_value)
        #     link_list.append(href_value)
        print(all_box_in_which_it_require)
all_link_scrapper()




with open("single_link_comedy.json","w") as file:
       file.write(json.dumps(link_list))
