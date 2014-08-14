
import sys, time
import os, shutil
import re
import inflect

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
                        FileTransferSpeed, FormatLabel, Percentage, \
                        ProgressBar, ReverseBar, RotatingMarker, \
                        SimpleProgress, Timer

infEng = inflect.engine()

print "\n\n.................. file copy ..................."

sourcePath = "/Users/aimee/Downloads/test/"
destinationPath = "/Users/aimee/Downloads/dest/"

if os.path.exists( sourcePath ) != True : 
	print "Could not find", sourcePath, "Quitting."
	quit()

if os.path.exists( destinationPath ) != True :
    print "Could not find", destinationPath, "Quitting."
    quit()

filesInSourcePath = os.listdir( sourcePath )
filesInDestinationPath = os.listdir( destinationPath )

if filesInSourcePath == []:
	print "Source directory contains no files. Quitting."
	quit()

fileTypes = ".mp3",".ogg" #,".avi", ".mpg", ".mpeg", ".mov", ".mp4", ".mkv", ".m4v"
sourceFiles = []
fileCount = 0
for file in filesInSourcePath :
	lowercaseFilename = file.lower()
	if lowercaseFilename.endswith(fileTypes) :
        sourceFiles.append(file)
        fileCount += 1

if fileCount >= 1 :

    print fileCount, infEng.plural("file", fileCount), "found in source folder.\nWould you like to copy now?"
    print "................................................"
    while True:
        userInput = raw_input("Enter 'y' to continue or 'n' to quit.\n ")

        if re.match('^[yn]$',userInput):
            break
        else:
            print "Enter 'y' to continue or 'n' to quit."
            continue

    if userInput == 'y':
        for sourceFile in sourceFiles:
            print "Checking destination for", sourceFile, "....."
            if sourceFile not in filesInDestinationPath :

                sourceFilePath = sourcePath + sourceFile
                statinfo = os.stat(sourceFilePath)
                fileSize = statinfo.st_size
                print "File size:", fileSize, "bytes"
                print "\nCopying", sourceFile, "to", destinationPath,".\n"
                shutil.copy2(sourceFilePath, destinationPath)
                #pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=300).start() 
                #for i in range(fileSize):
                #    time.sleep(0.01)
                #    pbar.update(i+1)
                #pbar.finish()

            else :
                print "File exists. Did not copy."
        print "Done."
