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

#downloadPicsByActors(["一之濑遥"])
downloadPicsAllActors()