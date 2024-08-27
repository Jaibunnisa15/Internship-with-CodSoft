import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

# Sample dataset
data = {
    'user_name': ['John','John','John','Alice','Alice','Alice','Bob','Bob','Bob','David','David','David'],
    'book_name': ['Harry Potter', 'A Littel Life', 'Believe In yourself', 'Harry Potter', 'Atomic Habits', 'Psychology of life', 'A Littel Life',
                  'Atomic  Habits','The gift of Forgiveness','Psychology of  life' , 'Believe In yourself', 'The gift of Forgiveness'],
    'rating': [5, 3, 4, 4, 5, 1, 4, 3, 5, 3, 4, 2]
}
# Convert to DataFrame
df = pd.DataFrame(data)

# Create a user-book matrix
user_book_matrix = df.pivot_table(index='user_name', columns='book_name', values='rating')

# Fill NaN with 0
user_book_matrix.fillna(0, inplace=True)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_book_matrix)

# Create a DataFrame for similarity
user_similarity_df = pd.DataFrame(user_similarity, index=user_book_matrix.index, columns=user_book_matrix.index)

def recommend_books(user_id, num_recommendations=3):
    # Find similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    
    # Get books rated by similar users
    similar_user_books = user_book_matrix.loc[similar_users].mean(axis=0)
    
    # Exclude books already rated by the user
    user_books = user_book_matrix.loc[user_id]
    books_to_recommend = similar_user_books[user_books == 0]
    
    # Recommend books with the highest average rating from similar users
    recommendations = books_to_recommend.sort_values(ascending=False).head(num_recommendations)
    
    return recommendations.index.tolist()

# Example usage
user_name = 'Alice'
recommended_books = recommend_books(user_name)
print(f"Recommended books for user {user_name}: {recommended_books}")

user_name = 'John'
recommended_books = recommend_books(user_name)
print(f"Recommended books for user {user_name}: {recommended_books}")

user_name = 'Bob'
recommended_books = recommend_books(user_name)
print(f"Recommended books for user {user_name}: {recommended_books}")

user_name = 'David'
recommended_books = recommend_books(user_name)
print(f"Recommended books for user {user_name}: {recommended_books}")




