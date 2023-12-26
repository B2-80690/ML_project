import  streamlit as st
import pickle
import pandas as pd
import numpy as np



# Open the file and read its contents as bytes
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

        index = movies_list[movies_list['Name_of_movie'] == movie].index[0]
        # print(similarity[index])
        # print(print(similarity[0].shape))

        distances = list(enumerate(similarity[index]))

        distances = sorted(distances, key=lambda x: x[1], reverse=True)
        # distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        # print(distances)

        print(f"Top 10 Recommendations for {movie}:")
        for i in distances[1:11]:
            recommended_movie_title = movies_list.iloc[i[0]]['Name_of_movie']
            allMovies.append(recommended_movie_title)
            # print(recommended_movie_title)
    except IndexError:
        print(f"Movie '{movie}' not found in the DataFrame.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        return allMovies




st.title("Movie Recomender System")

selected_movie_name = st.selectbox(
    "How would you like to be contacted ?",
movies_list['Name_of_movie'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    data = pd.read_csv("movieData2.csv")
    thisIsFinalDF = pd.DataFrame(data)
    list_of_recommended_movies = recommend("FUBAR")
    print(list_of_recommended_movies)
    movie = thisIsFinalDF["Name_of_movie"]
    poster_url = thisIsFinalDF["Poster_url_"]
    for movie_name in list_of_recommended_movies:
        for i in range(len(movie)):
            if movie_name == movie[i]:
                print(movie[i])
                print(poster_url[i])

    for movie in recommendations:
        st.write(movie)



##### now i am finding the posters




