import streamlit as st
import requests
import pickle
import pandas as pd

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=56eaa3c6834bb600014531fa4f454441'.format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"  # Placeholder image

def recommend(movie):
    index = data[data['title'] == movie].index[0]
    L = sorted(list(enumerate(similarity_matrix[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = []
    movie_posters = []
    for i in L:
        movie_id = data['id'][i[0]]
        recommendations.append(data['title'][i[0]])
        movie_posters.append(fetch_poster(movie_id))
    return recommendations, movie_posters

# Load the DataFrame from the pickle file
data = pickle.load(open('movies.pkl', 'rb'))
similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))

# Extract the movie titles as a list
movies_list = data['title'].values

# Set the title of the Streamlit app
st.title('Movie Recommender System')
st.write("### Find recommendations for your favorite movies!")

# Display a selectbox with movie titles
selected_movie = st.selectbox(
    'Select a movie you like:',
    movies_list
)

# Button to see the recommendations
if st.button('Recommend'):
    st.write(f"### Movies similar to {selected_movie}:")

    names, posters = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0], use_column_width=True)
        st.caption(names[0])
    with col2:
        st.image(posters[1], use_column_width=True)
        st.caption(names[1])
    with col3:
        st.image(posters[2], use_column_width=True)
        st.caption(names[2])
    with col4:
        st.image(posters[3], use_column_width=True)
        st.caption(names[3])
    with col5:
        st.image(posters[4], use_column_width=True)
        st.caption(names[4])

    st.write("\n")  # Adding some space after the recommendations
