def calcIDF(documents,uniqueWords):
    n = len(documents)
    term_dic= dict.fromkeys(uniqueWords,0)
    import math
    for id , dic in documents:
        for key, val in dic.items():
            if val>0:
                term_dic[key]+=1

    for key, val in term_dic.items():
        term_dic[key]= math.log(n/float(val))

    return term_dic
    


    
