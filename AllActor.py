# coding=utf-8

import index.ActorDAO as ActorDAO
import index.IndexActor as indexActor
from index import ActorFinder
from util import Log
import sys
import io
import traceback
from ml import BayesTrainingFromDB as bayes
from index import MovieDAO
from index import SysConst
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def saveMovieToDB(skipActors):
    try:
        if not skipActors:
            newActors  = ActorFinder.findActors()
            if len(newActors) > 0:
                Log.info("find new actors:")
                Log.info(newActors)
            else:
                Log.info("no found new actor.")

        actors = ActorDAO.getAllActors()

        allMovies = []

        count = 200

        for actor in actors:
            count = count - 1
            if count < 0:
                break;

            Log.info("begin to read: " + str(actor))
            allMovies = indexActor.saveActorToDB(url=actor["url"], actor=actor["name"], cache=False, shortName=actor["short_name"])
            #print("find new movies: " + str(newMovies))
            if len(allMovies) > 0:
                ActorDAO.updateLastReadTime(actor["name"])
            else:
                Log.info("not found " + actor["name"] + "'s movies.")

        forcast()

        return allMovies
    except Exception as e:
        Log.exception(e)

def forcast():
    Log.info("do forcast")
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
    saveMovieToDB(False)