from os import listdir
from os.path import isfile, join
import os
mypath = '/mnt/c/users/jm796/Dropbox/Camera Uploads/'
#mypath = os.path.join( "C:", "Users", "jm796", "Dropbox", "Apps", "Pictopia" )
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles[len(onlyfiles) - 2])


