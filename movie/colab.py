import numpy as np

def similarity(user, ratings, kind='user', epsilon=1e-9):
    # epsilon -> small number for handling dived-by-zero errors
    if kind == 'user':
        sim = user.dot(ratings.T) + epsilon
    elif kind == 'item':
        sim = ratings.T.dot(ratings) + epsilon
    return (sim - np.min(sim))/(np.max(sim) - np.min(sim))

def predict(ratings, similarity, kind='user'):
    if kind == 'user':
        return similarity.dot(ratings) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif kind == 'item':
        return ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])

def predictions(gen_ratings):
    file = './movie/data/ratings.npy'
    ratings = np.load(file)
    gen_ratings = np.array(gen_ratings).reshape((1, 206))
    ind = np.where(gen_ratings == 0)[1]
    user_similarity = similarity(gen_ratings, ratings, kind='user')
    user_pred = predict(ratings, user_similarity, kind='user')
    item_similarity = similarity(0, ratings, kind='item')
    item_pred = predict(gen_ratings, item_similarity, kind='item')
    return ind[np.argsort(user_pred[0])[:-21:-1]], ind[np.argsort(item_pred[0][ind])[:-21:-1]]    
