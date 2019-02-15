import numpy as np

def similarity(user, ratings, kind='user', epsilon=1e-9):
    # epsilon -> small number for handling dived-by-zero errors
    if kind == 'user':
        sim = user.dot(ratings.T) + epsilon
    return (sim - np.min(sim))/(np.max(sim) - np.min(sim))

# def predict_topk(ratings, similarity, kind='user', k=40):
#     pred = np.zeros(ratings.shape)
#     if kind == 'user':
#         for i in range(ratings.shape[0]):
#             top_k_users = [np.argsort(similarity[:,i])[:-k-1:-1]]
#             for j in range(ratings.shape[1]):
#                 pred[i, j] = similarity[i, :][top_k_users].dot(ratings[:, j][top_k_users]) 
#                 pred[i, j] /= np.sum(np.abs(similarity[i, :][top_k_users]))
#     return pred
def predict(ratings, similarity, kind='user'):
    if kind == 'user':
        return similarity.dot(ratings) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif kind == 'item':
        return ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])

def predictions(gen_ratings):
    file = './movie/ratings.npy'
    ratings = np.load(file)
    gen_ratings = np.array(gen_ratings).reshape((1, 206))
    ind = np.where(gen_ratings == 0)[1]
    user_similarity = similarity(gen_ratings, ratings, kind='user')
    user_pred = predict(ratings, user_similarity, kind='user')
    return ind[np.argsort(user_pred[0])[:-20:-1]]    
