
import  json

from selenium import webdriver
from selenium.webdriver.common.by import By
finder = webdriver.Chrome()










def data_scraper(url_):


        # print(data[0]['link'])

        # url_for_browser = data[250]['link']

        finder.get(url_)

        all_data = finder.find_element(By.XPATH , "/html")

        all_data_new = (all_data.text).split("\n")

        for val in all_data_new:
            print(val)

        movie_name_index = all_data_new.index("All topics")

        actual_movie_name = all_data_new[movie_name_index + 1]

        movie_year = all_data_new[movie_name_index + 2]

        gonear_start_index = all_data_new.index("99+ PHOTOS")

        goner_ending_index = all_data_new.index("/10")

        list_of_gonears = list()

        for i in range(gonear_start_index + 1 ,goner_ending_index - 2 ):
            list_of_gonears.append(all_data_new[i])

        print(f"your movie name is {actual_movie_name} '\n' your movie released date {movie_year} '\n' your gonear list {list_of_gonears}")















def data_reader():
    with open("all_file_of_data_link.json", 'r') as file:
        data = file.read()

        data = json.loads(data)

        # print(len(data))
        count = 0

        # for index in range(0,len(data),2):
        #
        #     if count == 500:
        #         break
        #
        #     data_scraper(data[index]['link'])
        #     break
        #     count += 2
        data_scraper(data[5]['link'])


data_reader()






