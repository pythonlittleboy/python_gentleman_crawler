# -*- coding: UTF-8 -*-

import index.MovieDAO as movieDAO
import index.ImageIO as imageIO
import index.ActorDAO as actorDAO
import os
from util import Log

def downloadPicsByActors(actors):
    for actor in actors:
        downloadActor(actor)

def downloadPicsAllActors():
    try:
        Log.info("download pics begins")
        actors = actorDAO.getAllActorsFully()
        count = 0
        for actor in actors:
            count = count + downloadActor(actor["short_name"])
            if count > 1000:
                break
    except Exception as err:
        Log.error("download pics stopped: ")
        Log.exception(err)

def downloadActor(shortName):
    movies = movieDAO.getMoviesByCondition("short_name = '" + shortName + "' and wrong_pic is null")
    imageIO.checkDirPath(shortName)

    count = 0
    for movie in movies:
        saved = imageIO.saveImage(movie)
        if saved:
            count = count + 1
    return count

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