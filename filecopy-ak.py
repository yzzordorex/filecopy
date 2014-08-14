
import sys, time
import os, shutil
import re
import inflect

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
                        FileTransferSpeed, FormatLabel, Percentage, \
                        ProgressBar, ReverseBar, RotatingMarker, \
                        SimpleProgress, Timer

infEng = inflect.engine()

#Define paths and open Downloads folder
sourcePath = "/Users/aimee/Downloads/test/"
destinationPath = "/Users/aimee/Downloads/dest/"



#Define movie file types
movTypes = ".mp3",".ogg"
#movTypes = ".avi", ".mpg", ".mpeg", ".mov", ".mp4", ".mkv", ".m4v"

movieFiles = []

# Check: Source and Destination exist
if os.path.exists( sourcePath ) != True or os.path.exists( destinationPath ) != True :
	print "Could not find paths. Quitting."
	quit()

	
#Return files in path to a list
filesInSourcePath = os.listdir( sourcePath )
filesInDestinationPath = os.listdir( destinationPath )


#Are there files?
if filesInSourcePath == []:
	print "The Downloads folder contains no files. Quitting."
	quit()



#Look for movie files in the source path and add to a list
for file in filesInSourcePath :
	lowerFile = file.lower()
	if lowerFile.endswith(movTypes) :
		movieFiles.append(file)

movieFileCount = len(movieFiles)

if movieFileCount >= 1 :

    print "\nMOVIES FOUND IN DOWNLOADS FOLDER:\n", movieFiles
    print "\n\n", movieFileCount, "Movie", infEng.plural("file", movieFileCount)
    print " found in your Downloads folder.\nWould you like to copy now?\n"

    while True:
        userInp = raw_input("Enter 'y' to continue or 'n' to quit.\n ")

        if re.match('^[yn]$',userInp):
            break
        else:
            print "Invalid input. Enter 'y' to continue or 'n' to quit."
            continue

	if userInp == 'n':
		print "Quitting."
		quit()

            
            
    #Checks if movie already exists in Destination folder, copies movie to Destination folder if not.
    if userInp == 'y':
        for movFile in movieFiles:
            print "Checking if", movFile, "already exists..."
            if movFile not in os.listdir(destinationPath):

                movFilePath = sourcePath + movFile
                statinfo = os.stat(movFilePath)
                fileSize = statinfo.st_size
                print fileSize, "bytes"
                print movFile, "found.\nCopying to:", destinationPath,".\n"
                shutil.copy2(movFilePath, destinationPath)
                #pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=300).start() 
                #for i in range(fileSize):
                #    time.sleep(0.01)
                #    pbar.update(i+1)
                #pbar.finish()

            else :
                print movFile, "already exists. [DID NOT COPY]\n\n\n"
