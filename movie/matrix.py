import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds

def load_datasets(path1, path2):
    df_raw = pd.read_csv(path1)
    df_raw.drop('Unnamed: 0', axis = 1, inplace = True)
    movies_df = pd.read_csv(path2)
    ratings_df = df_raw.pivot(index = 'userId', columns ='movieId', values = 'rating').fillna(0)
    return df_raw, movies_df, ratings_df

def normalize(ratings_df):
    ratings = ratings_df.values
    mean_ratings = (np.true_divide(ratings.sum(1),(ratings!=0).sum(1))).reshape(-1, 1)
    ratings_normalized = []

    i = 0
    for row in ratings:
        new_mat = []
        for val in row:
            if val != 0:
                new_mat.append(val - mean_ratings[i][0])
            else:
                new_mat.append(0)
        ratings_normalized.append(new_mat)
        i += 1

    return np.array(ratings_normalized, dtype='float32'), mean_ratings

def factorization(ratings_normalized, mean_ratings, ratings_df):
    U, sigma, Vt = svds(ratings_normalized, k = 50)
    sigma = np.diag(sigma)
    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + mean_ratings.reshape(-1, 1)
    return pd.DataFrame(all_user_predicted_ratings, columns = ratings_df.columns)

def recommend_movies(predictions_df, userID, movies_df, original_ratings_df, num_recommendations=5):
    # Get and sort the user's predictions
    user_row_number = userID  # UserID starts at 1, not 0
    sorted_user_predictions = predictions_df.iloc[user_row_number].sort_values(ascending=False)
    # Get the user's data and merge in the movie information.
    user_data = original_ratings_df[original_ratings_df.userId == (userID)]
    user_full = (user_data.merge(movies_df, how = 'left', left_on = 'movieId', right_on = 'movieId'))
    # Recommend the highest predicted rating movies that the user hasn't seen yet.
    recommendations = (movies_df[~movies_df['movieId'].isin(user_full['movieId'])].
         merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left', left_on = 'movieId', right_on = 'movieId').rename(columns = {user_row_number: 'Predictions'}).
         sort_values('Predictions', ascending = False).iloc[:num_recommendations, :-1])
    return user_full, recommendations

def predictions(gen_ratings):
    df_raw, movies_df, ratings_df = load_datasets('./movie/data/206_common_users.csv', './movie/data/206_full_data.csv')
    ratings_normalized, mean_ratings = normalize(ratings_df)
    preds_df = factorization(ratings_normalized, mean_ratings, ratings_df)
    preds_df.loc[10991] =  np.array(gen_ratings).reshape(206)
    _, predictions = recommend_movies(preds_df, 10991, movies_df, df_raw, 20)
    return predictions
