from index import MovieDAO
from index import SysConst
from ml import BayesTrainingFromDB as bayes

def forcast():
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


forcast()