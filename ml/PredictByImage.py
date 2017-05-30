from index import SysConst
from index import SimilarDAO

def predict():
    conn = SysConst.getConnect()
    movies = SimilarDAO.getAllBaseMovies(conn)
    allTargetMovies = {}
    for movie in movies:
        base = movie["av_number"]
        allMovies = SimilarDAO.getSimilarsByBase(base, conn)
        i = 0
        for movie in allMovies:
            i += 1
            if movie["target"] in allTargetMovies:
                allTargetMovies[movie["target"]] = i + allTargetMovies[movie["target"]]
            else:
                allTargetMovies[movie["target"]] = i
    conn.close()

    list = []
    for name in allTargetMovies:
        list.append({"av_number": name, "similar": allTargetMovies[name]})

    list = sorted(list, key=lambda d: d["similar"], reverse=False)
    list = list[0:50]

    numberList = []
    for one in list:
        numberList.append(one["av_number"])

    return numberList


#print(predict())