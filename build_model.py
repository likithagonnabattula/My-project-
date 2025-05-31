import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.read_csv('movies.csv')

# Create a 'tags' column by combining overview and genres
movies['tags'] = movies['overview'] + ' ' + movies['genres'].str.replace('|', ' ')

# Select required columns
new_data = movies[['movie_id', 'title', 'tags']]

# Preprocess tags
new_data['tags'] = new_data['tags'].fillna('').str.lower()

# Vectorize tags
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_data['tags']).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(new_data, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ movie_list.pkl and similarity.pkl saved!")
