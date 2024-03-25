import math
from io import BytesIO

import cairosvg
import requests
import streamlit as st
from PIL import Image
from streamlit_card import card

from model.movie import Movie
from model.movieList import MovieList
from utils import sendSPARQLQuery


def showMovie(movie):
    title = movie.get_title()
    director = movie.get_director()
    logo = movie.get_logo()

    with st.container(height=200):
        st.markdown(f"**{title}**", unsafe_allow_html=True)
        st.write(f"Directed by {director}")
        if logo:
            st.image(logo)


def parseMovieData(movie_data):
    movie_list = MovieList()

    for binding in movie_data["results"]["bindings"]:

        title = binding["filmLabel"]["value"]
        director = binding["directorLabel"]["value"]
        logo = binding.get("logo")
        if logo:
            logo = logo["value"]

        movie = Movie(title, director, logo)
        movie_list.add_movie(movie)

    return movie_list


st.title("CineQ")

language = st.selectbox("Language", ("English", "German"))

movies = MovieList()

# Input form for the SPARQL query
with st.form("query_form"):
    query = st.text_area(
        "SPARQL Query", placeholder="Enter your SPARQL query here", height=200
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        movie_data = sendSPARQLQuery(query)
        movies = parseMovieData(movie_data)

n_movies = len(movies)


for row in range(math.ceil(n_movies / 3)):
    col1, col2, col3 = st.columns(3)
    with col1:
        showMovie(movies[row * 3])
    with col2:
        if row < math.ceil(n_movies / 3) or n_movies % 3 != 1:
            showMovie(movies[row * 3 + 1])
        else:
            st.empty()
    with col3:
        if (row < math.floor(n_movies / 3)) or (n_movies % 3 == 0):
            showMovie(movies[row * 3 + 2])
        else:
            st.empty()
