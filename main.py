from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Creating an app instance
app = Flask(__name__)

# Loading and cleaning the data
movies = pd.read_csv('./data/data.csv')
movies = movies[['id', 'title', 'overview', 'genre']]

# Handling NaN values
movies['overview'] = movies['overview'].fillna('')
movies['genre'] = movies['genre'].fillna('')

# Adding a new column to store the tags
movies['tags'] = movies['overview'] + ' ' + movies['genre']

# Creating a count matrix
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(movies['tags'].values.astype('U')).toarray()

# Creating a similarity score matrix
similarity = cosine_similarity(vector)

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.json.get('title')
    if not movie_title:
        return jsonify({'error': 'Title is required'}), 400

    # Finding the index in a case-insensitive way
    matching_movies = movies[movies['title'].str.lower() == movie_title.lower()]
    if matching_movies.empty:
        return jsonify({'error': 'Movie not found'}), 404

    index = matching_movies.index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Extracting recommended titles
    recommendations = [movies.iloc[i[0]]['title'] for i in distances[1:6]]  # Exclude the input movie
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
