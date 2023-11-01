from selenium import  webdriver

from selenium.webdriver.common.by import By

import  json

browser = webdriver.Chrome()


url_storage = list()
def functioN_of():


    url = 'https://www.imdb.com/chart/top/'
    browser.get(url)
    ul_list_path = browser.find_element(By.XPATH , "/html/body/div[2]/main/div/div[3]/section/div/div[2]/div")
    now_i_will_get = ul_list_path.find_elements(By.TAG_NAME , "a")

    # print(len(now_i_will_get))

    for val in now_i_will_get:
        now_get_href = val.get_attribute("href")
        dictionary = {'link':now_get_href}


        url_storage.append(dictionary)

functioN_of()

with open("all_file_of_data_link.json", 'w') as file:

    file.write(json.dumps(url_storage))





# print(url_storage[0]['link'])



# def my_fun(url_link):

    # print(link)

    # browser.get(url_link)

    # FIND_FIRST_SECTION = browser.find_element(By.XPATH , "/html/body/div[2]/main/div/section[1]/section/div[3]/section")
    #
    # val = FIND_FIRST_SECTION.get_attribute("sc-e226b0e3-3 jJsEuz").
    #
    # print(val)








#     finding_poster_url_link = browser.find_element(By.XPATH,
#                                                    "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/a")
#     actual_link = finding_poster_url_link.get_attribute("href")
#     print(actual_link)
#     find_all_by_section = browser.find_elements(By.TAG_NAME, "Section")
#
#     first_section = (find_all_by_section[1].text).split("\n")
#
#     movie_name = first_section[2]
#     released_year = first_section[3]
#
#     movie_length = first_section[5]
#
#     movie_description_finder_last_index = first_section.index("/10")
#
#     actual_movie_description = first_section[movie_description_finder_last_index - 2]
#
#     movie_rating = first_section[movie_description_finder_last_index - 1]
#
#     views_in = first_section[movie_description_finder_last_index + 1]
#
#     critic_reviews_finder = first_section.index("Critic reviews")
#     actual_critic_reviews = first_section[critic_reviews_finder + 1]
#
#     movie_genore_finder = first_section.index("99+ PHOTOS")
#     last_index = first_section.index("Rate")
#     actual_last = last_index - 4
#     # here i have founded list of gonears
#     list_of_genors = list()
#
#     for val in range(movie_genore_finder + 1, actual_last):
#         list_of_genors.append(first_section[val])
#
#     # print(list_of_genors)
#
#     seventh_section = (find_all_by_section[11].text).split("\n")
#     list_of_similar = list()
#
#     # print(seventh_section)
#     more_like_this_index = seventh_section.count("Watch options")
#     # print(f"i am printing the watch option{more_like_this_index}")
#
#     str = 0
#     last_ind = 0
#     for watch in range(more_like_this_index):
#         if last_ind + 2 < len(seventh_section):
#             last_ind = seventh_section.index("Watch options", str)
#             list_of_similar.append(seventh_section[last_ind + 2])
#             print(seventh_section[last_ind + 2])
#             str = last_ind + 1
#             last_ind = last_ind + 2
#
#         # print(last_ind)
#
#     sixth_section = (find_all_by_section[6].text).split("\n")
#     cast = list()
#     true_cast = list()
#
#     starting_index = sixth_section.index("Top cast")
#     ending_index = sixth_section.index("Director")
#
#     for val in range(starting_index + 2, ending_index):
#         cast.append(sixth_section[val])
#
#     for index in range(len(cast)):
#         if index % 2 == 0:
#             true_cast.append(cast[index])
#
#     fifth_section = (find_all_by_section[0].text).split("\n")
#
#     director_index = fifth_section.index("Director")
#
#     Director_name = fifth_section[director_index + 1]
#
#     fourth_section = (find_all_by_section[17].text).split("\n")
#     print(fourth_section)
#
#     gross_world_index = fourth_section.index("Gross worldwide")
#     world_wide_collection = fourth_section[gross_world_index + 1]
#
#     budget_index = fourth_section.index("Budget")
#
#     Budget_required = fourth_section[budget_index + 1]
#
#     third_section = (find_all_by_section[16].text).split("\n")
#
#     Country_of_origin_index = third_section.index("Country of origin")
#     Country_of_origin = third_section[Country_of_origin_index + 1]
#
#     language_index = third_section.index("Languages")
#     movie_language = third_section[language_index + 1]
#
#     second_section = (find_all_by_section[7].text).split("\n")
#
#     Award_win = second_section[1]
#
#     dict_ = {
#         "movie name": movie_name,
#         "released year": released_year,
#         "movie length": movie_length,
#         "actual movie description": actual_movie_description,
#         "movie rating": movie_rating,
#         "views": views_in,
#         "actual critic reviews": actual_critic_reviews,
#         "genre": list_of_genors,
#         "index": more_like_this_index,
#         "cast": cast,
#         "true cast": true_cast,
#         "Director name": Director_name,
#         "world wide collection": 0,
#         "budget required": Budget_required,
#         "country of origin": Country_of_origin,
#         "language": movie_language,
#         "Award": Award_win
#     }
#
#     print(dict_)
#
#     # all_info_list.append(dict_)
#     #
#     # print(all_info_list)
#
#
#     # with open("all_clear_data.json", 'w') as file:
#     #     file.write(json.dumps(all_info_list))
#
# # print(url_storage)
#
#
#
# my_fun(url_storage[0]['link'])
# # count = 0
# # for val in url_storage:
# #     count += 1
# #     print(val)
#     print(count)


# with open("new_url.json", 'w') as file:
#     file.write(json.dumps(url_storage))





