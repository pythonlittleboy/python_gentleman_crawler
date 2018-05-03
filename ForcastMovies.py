from ml import BayesTrainingFromDB as bayes
from index import MovieDAO
from index import SysConst

def forcast():
    print("do forcast")
    localBayes = bayes.BayesTrainingFromDB("local")
    vrBayes = bayes.BayesTrainingFromDB("vr")
    skipBayes = bayes.BayesTrainingFromDB("skip")
    trashBayes = bayes.BayesTrainingFromDB("trash")

    movies = MovieDAO.getMoviesByCondition("local = 0 and trash = 0 and skip = 0")

    conn = SysConst.getConnect()
    for movie in movies:
        token = movie["av_number"] + movie["actor"] + movie["title"]
        # token = movie["av_number"] + movie["title"]
        local = localBayes.probable(token)
        vr = vrBayes.probable(token)
        skip = skipBayes.probable(token)
        trash = trashBayes.probable(token)

        #movie["vr_forcast"] = local + vr
        forcast = round((vr - skip * 0.4 - trash * 0.01 + local * 0.3) * 10000)
        MovieDAO.updateMovieVRForcast(movie["av_number"], forcast, conn)
        
    conn.commit()
    conn.close()

if __name__ =='__main__':
    forcast()