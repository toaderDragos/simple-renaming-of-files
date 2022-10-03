import os
import shutil

directory = 'D:\Android\Spirituality in Vietnam\imagini\Poze bune'
namesList = os.listdir(directory)
for oldFileName in namesList:
    newName = oldFileName.lower()
    oldPath = directory + '\\' + oldFileName
    newPath = directory + '\\' + newName
    shutil.move(oldPath, newPath)

    
