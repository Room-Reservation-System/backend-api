from os import walk, path, remove

def clearAll(dirPath:str):

    # dirPath=path.dirname(path.realpath(__file__))
    files=[]
    for (dPath,dNames,dFiles) in walk(dirPath):
        files.extend(dFiles)
    for file in files:
        remove(path.join(dirPath,file))