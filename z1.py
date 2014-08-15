import os

sourceDir = "/Users/aimee/Downloads/test/"
destinationDir = "/Users/aimee/Downloads/dest/"


# Rewrite the following as a function. 
# The function should accept one argument, a path to a directory
# It should return true if the directory exists
# It should return false if the directory does not exist
# test for the above two defined directories
# bonus points if you add more directories to test and demonstrate their output
# There will be a part two....

if os.path.exists( sourceDir ) != True : 
    print "Could not find", sourceDir, "Quitting."
    quit()

if os.path.exists( destinationDir ) != True :
    print "Could not find", destinationDir, "Quitting."
    quit()

