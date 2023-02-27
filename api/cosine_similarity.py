from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def get_similarity(target, candidates):
    candidates = np.array(candidates)
    target = np.expand_dims(np.array(target), axis=0)
    sim = cosine_similarity(target, candidates)
    sim = np.squeeze(sim).tolist()
    sort_index = np.argsort(sim)[::-1]
    sort_score = [sim[i] for i in sort_index]
    similarity_scores = zip(sort_index, sort_score)
    return similarity_scores
