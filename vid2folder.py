'''Notes:
	- Possible while loop to frequently check the source folder for new files.
	- Try merging movie counter and file counter into same function.
	- Look for movie file in /Downloads/some folder/ and copy entire folder to Destination
	- Check for music, add music option.
	- A copy progress counter would be nice.
	- Make a simple GUI.
		- Allow user to set Source and Destination paths
'''
import sys, time
import os, shutil
import re
import inflect

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
                        FileTransferSpeed, FormatLabel, Percentage, \
                        ProgressBar, ReverseBar, RotatingMarker, \
                        SimpleProgress, Timer, Attribute

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
filesInSourcePath = os.listdir( sourcePath )
filesInDestinationPath = os.listdir( destPath )

#File extension types.
movTypes = ".avi", ".mpg", ".mpeg", ".mov", ".mp4", ".mkv", ".m4v"
musicTypes = ".mp3", ".m4a", ".ogg", ".mka"

movieFiles = []
copySourceMoviesFiles = []

#Creates a list of all movie files in the Source destination and it's subfolders.
#movieFiles = [os.path.join(root, name)
# 				for root, dirs, files in os.walk(sourcePath)
#				for name in files
#				if name.endswith(movTypes)]

#Return files in paths to a list
filesInSourcePath = os.listdir( sourcePath )
filesInDestinationPath = os.listdir( destPath )

#Look for movie files in the source path and add to a list
#root returns the path of each file
#dirs returns sub folders of root
#files returns a list of files in root
for root, dirs, files in os.walk(sourcePath) :
	for name in files:
		if name.endswith(movTypes):
			movieFiles.append( name )
			filePathJoin = os.path.join(root, name)
			copySourceMoviesFiles.append( filePathJoin )

#for file in filesInSourcePath :
#	lowerFile = file.lower()
#	if lowerFile.endswith(movTypes) :
#		movieFiles.append(file)

movieFileCount = len(movieFiles)

#If any movie files are present in the Source folder, print movies found
if movieFileCount >= 1 :
	print movieFileCount, "[MOVIES FOUND:]\n", movieFiles, "\n\n", "Movie", infEng.plural("file", movieFileCount), "found in your Downloads folder and subfolders.\nWould you like to copy the", infEng.plural("movie", movieFileCount), "to you Movie folder now?\n"

	#Prompts if user would like to copy movies
	while True :
		userInp = raw_input("Enter 'y' to continue or 'q' to quit. ")
		acceptInp = re.match('^[yq]$',userInp)
		if acceptInp:
			break
		else :
			print "Invalid input. Enter 'y' to continue or 'q' to quit."
			continue

	if userInp == 'q':
		print "Quitting."
		quit()

	#Checks if movie already exists in Destination folder, copies movie to Destination folder if not.
	if userInp == 'y':

		for movFileName in movieFiles:
			if movFileName in os.listdir(destPath):
				print movFileName, "Already exists! [DID NOT COPY]"

			if movFileName not in os.listdir(destPath):
				
#				movSourceFilePath = sourcePath + movFile
#				movDestFilePath = destPath + movFile
#				copySourceMovies = str(copySourceMovies)

				print "Movies found in Downloads folder and subfolders:\n", movFileName, "[COPYING...]\nCopying movie to:", destPath
				# shutil.copytree(src, dst, symlinks=False, ignore=None)
				shutil.copytree(sourcePath, destPath, symlinks=False)

#				shutil.copy2(movFile, destPath)

				'''sourceFileSize = os.stat(movSourceFilePath).st_size
				copied = 0
				copySource = open(movSourceFilePath, 'rb')
				copyTarget = open(movDestFilePath, 'wb')

				while True:
					chunk = copySource.read(32768)
					if not chunk:
						break
					copyTarget.write(chunk)
					copied += len(chunk)
					print '\r%02d%%' % (copied * 100 / sourceFileSize),
					copySource.close()
					copyTarget.close()

				'pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=sourceFileSize).start()
				for i in range( ):
					time.sleep(0.01)
					pbar.update(i+1)
				pbar.finish()'''