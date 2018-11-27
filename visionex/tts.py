import io
from os import listdir
from os.path import isfile, join
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()
path = "/mnt/c/users/jm796/gcloud/visionex"
os.chdir(path)

mypath = '/mnt/c/users/jm796/Dropbox/Camera Uploads/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files = [ fi for fi in onlyfiles if fi.endswith(('.mov', '.mp4')) ]
'''path = "/mnt/c/users/jm796/gcloud/visionex/monoAudio"
os.chdir(path)'''
import os
os.chdir(r"/mnt/c/users/jm796/Dropbox/Camera Uploads")

a = files[len(files) - 1]
a = ("{0}.flac").format(a[:len(a) - 4])
print(a)

p = (r"ffmpeg -i '{0}' -ac 1 '{1}'").format(files[len(files) - 1],a)
os.system(p)
# The name of the audio file to transcribe
#os.system('mv ' +a+ '.flac ' + '/mnt/c/users/jm796/gcloud/visionex/monoAudio/')

file_name = (r"/mnt/c/users/jm796/Dropbox/Camera Uploads/{0}").format(a)

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))

os.chdir(r"/mnt/c/users/jm796/Dropbox/Camera Uploads")
os.system(r"rm '{0}'".format(a))
os.system(r"rm '{0}'".format(files[len(files) - 1]))