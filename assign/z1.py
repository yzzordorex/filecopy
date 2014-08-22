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

def doesDirectoryExist(p):
	if os.path.exists( p ) != True : 
		return False
	else :
		return True


print "Is ", usersDir, "valid?", doesDirectoryExist(usersDir)
print "Is ", sourceDir, "valid?", doesDirectoryExist(sourceDir)
print "Is ", destinationDir, "valid?", doesDirectoryExist(destinationDir)
print "Is ", fakeDir, "valid?", doesDirectoryExist(fakeDir)


for root, dirs, files in os.walk("/Users/aimee/Downloads/"):
    print root
    print dirs
    print files
    print "\n==================\n"
    for filename in files:
        fullpath = os.path.join(root, filename)
        print fullpath
