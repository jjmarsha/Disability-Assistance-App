from os import listdir
from os.path import isfile, join
import os

path = "/mnt/c/users/jm796/gcloud/visionex"
os.chdir(path)
mypath = '/mnt/c/users/jm796/Dropbox/Camera Uploads/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
oldsize = len(onlyfiles)


disadvantage = input('Which disable assistance do you want to you? ')
if disadvantage.lower() == 'blind':
		while True:
			onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
			if len(onlyfiles) > oldsize:
				print("Getting new image")
				os.system('python3 facetest.py')
			oldsize = len(onlyfiles)

elif disadvantage.lower() == 'deaf':
		while True:
			onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
			if len(onlyfiles) > oldsize:
				print("Getting new image")
				os.system('python3 stt.py')
			oldsize = len(onlyfiles)
elif disadvantage.lower() == 'mute':
	while True:
		onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		if len(onlyfiles) > oldsize:
			print("Getting new image")
			os.system('python3 mute.py')
		oldsize = len(onlyfiles)