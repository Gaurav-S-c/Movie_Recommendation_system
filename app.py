import pandas as pd
import pickle
import streamlit as st
import requests

movies=pickle.load(open('movie_dict.pkl','rb'))
data=pd.DataFrame(movies)
similarity=pickle.load(open('similarity.pkl','rb'))

#TMDB  and OMDB API key:
API_KEY = "0361c880dff8292ad595e26765c54f45"
OMDB_KEY = "62c1f87c"
# Read API keys from Streamlit secrets
API_KEY = st.secrets["API_KEY"]
OMDB_API = st.secrets["OMDB_KEY"]

def fetch_poster(movie_name):
    # First try TMDB
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        data = response.json()
        
        if data["results"]:
            best_match = max(data["results"], key=lambda x: x.get("popularity", 0))
            poster_path = best_match.get("poster_path")
            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path
    except Exception as e:
        print("TMDB error:", e)

    # Second try OMDb (needs free API key from omdbapi.com)
    try:
        url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_KEY}"
        response = requests.get(url, timeout=8).json()
        if response.get("Poster") and response["Poster"] != "N/A":
            return response["Poster"]
    except:
        pass

    # fallback
    return "https://via.placeholder.com/300x450/222222/FFFFFF?text=No+Poster"



def recommend(movie):
    movie_index = data[data['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:9]

    recommend_movies=[]
    recommend_posters=[]
    for i in movie_list:
        title = data.iloc[i[0]].title
        recommend_movies.append(title)
        recommend_posters.append(fetch_poster(title))
    return recommend_movies, recommend_posters

#streamlit web app
st.title("🍿 Movie Recommendation System 🎬")
st.markdown("Find movies similar to your favorite one!")

selected_movie = st.selectbox("🎥 Select a movie", list(data['title'].values))
btn = st.button("🔍 Recommend")

if btn:
    names, posters = recommend(selected_movie)

    # Display in grid
    cols = st.columns(4)
    for i in range(len(names)):
        with cols[i % 4]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"**{names[i]}**", unsafe_allow_html=True)
