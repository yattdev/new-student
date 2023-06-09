import os

from PIL import Image
from settings import MEDIA_ROOT
def resizeImage(imagePath,width,height):
    with Image.open(imagePath) as img:
        img=img.resize((width,height))
        img.save(imagePath)

def createDirectoryIfNotExist(directory):
    os.chdir(MEDIA_ROOT/"apartment")
    if not os.path.isdir(directory):
        os.mkdir(directory)
def changeCurrentImages(directory):
    os.chdir(directory)
    fics=os.listdir(os.getcwd())
    for fic in fics:
        if os.path.isdir(fic):
            print(fic,end="/")
            changeCurrentImages(fic)
            os.chdir('..')
        elif os.path.isfile(fic):
            if('Agent' in os.getcwd()):
                resizeImage(fic,800,896)
            else:
                resizeImage(fic,600,800)
            print(fic,"redimenssionnée !!")

changeCurrentImages(MEDIA_ROOT)
