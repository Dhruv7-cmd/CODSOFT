import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie data
movies = pd.DataFrame({
    'title': [
        'The Matrix', 'John Wick', 'Inception', 'Interstellar',
        'The Dark Knight', 'Avengers: Endgame', 'Iron Man', 'The Martian'
    ],
    'description': [
        'A computer hacker learns about the true nature of reality and his role in the war against its controllers.',
        'An ex-hitman comes out of retirement to track down the gangsters that took everything from him.',
        'A thief who steals corporate secrets through dream-sharing technology is given an inverse task.',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity’s survival.',
        'Batman raises the stakes in his war on crime with help from Lieutenant Gordon and Harvey Dent.',
        'Superheroes unite to reverse Thanos’ actions and restore balance to the universe.',
        'A billionaire builds a high-tech suit of armor to fight evil and protect the world.',
        'An astronaut becomes stranded on Mars and must rely on ingenuity to survive.'
    ]
})

# Convert descriptions to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['description'])

# Compute cosine similarity between all movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations
def recommend_movie(title, top_n=3):
    if title not in movies['title'].values:
        return f"Movie '{title}' not found in database."
    
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
    recommended_titles = [movies.iloc[i[0]]['title'] for i in sim_scores]
    return recommended_titles

# Example usage
movie_to_search = "Inception"
print(f"Recommended movies similar to '{movie_to_search}':")
print(recommend_movie(movie_to_search))