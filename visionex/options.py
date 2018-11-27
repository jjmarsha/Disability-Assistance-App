from os import listdir
from os.path import isfile, join
import os

path = "/mnt/c/users/jm796/gcloud/visionex"
os.chdir(path)
mypath = '/mnt/c/users/jm796/Dropbox/Camera Uploads/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files = [ fi for fi in onlyfiles if not fi.endswith(('.mov', '.mp4')) ]


'''while True:

		onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	if onlyfiles.endswith	
		if len(onlyfiles) > oldsize:
			print("Getting new image")
			os.system('python3 database.py')
		oldsize = len(onlyfiles)
		'''