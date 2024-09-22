import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import random

data = {
    'User1': [5, 4, 0, 0, 1],
    'User2': [0, 0, 4, 5, 0],
    'User3': [2, 0, 0, 3, 4],
    'User4': [0, 0, 5, 4, 3],
}
movies = ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5']

ratings = pd.DataFrame(data, index=movies).T

movies_data = pd.DataFrame({
    'title': movies,
    'description': [
        'Action movie with a hero',
        'A romantic film',
        'A thriller',
        'An action-packed adventure',
        'A comedy'
    ]
})
def recommend_movies(user):
    user_similarity = cosine_similarity(ratings.fillna(0))
    similarity_df = pd.DataFrame(user_similarity, index=ratings.index, columns=ratings.index)
    
    similar_users = similarity_df[user].sort_values(ascending=False)[1:] 
    recommendations = pd.Series(dtype='float64')
    
    for similar_user in similar_users.index:
        user_ratings = ratings.loc[similar_user]
        recommendations = pd.concat([recommendations, user_ratings[user_ratings > 0]])
    
    if not recommendations.empty:
        recommendations += random.uniform(-0.5, 0.5) 
    
    return recommendations.groupby(recommendations.index).mean().sort_values(ascending=False)

def recommend_content_based(title):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_data['description'])
    
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    idx = movies_data.index[movies_data['title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:3] 
    movie_indices = [i[0] for i in sim_scores]
    return movies_data.iloc[movie_indices]

user_to_recommend = 'User1'
print("Collaborative Filtering Recommendations for", user_to_recommend)
recommended_movies = recommend_movies(user_to_recommend)
print(recommended_movies)
if not recommended_movies.empty:
    print("Recommended Movies with Descriptions:")
    for movie in recommended_movies.index:
        description = movies_data.loc[movies_data['title'] == movie, 'description'].values[0]
        print(f"{movie}: {description}")

movie_to_recommend = 'Movie1'
print("\nContent-Based Filtering Recommendations for", movie_to_recommend)
recommended_content_movies = recommend_content_based(movie_to_recommend)
print("Recommended Movies with Descriptions:")
for index, row in recommended_content_movies.iterrows():
    print(f"{row['title']}: {row['description']}")
