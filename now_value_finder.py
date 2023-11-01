from selenium import  webdriver

from selenium.webdriver.common.by import By

import  json

browser = webdriver.Chrome()

def scrapping_fun(url_link):
    print(url_link[0])

    browser.get()

    title = browser.find_element(By.XPATH,
                                 "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span")
    print(title.text)









def fun_to_read():

    with open("new_url.json", 'r') as file:
        data = file.read()

        new_data = data.split(",")

        print(new_data)

        print(new_data[0])








fun_to_read()