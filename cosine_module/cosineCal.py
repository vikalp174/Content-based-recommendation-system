from math import sqrt


def square_rooted(x):

    return round(sqrt(sum([a*a for a in x])), 3)


def cosine_similarity(x, y):
    numerator = sum(a*b for a, b in zip(x, y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator), 3)


def cosin_cal(ids, tf_m_idf_mat):
    similarity_mat = []
    for i in ids:
        dic = {}
        for j in ids:
            cosine = cosine_similarity(tf_m_idf_mat[i-1], tf_m_idf_mat[j-1])
            dic[j] = cosine
        similarity_mat.append([i, dic])
    return similarity_mat
