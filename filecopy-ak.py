
import sys, time
import os, shutil
import re
import inflect

infEng = inflect.engine()

print "\n\n.................. file copy ..................."
print "................................................"

sourceDir = "/Users/aimee/Downloads/test/"
destinationDir = "/Users/aimee/Downloads/dest/"

if os.path.exists( sourceDir ) != True : 
    print "Could not find", sourceDir, "Quitting."
    quit()

if os.path.exists( destinationDir ) != True :
    print "Could not find", destinationDir, "Quitting."
    quit()

filesInSourceDir = os.listdir( sourceDir )
filesInDestinationDir = os.listdir( destinationDir )

if filesInSourceDir == []:
    print "Source directory contains no files. Quitting."
    quit()

audioFileExts = ".mp3",".ogg"
videoFileExts = ".avi", ".mpg", ".mpeg", ".mov", ".mp4", ".mkv", ".m4v"

while True:
    userInput = raw_input("Copy [a]udio files, [v]ideo files, or [A]ll files? ")

    if re.match('^[avA]$',userInput):
        break
    else:
        print "Copy [a]udio files, [v]ideo files, or [A]ll files? "
        continue

if userInput == "a" :
    fileTypes = audioFileExts
elif userInput == "v" :
    fileTypes = videoFileExts
elif userInput == "A" :
    fileTypes = audioFileExts + videoFileExts

sourceFiles = []
fileCount = 0
for file in filesInSourceDir :
    lowercaseFilename = file.lower()
    if lowercaseFilename.endswith(fileTypes) :
        sourceFiles.append(file)
        fileCount += 1

if fileCount >= 1 :

    print fileCount, infEng.plural("file", fileCount), "found in source folder. Would you like to copy now?"
    while True:
        userInput = raw_input("[c]opy or [q]uit? ")

        if re.match('^[cq]$',userInput):
            break
        else:
            print "Enter 'c' to copy or 'q' to quit. "
            continue

    if userInput == 'c':
        for sourceFile in sourceFiles:
            print "................................................"
            print "Checking destination for", sourceFile, "....."
            if sourceFile not in filesInDestinationDir :

                sourceFilePath = sourceDir + sourceFile
                statinfo = os.stat(sourceFileDir)
                fileSize = statinfo.st_size
                print "File size:", fileSize, "bytes"
                print "\nCopying", sourceFile, "to", destinationDir,".\n"
                shutil.copy2(sourceFilePath, destinationDir)
            
            else :
                print "File exists. Did not copy."
        print "Done."
