import index.MovieDAO as movieDAO
import index.ImageIO as imageIO
import index.ActorDAO as actorDAO

def downloadPicsByActors(actors):
    for actor in actors:
        downloadActor(actor)

def downloadPicsAllActors():
    actors = actorDAO.getAllActorsFully()
    for actor in actors:
        downloadActor(actor["name"])

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