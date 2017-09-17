import index.ActorDAO as ActorDAO
import index.IndexActor as indexActor
from index import ActorFinder
from util import Log

def saveMovieToDB(skipActors):
    try:
        if not skipActors:
            newActors  = ActorFinder.findActors()
            if len(newActors) > 0:
                Log.info("find new actors:")
                #print(newActors)
            else:
                Log.info("no found new actor.")

        actors = ActorDAO.getAllActors()

        allMovies = []

        count = 600

        for actor in actors:
            count = count - 1
            if count < 0:
                break;

            Log.info("begin to read: " + str(actor))
            allMovies = indexActor.saveActorToDB(url=actor["url"], actor=actor["name"], cache=False)
            #print("find new movies: " + str(newMovies))
            if len(allMovies) > 0:
                ActorDAO.updateLastReadTime(actor["name"])
            else:
                Log.info("not found " + actor["name"] + "'s movies.")

        return allMovies
    except Exception as e:
        #print(e)
        Log.error(e)


saveMovieToDB(False)