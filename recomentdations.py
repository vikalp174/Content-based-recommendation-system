def recomend(mat_vector, num):
    main_list = mat_vector[1]
    main_list.sort(key=lambda x: x[1], reverse=True)
    snd = []
    for i in range(1, num+1):
        snd.append(main_list[i][0])
    return snd
