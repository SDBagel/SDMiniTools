import glob
import shutil

# list = values that you want to move, file extension = eg. fasta, originFolderPath & destinationFolderPath = folderName of items
def SortByList(listPath, fileExtension, originFolderPath, destinationFolderPath):
    files = glob.glob(originFolderPath+"\\*."+fileExtension)
    list = open(listPath, "r").read()

    for file in files:
        filename = file.split('\\')[1][0:-(len(fileExtension)+1)]
        print(filename)
        if (filename in list):
            print("true")
            oldpath = originFolderPath+'\\'+filename+"."+fileExtension
            newpath = destinationFolderPath+'\\'+filename+"."+fileExtension
            shutil.move(oldpath, newpath)

    movedFiles = glob.glob(destinationFolderPath+"\\*."+fileExtension)
    print("Operation Completed: "+str(len(movedFiles))+" out of "+str(len(list.split("\n")))+" were moved to the destination folder.")
    input()

lP = input("ListPath >")
fE = input("FileExtension >")
oFP = input("Origin Folder >")
dFP = input("Destination Folder >")
SortByList(lP, fE, oFP, dFP)
