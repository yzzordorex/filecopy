import sys, time
import os, shutil
import re
import inflect

infEng = inflect.engine()

#User paths
sourcePath = "/Users/bryan/Downloads/test/"
destPath = "/Volumes/Europa/Movies/"

#Define if path exists, checks if source and destination paths exist.
def doesDirectoryExist(p):
	if os.path.exists( p ) != True : 
		return False
	else :
		return True

if not doesDirectoryExist(sourcePath) :
	print "Source Path not found. Quitting."
	quit()
if not doesDirectoryExist(destPath) :
	print "Destination Path not found. Quitting."
	quit()

#Return files in path to a list
filesInSourceDir = os.listdir( sourcePath )
filesInDestinationDir = os.listdir( destPath )

while True:
    userInput = raw_input("Copy [a]udio files, [v]ideo files, [A]ll files or [q]uit? ")

    if re.match('^[avAq]$',userInput):
        break
    else:
    	print "Invalid input, try again."
        continue

#File extension types.
videoFileExts = ".avi", ".mpg", ".mpeg", ".mov", ".mp4", ".mkv", ".m4v"
audioFileExts = ".mp3", ".m4a", ".ogg", ".mka"

if userInput == "a" :
	fileTypes = audioFileExts
elif userInput == "v" :
	fileTypes = videoFileExts
elif userInput == "A" :
	fileTypes = audioFileExts + videoFileExts
elif userInput == "q" :
	print "Quitting."
	quit()

sourceFiles = []

for root, dirs, files in os.walk(sourcePath) :
	if dirs not in filesInDestinationDir :
		for name in dirs :
			newSubFolder = os.path.join(destPath, name)
			os.mkdir(newSubFolder)

	for name in files :
		lowercaseFileName = name.lower()

		if lowercaseFileName.endswith(fileTypes) :
			sourceFiles.append(name)

		if name not in filesInSourceDir:
			print 'name not in filesInSourceDir:', name

			for name in files :
				copyFile = os.path.join(root, name)
				shutil.copy(copyFile, destPath)

		if name in filesInSourceDir :
			print "name in sourcePath: ", name
			if name not in destPath :

				copyFile = os.path.join(root, name)
				print copyFile
				shutil.copyfile(copyFile, destPath)
