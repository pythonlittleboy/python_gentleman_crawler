from index import SysConst
from index import DiskIndex
from index import MovieDAO
from index import DownloadDAO

def tagVR():
    vrPath = SysConst.getVRPath()
    movieFiles = DiskIndex.getMovies(vrPath)
    allNumbers = DownloadDAO.get_all_download()

    conn = SysConst.getConnect()

    for avNumber in allNumbers:
        name = avNumber.lower()
        first = name[0:name.find('-')]
        second = name[name.find('-') + 1:]
        for file in movieFiles:
            filename = file["filename"].lower()
            if filename.find(first) > -1 and filename.find(second) > -1:
                print("find " + name + " : " + file["fullpath"])
                movieFiles.remove(file)

                av = {"av_number": avNumber.upper(), "local": 1, "classic": 0, "vr": 1, "trash": 0}
                DownloadDAO.mark_download(conn, av)

                break

    conn.commit()
    conn.close()


def tagClassic():
    vrPath = SysConst.getClassicPath()
    movieFiles = DiskIndex.getMovies(vrPath)
    allNumbers = DownloadDAO.get_all_download()

    conn = SysConst.getConnect()

    for avNumber in allNumbers:
        name = avNumber.lower()
        first = name[0:name.find('-')]
        second = name[name.find('-') + 1:]
        for file in movieFiles:
            filename = file["filename"].lower()
            if filename.find(first) > -1 and filename.find(second) > -1:
                print("find " + name + " : " + file["fullpath"])
                movieFiles.remove(file)

                av = {"av_number": avNumber.upper(), "local": 1, "classic": 1, "vr": 0, "trash": 0}
                DownloadDAO.mark_download(conn, av)

                break

    conn.commit()
    conn.close()


def tagTrash():
    vrPath = SysConst.getTextPath()
    movieFiles = DiskIndex.getTxts(vrPath)
    allNumbers = DownloadDAO.get_all_download()

    conn = SysConst.getConnect()

    for avNumber in allNumbers:
        name = avNumber.lower()
        first = name[0:name.find('-')]
        second = name[name.find('-') + 1:]
        for file in movieFiles:
            filename = file["filename"].lower()
            if filename.find(first) > -1 and filename.find(second) > -1:
                print("find " + name + " : " + file["fullpath"])
                movieFiles.remove(file)

                av = {"av_number": avNumber.upper(), "local": 0, "classic": 0, "vr": 0, "trash": 1}
                DownloadDAO.mark_download(conn, av)

                break

    conn.commit()
    conn.close()


def tagDownload():
    path = SysConst.getDownloadPath()
    movieFiles = DiskIndex.getTxts(path)
    allNumbers = DownloadDAO.get_all_download()

    conn = SysConst.getConnect()

    for avNumber in allNumbers:
        name = avNumber.lower()
        first = name[0:name.find('-')]
        second = name[name.find('-') + 1:]
        for file in movieFiles:
            filename = file["filename"].lower()
            if filename.find(first) > -1 and filename.find(second) > -1:
                print("find " + name + " : " + file["fullpath"])
                movieFiles.remove(file)
                MovieDAO.markMovieDownload(conn, avNumber.upper())
                break

    conn.commit()
    conn.close()


def tagAll():
    tagTrash()
    tagClassic()
    tagVR()
    # tagDownload()


if __name__ =='__main__':
    tagClassic()
    tagVR()