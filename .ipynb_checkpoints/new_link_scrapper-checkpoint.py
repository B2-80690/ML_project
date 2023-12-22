
from selenium import webdriver
from selenium.webdriver.common.by import By
finder = webdriver.Chrome()


def link_scrapper():

    # url_given = "https://www.imdb.com/search/title/?genres=action"
    # https://www.imdb.com/search/title/?genres=action&start=101&ref_=adv_nxt
    url_given = f"https://www.imdb.com/search/title/?genres=action&start='{51}'&ref_=adv_nxt"


    finder.get(url_given)

    now_find_the_url = finder.find_element(By.XPATH , "/html")

    # NEXT = now_find_the_url.find_element(By.TAG_NAME , "a")

    now_going_main = now_find_the_url.find_element(By.ID , "pagecontent")

    now_going_another_div = now_going_main.find_element(By.ID , "main")

    # now_i_am_going_for_child = now_going_another_div.



    print(now_going_another_div.text)




    # get_url = now_find_the_url.find_element(By.TAG_NAME , "a")
    #
    # actual_url = get_url.get_attribute("href")

    # print(actual_url)





link_scrapper()

# "https://www.imdb.com/search/title/?genres=action&start='{51}'&ref_=adv_nxt"
#
#
# "/search/title/?genres=action&start=100&ref_=adv_next"


# print(    f"https://www.imdb.com/search/title/?genres=action&start='{51}'&ref_=adv_nxt"
# )


