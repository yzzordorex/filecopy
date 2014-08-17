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
filesInSourcePath = os.listdir( sourcePath )
filesInDestinationPath = os.listdir( destPath )

#File extension types.
movTypes = ".avi", ".mpg", ".mpeg", ".mov", ".mp4", ".mkv", ".m4v"
musicTypes = ".mp3", ".m4a", ".ogg", ".mka"

movieFiles = []
copySourceMoviesFiles = []

for root, dirs, files in os.walk(sourcePath) :
	for name in files:
		if name.endswith(movTypes):
			movieFiles.append( name )
			filePathJoin = os.path.join(root, name)
			copySourceMoviesFiles.append( filePathJoin )

