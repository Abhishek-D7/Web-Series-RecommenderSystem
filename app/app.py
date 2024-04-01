import streamlit as st
import pickle
import numpy as np
similarity = pickle.load(open("Similarity.pkl", "rb"))
Series = pickle.load(open("Series.pkl", "rb"))
Series = Series['Title'].values
image_path = r"C:\Users\abhid\PycharmProjects\tensorflow envi\TV-series-Recommender\app\MovieRS.jpg"
st.title('Movies And TV-Series Recommender System')
st.image(image_path, caption='Recommender System')


def recommendation(movie):
    movie_index = np.where(Series == movie)[0][0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommend = []
    for i in movies_list:
        recommend.append(Series[i[0]])

    return recommend


Select = st.selectbox(
    'Search TV Series or Movie',
    Series)

if st.button('Recommend'):
    recommendations = recommendation(Select)
    for i in recommendations:
        st.write(i)
