from index import MovieDAO
from index import SysConst
from ml import BayesTrainingFromDB as bayes

def forcastToDB():
    localBayes = bayes.BayesTrainingFromDB("local")
    vrBayes = bayes.BayesTrainingFromDB("vr")

    movies = MovieDAO.getMoviesByCondition("local is null")
    conn = SysConst.getConnect()

    for movie in movies:
        local = localBayes.classify(movie["title"])
        vr = vrBayes.classify(movie["title"])

        if local == "pos" and vr == "pos":
            movie["vr_forcast"] = 1
        else:
            movie["vr_forcast"] = 0

        MovieDAO.updateMovieFile(conn, movie)

    conn.commit()
    conn.close()

def forcastToNumbers():
    localBayes = bayes.BayesTrainingFromDB("local")
    vrBayes = bayes.BayesTrainingFromDB("vr")

    movies = MovieDAO.getMoviesByCondition("local is null")

    for movie in movies:
        local = localBayes.probable(movie["title"])
        vr = vrBayes.probable(movie["title"])

        movie["vr_forcast"] = local + vr


    movies = sorted(movies, key=lambda d: d['vr_forcast'], reverse=True)

    numbers = []
    for i in range (0, 50):
        print(movies[i])
        numbers.append(movies[i]["av_number"])

    return numbers;

print(forcastToNumbers())