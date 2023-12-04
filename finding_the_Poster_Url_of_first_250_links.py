import json
from selenium import webdriver
from selenium.webdriver.common.by import By
finder = webdriver.Chrome()

list_of_all_movies = list()
def all_poster_Url_finder(url):

    finder.get(url)

    #here i am finding the image tag of the top 250 movies
    try:
        div_of_poster = finder.find_element(By.XPATH,"/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/div[1]")
        # all_data_new = (all_data.text).split("\n")
        imag_tag = div_of_poster.find_element(By.TAG_NAME , "img").get_attribute("src")
        # print(imag_tag)

    except ValueError as e:
        imag_tag = None
        # print(imag_tag)
    try:
        box_location = finder.find_element(By.XPATH , "/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div[2]")
        actual_name_ho = box_location.find_elements(By.TAG_NAME , "a")
        names = list()

        for name in actual_name_ho:
            names.append(name.text)
        count = 0
        actual_names = list()
        for index in range(len(names)):
            if names[index] == "":
                actual_names.append(names[index + 1])
                count += 1
            if count == 3:
                break


    except ValueError as e:
        actual_names = None
        # print(actual_names)



    try:
        all_data = finder.find_element(By.XPATH, "/html")
        all_data_new = (all_data.text).split("\n")
        try:
            # all that is okk
            # here i am finding the director name
            index_of_director = all_data_new.index("Director")
            actual_director_name = all_data_new[index_of_director + 1]
            # name of director ends
        except ValueError as e:
            actual_director_name = None

        # here i am finding the gonear list
        try:
            gonear_start_index = all_data_new.index("99+ PHOTOS")
            goner_ending_index = all_data_new.index("/10")

            list_of_gonears = list()
            for i in range(gonear_start_index + 1, goner_ending_index - 2):
                list_of_gonears.append(all_data_new[i])
            # finding the gonear ends here
        except ValueError as e:

            list_of_gonears = list()



        try:
            # here i am finding the movie name
            movie_name_index = all_data_new.index("All topics")
            actual_movie_name = all_data_new[movie_name_index + 1]
            # finding the actual movie name ends here
        except ValueError as e:
            actual_movie_name = None

        try:
            # here i am finding the reviews in millions
            goner_ending_index = all_data_new.index("/10")
            all_views_of_people = all_data_new[goner_ending_index + 1]
            # finding the views in millions ends
        except ValueError as e:
            all_views_of_people = 0

        try:
            # here i am finding the movie year
            movie_name_index = all_data_new.index("All topics")
            movie_year = all_data_new[movie_name_index + 2]
            # finding the actual movie year ends here
        except ValueError as e:
            movie_year = 0

        try:
            # here i am finding the actual description
            goner_ending_index = all_data_new.index("/10")
            actual_description = all_data_new[goner_ending_index - 2]
            # here finding the actual description ends
        except ValueError as e:

            actual_description = None

        try:
            # here i am finding the actual run time
            run_time_index = all_data_new.index("Runtime")
            actual_runtime = all_data_new[run_time_index + 1]
            # finding the actual runtime ends here
        except ValueError as e:

            actual_runtime = 0

        try:
            # here i am finding the actual language
            language_index = all_data_new.index("Also known as")
            acutal_language = all_data_new[language_index - 1]
            # finding the actual language ends here
        except ValueError as e:

            acutal_language = None

        try:
            # here i am finding the actual country name
            country_finder = all_data_new.index("Release date")
            language_index = all_data_new.index("Also known as")
            actual_country = all_data_new[language_index + 3]
            # here origian of country name is ending
        except ValueError as e:

            actual_country = None

        try:
            # here i am finding the budget for the movie
            budget_index = all_data_new.index("Budget")
            acutal_budget = all_data_new[budget_index + 1]
            # finding the actual budget ends here
        except ValueError as e:

            acutal_budget = 0

        try:
            # here i am finding actual gross collection of movie
            collection_index = all_data_new.index("Gross worldwide")
            actual_collection = all_data_new[collection_index + 1]
            # here finding the actual gross collection ends here

        except ValueError as e:

            actual_collection = 0

        try:
            # here i am finding how many reviews given by the user in k
            index_of_user_reviews = all_data_new.index("Review")
            actual_user_review_string = all_data_new[index_of_user_reviews - 1].replace("K", " ")
            actual_revewis = float(actual_user_review_string.strip()) * 1000
            # here finding the actual reviews ends
        except ValueError as e:

            actual_revewis = 0

        try:
            # here i am finding the rating of ten
            goner_ending_index = all_data_new.index("/10")
            rating_out_of_ten = all_data_new[goner_ending_index - 1]
            # here finding the rating of ten ends
        except ValueError as e:
            rating_out_of_ten = 0

        try:
            # here i am finding the url
            url_of_poster = finder.find_element(By.XPATH,
                                                "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/a")
            # print(url_of_poster)
            href_ = url_of_poster.get_attribute("href")
            # print(href_)

        except ValueError as e:

            href_ = None
    except:
        actual_director_name = None

        list_of_gonears = []

        actual_movie_name = None

        movie_year = None

        actual_revewis = 0
        # #
        # actual_url = "NULL"

        all_views_of_people = 0

        actual_description = None

        actual_runtime = None

        actual_country = None

        acutal_language = None

        acutal_budget = 0

        actual_collection = 0

        rating_out_of_ten = 0

        href_ = None

        imag_tag = None

        actual_names = None

    print(
        f"{'*' * 80}"
        f"print actual director name = {actual_director_name}'\n' "
        f"movie name is = {actual_movie_name} '\n' "
        f"list of gonears is = {list_of_gonears} '\n'"
        f"actual_description is = {actual_description} '\n'"
        f"actual_runtime is = {actual_runtime} '\n'"
        f"acutal_language is = {acutal_language} '\n'"
        f"print actual_country = {actual_country} '\n'"
        f"acutal_budget is = {acutal_budget}  '\n'"
        f"actual_collection is = {actual_collection} '\n'"
        f"actual_revewis is = {actual_revewis}  '\n'"
        f"movie year = {movie_year} '\n'"
        f"print all_views_of_people = {all_views_of_people}'\n' "
        f"print rating_out_of_ten = {rating_out_of_ten} '\n'"
        # f"printing the link_of_poster = {href_} \n"
        f"printing the link_of_poster = {imag_tag} \n"
        f"printing cast names = {actual_names} \n"        
        f"{'*' * 80}"

    )

    dictionary = {

        "Name_of_movie": actual_movie_name,
        "Name_of_director": actual_director_name,
        "List_of_genre": list_of_gonears,
        "Discription_of_movie": actual_description,
        "Run_time_in_min": actual_runtime,
        "Language_of_move": acutal_language,
        "Country_of_origin": actual_country,
        "Budget_of_movie": acutal_budget,
        "Global_collection": actual_collection,
        "Release_year": movie_year,
        "Rating_out_of_ten": rating_out_of_ten,
        "World_Wild_Views": all_views_of_people,
        "Reviews_to_movie": actual_revewis,
        # "Poster_url":href_,
        "Names_of_Cast": actual_names,
        "Poster_url_":imag_tag

    }

    list_of_all_movies.append(dictionary)

    # print(f"-" * 80)










def all_link_feeder():

    with open("unique_list_of_url.json" ,"r") as file:
        data = file.read()

        data = json.loads(data)

        for link_ in data:
            # data_scraper(link_)

            all_poster_Url_finder(link_)


all_link_feeder()

def write_in_the_json_():
    with open("all_new_data_sam+Devika_collected.json","a") as file:
        file.write(json.dumps(list_of_all_movies))



write_in_the_json_()