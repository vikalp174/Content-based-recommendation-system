def termFriqCalculator(doc, docDic):
    n = len(doc)
    tfDic = {}
    for key, val in docDic.items():
        tfDic[key] = val/float(n)
    return tfDic


def tF_cal(main_metrix, uniqueWords):
    tf_mat = []
    for id, doc in main_metrix:
        # make dictionary of the document
        docDic = dict.fromkeys(uniqueWords, 0)
        # calculate how may times that word came in that document and update it in the dictionary
        for val in doc:
            docDic[val] += 1
        # calculate term friquency of the terms in the doc
        tf = termFriqCalculator(doc, docDic)
        # add the final dictionary to the mattrix along with its id
        tf_mat.append([id, tf])
    return tf_mat


