import index.MovieDAO as movieDAO
import index.ImageIO as imageIO
import index.ActorDAO as actorDAO
import os
from util import Log
from index import SysConst

def rename():
    try:
        Log.info("rename pics begins")
        actors = actorDAO.getAllActorsFully()
        for actor in actors:
            renameActor(actor["name"], actor["short_name"])
    except Exception as err:
        Log.error("rename pics stopped: ")
        Log.exception(err)

def renameActor(actor, shortName):
    path = SysConst.getImageCachePath() + actor
    newPath = SysConst.getImageCachePath() + shortName
    exist = os.path.exists(path)
    exist2 = os.path.exists(newPath)
    if exist and not exist2:
        Log.info(path + " <--> " + newPath)
        os.rename(path, newPath)


if __name__ =='__main__':
    rename()