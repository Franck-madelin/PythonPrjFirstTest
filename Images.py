"""
Created on 2 janv. 2020

@author: franck
"""

import os
import sys
from distutils.file_util import copy_file


def getImgPath():
    cpt = 0
    images = list()
    for folder, subf, files in os.walk(c[0]):
        # print("in folder " + folder)
        subf[:] = [sf for sf in subf if not sf[0] == '.']
        files[:] = [f for f in files if not f[0] == "."]

        # exit()
        for file in files:
            if file.endswith(".jpg"):
                # print("    find file "+ folder  + file )
                images.append(folder + "/" + file)
                cpt += 1
                if cpt > 20:
                    break
            if cpt > 20:
                break
        if cpt > 20:
            break

    return images


def saveFile(stringListe):
    pathImg = os.getcwd() + "/Images"
    if not os.path.exists(pathImg):
        os.mkdir(pathImg)
    for fichier in stringListe:
        d = copy_file(fichier, pathImg)
        print(d)
    print("Nous avons sauve %s images" % (len(stringListe)))
    return

------
is_windows = sys.platform.startswith('win')

if is_windows:
    c = list()
    c.append(os.path.expanduser('~'))
    c.append(os.path.expanduser('~') + "/Pictures")
    c.append(os.path.expanduser('~') + "/Photos")

# print(c)
liste = getImgPath()
saveFile(liste)
"""hummm"""