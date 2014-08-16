'''Notes:
	- Possible while loop to frequently check the source folder for new files.
	- Try merging movie counter and file counter into same function.
	- Look for movie file in /Downloads/some folder/ and copy entire folder to Destination
	- Check for music, add music option.
	- A copy progress counter would be nice.
	- Make a simple GUI.
		- Allow user to set Source and Destination paths
		- 
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
		print "No, it's not valid."
		raise Exception
	else :
		print "Yes, it's valid."
		return True

try :
	print "Is", sourcePath, "valid?", doesDirectoryExist(sourcePath)
	print "Is", destPath, "valid?", doesDirectoryExist(destPath)
except :
	print "One more paths not found. Quitting."
	quit()

	#Return files in path to a list
#	filesInSourcePath = os.listdir( sourcePath )
#	filesInDestinationPath = os.listdir( destPath )

#Movie file types.
movTypes = ".avi", ".mpg", ".mpeg", ".mov", ".mp4", ".mkv", ".m4v"
movieFiles = []

#Return files in paths to a list
filesInSourcePath = os.listdir( sourcePath )
filesInDestinationPath = os.listdir( destPath )

#Is this redundant?
#Function to check if there are any files in the Source path, exit if none.
#def countFiles():
#	if os.listdir(sourcePath) == []:
#		print "The Downloads folder contains no files. Quitting."
#		quit()

def copyMovies():
	#Look for movie files in the source path and add to a list
	for file in filesInSourcePath :
		lowerFile = file.lower()
		if lowerFile.endswith(movTypes) :
			movieFiles.append(file)

	movieFileCount = len(movieFiles)

	#If any movie files are present in the Source folder, print movies found
	if movieFileCount >= 1 :
		print "\nMOVIES FOUND IN DOWNLOADS FOLDER:\n", movieFiles, "\n\n", movieFileCount, "Movie", infEng.plural("file", movieFileCount), "found in your Downloads folder.\nWould you like to copy the", infEng.plural("movie", movieFileCount), "to you Movie folder now?\n"

		#Prompts if user would like to copy movies
		while True :
			userInp = raw_input("Enter 'y' to continue or 'n' to quit. ")
			acceptInp = re.match('^[yn]$',userInp)
			if acceptInp:
				break
			else :
				print "Invalid input. Enter 'y' to continue or 'n' to quit."
				continue

		if userInp == 'n':
			print "Quitting."
			quit()

		#Checks if movie already exists in Destination folder, copies movie to Destination folder if not.
		if userInp == 'y':
			for movFile in movieFiles:
				print "Checking if", movFile, "already exists..."
				if movFile not in os.listdir(destPath):
					
					movSourceFilePath = sourcePath + movFile
					movDestFilePath = destPath + movFile

					sourceFileSize = os.stat(movSourceFilePath).st_size
					copied = 0
					copySource = open(movSourceFilePath, 'rb')
					copyTarget = open(movDestFilePath, 'wb')

					print movFile, "found.\nCopying to:", destPath
					shutil.copy2(movSourceFilePath, destPath)

					'''while True:
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

				if movFile in os.listdir(destPath):
					print movFile, "already exists. [DID NOT COPY]"

#countFiles()
copyMovies()
