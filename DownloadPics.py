import index.MovieDAO as movieDAO
import index.ImageIO as imageIO
import index.ActorDAO as actorDAO
from util import Log

def downloadPicsByActors(actors):
    for actor in actors:
        downloadActor(actor)

def downloadPicsAllActors():
    try:
        Log.info("download pics begins")
        actors = actorDAO.getAllActorsFully()
        for actor in actors:
            downloadActor(actor["name"])
    except Exception as err:
        Log.error("download pics stopped: ")
        Log.error(err)

def downloadActor(actor):
    movies = movieDAO.getMoviesByCondition("actor = '" + actor + "' and wrong_pic is null")
    imageIO.checkDirPath(actor)
    for movie in movies:
        imageIO.saveImage(movie)

def deleteNotExistImageMovies():
    actors = actorDAO.getAllActorsFully()
    for actor in actors:
        deleteNotExistImageMoviesActor(actor["name"])

def deleteNotExistImageMoviesActor(actor):
    movies = movieDAO.getMoviesByCondition("actor = '" + actor + "'")
    for movie in movies:
        if not imageIO.isExistImage(movie):
            movieDAO.deleteMovie(movie["av_number"])

#downloadPicsByActors(["xxx"])
downloadPicsAllActors()
#deleteNotExistImageMovies()