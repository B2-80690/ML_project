from flask import Flask , request , render_template
# from itertools import zip
import pickle
import pandas as pd


app = Flask(__name__)


# Load movie data and similarity matrix
with open('movie_dict.pkl', 'rb') as file:
    data = file.read()

with open('similarity.pkl', 'rb') as similiraty:
    similarity = similiraty.read()
    # Deserialize the bytes object as a NumPy array
    similarity = pickle.loads(similarity)

    # print(similarity)

# Deserialize the bytes-like object using pickle.loads()
movies_dictionary = pickle.loads(data)


## now find the movies form similarity
movies_list = pd.DataFrame(movies_dictionary)

print(movies_list["Name_of_movie"])
def recommend(movie):
    allMovies = list()

    try:
        movies_list['Name_of_movie'] = [ x.lower()  for x in movies_list['Name_of_movie']]

        index = movies_list[movies_list['Name_of_movie'] == movie].index[0]
        # print(similarity[index])
        # print(movie)
        # print(print(similarity[0].shape))

        distances = list(enumerate(similarity[index]))

        distances = sorted(distances, key=lambda x: x[1], reverse=True)
        # distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        # print(distances)

        # print(f"Top 10 Recommendations for {movie}:")
        for i in distances[1:11]:
            recommended_movie_title = movies_list.iloc[i[0]]['Name_of_movie']
            allMovies.append(recommended_movie_title)
            print(recommended_movie_title)
    except IndexError:
        print(f"Movie '{movie}' not found in the DataFrame.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        return allMovies
        # print(allMovies)

# recommend("FUBAR")

# whenever you have and root rout it will by deafualt render the home page
@app.route("/")
def hellow_world():
    return render_template("home.html")

@app.route("/samir")
def samir():
    return render_template("search.html")


# when you enter the response it will send your search to the new rout called /starch
@app.route('/search', methods=['POST'])
def search():

    # in this function i have to get the the requird values and render them on the page
    search_term = request.form['searchInput']
    # Do something with the search term, for example:
    # print("You searched for:", search_term)
    # Return a response
    # recommend(search_term)
    # here i was finding the all searched movies
    # top_10_movies = " ";
    # print(type(recommend(search_term)))
    # list_for = " "
    # for i in range(len(recommend(search_term))):
    #     print(recommend(search_term)[i])
    #     list_for.join(recommend(search_term)[i])
    #
    # print(list_for)
    # it is ended here

    recommendations = recommend(search_term)

    data = pd.read_csv("movieData2.csv")
    thisIsFinalDF = pd.DataFrame(data)
    print("-"*80)
    # list_of_recommended_movies = recommend("FUBAR")
    print("here i am not  calling the hardcoded function")
    # print(list_of_recommended_movies)
    print("-" * 80)
    movie = thisIsFinalDF["Name_of_movie"]
    poster_url = thisIsFinalDF["Poster_url_"]
    list_of_names = list()
    list_of_urls = list()
    for movie_name in recommendations:
        for i in range(len(movie)):
            lowered_movies = movie[i].lower()
            if movie_name == lowered_movies:
                print(movie[i])
                print(poster_url[i])
                list_of_urls.append(poster_url[i])
                list_of_names.append(movie[i])
                # return poster_url[i]



    # return "Search term received: ".join(recommend(search_term))
    return render_template("poster.html",poster_urls=list_of_urls , poster_names=list_of_names)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         print("hellow i am in the post")
#     else:
#         print("hellow i am in get")

