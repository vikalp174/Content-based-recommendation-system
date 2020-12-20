def tf_idf_cal(tf_matrix,idf_dic):
    matrix=[]
    for id, dic in tf_matrix:
        idf_tf = {}
        for key, val in dic.items():
            idf_tf [key]= val*idf_dic[key]
        matrix.append([id,idf_tf])
    return matrix
