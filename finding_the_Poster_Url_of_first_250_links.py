import json
from selenium import webdriver
from selenium.webdriver.common.by import By
finder = webdriver.Chrome()


def all_poster_Url_finder(url):

    finder.get(url)
    # all_data = finder.find_element(By.XPATH, "/html")

    div_of_poster = finder.find_element(By.XPATH,"/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/div[1]")
    # all_data_new = (all_data.text).split("\n")
    imag_tag = div_of_poster.find_element(By.TAG_NAME , "img").get_attribute("src")
    print(imag_tag)











def all_link_feeder():

    with open("unique_list_of_url.json" ,"r") as file:
        data = file.read()

        data = json.loads(data)

        for link_ in data:
            # data_scraper(link_)

            all_poster_Url_finder(link_)

all_link_feeder()