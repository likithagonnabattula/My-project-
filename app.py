import streamlit as st
import pandas as pd
import pickle

# Load pre-processed data
new_data = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommend function
def recommend(movie):
    try:
        movie_index = new_data[new_data['title'] == movie].index[0]
    except IndexError:
        return ["Movie not found."]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [new_data.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies

# ---------- UI Start ---------- #

# Set page config
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# Optional background styling (CSS)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Title
st.markdown('<div class="title">🎥 Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown("#### 📽️ Discover 5 movies similar to your favorite")

# Movie selection
selected_movie = st.selectbox("🎞️ Select or type a movie title:", new_data['title'].values)

# Recommend button
if st.button("🍿 Recommend"):
    recommendations = recommend(selected_movie)

    if recommendations[0] == "Movie not found.":
        st.error("❌ Movie not found. Try another title.")
    else:
        st.subheader("📺 You might enjoy these movies:")
        for movie in recommendations:
            st.markdown(f'<div class="movie-box">✅ {movie}</div>', unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")

