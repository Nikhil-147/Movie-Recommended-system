import streamlit as st
import pandas as pd
import pickle 

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    
    for i in movie_list:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names
    

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('simirality.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Type or select a movie from the dropdown",(movies['title'].values))

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)