import pandas as pd
import streamlit as st
import pickle

# def fetch_poster(movie_id):
#     response = requests.get()
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


movies_dict =pickle.load(open('movie_dict.pkl' , 'rb'))#read binary mode
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender System' )
selected_movie_name = st.selectbox(
    'How would you .......',
    movies['title'].values
)
similarity= pickle.load(open('similarity.pkl', 'rb'))
def recommend (movie):
    movie_index =  movies[movies['title'] == movie].index[0]
    top_movie_list = sorted(list(enumerate(similarity[movie_index])) , reverse= True , key = lambda x:x[1])[1:6]
    for i in top_movie_list:
        st.write(movies.iloc[i[0]].title)

    return
if st.button('Recommend'):
    recommend(selected_movie_name)
