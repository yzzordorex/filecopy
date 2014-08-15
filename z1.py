import os

usersDir = "/Users/"
sourceDir = "/Users/aimee/Downloads/test/"
destinationDir = "/Users/aimee/Downloads/dest/"
fakeDir = "/Users/SteveJobs/Secret/uber_secret/pc-BAK/My Documents/My Pictures/Steve/pr0n/"


# Rewrite the following as a function. 
# The function should accept one argument, a path to a directory
# It should return true if the directory exists
# It should return false if the directory does not exist
# test for the above two defined directories
# bonus points if you add more directories to test and demonstrate their output
# There will be a part two....

def pathCheck(p):
    if os.path.exists( p ) != True : 
		print "Could not find", p, "Quitting."
		quit()

#if os.path.exists( destinationDir ) != True :
#   print "Could not find", destinationDir, "Quitting."
#    quit()

pathCheck(usersDir)
pathCheck(sourceDir)
pathCheck(destinationDir)
pathcheck(fakeDir)