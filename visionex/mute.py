from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types as Types
from google.cloud import vision
from google.cloud import storage
from google.cloud.vision import types
import re
from os import listdir
from os.path import isfile, join
import os
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import textts

mypath = '/mnt/c/users/jm796/Dropbox/Camera Uploads/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

clientVision = vision.ImageAnnotatorClient()
clientLanguage = language.LanguageServiceClient()
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

TOKEN = 'hED4sqJ7nVAAAAAAAAABGK9yMe5CsjWNjMlo_PWTYY4YfmwTho5xLYK_2yhTsDem'


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)


def TextRecognition():
	image = vision.types.Image()
	image.source.image_uri = 'gs://pictures-lab/a1.jpg'
	resp = clientVision.text_detection(image=image)
	return resp.text_annotations[0].description

def breakToSentence(p):
	sentenceEnders = re.compile('[.!?]')
	return sentenceEnders.split(p)

def analyzeOneSentence(sentence):
    data = {}
    document = Types.Document(
    content=sentence,
    type=language.enums.Document.Type.PLAIN_TEXT)
    ent_analysis = clientLanguage.analyze_entities(document=document)
    response = clientLanguage.analyze_entities(
document=document,
encoding_type='UTF32',)
    for entity in response.entities:
        data[entity.name] = entity_type[entity.type]
    return data

def listOfAnalyzedSentences(paragraph):
	listOfAnalyzed = []
	sentenceList = breakToSentence(paragraph)
	for s in sentenceList:
		listOfAnalyzed.append(analyzeOneSentence(s))
	return listOfAnalyzed


def createFileData(listOfAnalyzed):
	file = open("a.txt", "w")
	for i in range(len(listOfAnalyzed)):
		print(str(i+1)+'\n', file=file)
		for name in listOfAnalyzed[i].keys():
			print(name+":"+listOfAnalyzed[i][name] +'\n', file=file)
			
	file.close()
def createStoreParagraph():
	file = open("paragraph.txt", "w")
	file.write (TextRecognition())
	file.close()

def backup(LOCALFILE, BACKUPPATH):
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

def createData():
    createFileData(listOfAnalyzedSentences(TextRecognition()))
    createStoreParagraph()

# UP load to bucket



# Get Image from bucket and create a.txt and paragrapth.txt
createData()

textts.tts(TextRecognition())


#Send data to drop box
if __name__ == '__main__':
    # Check for an access token

    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. "
            "Open up backup-and-restore-example.py in a text editor and "
            "paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an "
            "access token from the app console on the web.")

    # Create a backup of the current settings file
    backup('a.txt','/a.txt')
    backup('paragraph.txt','/paragraph.txt')


print("end analyzing")
