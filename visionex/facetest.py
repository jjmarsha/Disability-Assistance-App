from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import io
from os import listdir
from google.cloud import storage
from os.path import isfile, join
import os
import textts
    
client = vision.ImageAnnotatorClient()

def detect_labels(path):
    """Detects labels in the file."""

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    answer = 'There are ';
    for label in labels:
        answer += label.description + ", "
    return answer


def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of Face objects with information about the picture.
    """

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations

def highlight_faces(image, faces, output_filename):
    """Draws a polygon around the faces, then saves to output_filename.

    Args:
      image: a file containing the image with the faces.
      faces: a list of faces found in the file. This should be in the format
          returned by the Vision API.
      output_filename: the name of the image file to be created, where the
          faces have polygons drawn around them.
    """
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')

    im.save(output_filename)

def main(input_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)


mypath = '/mnt/c/users/jm796/Dropbox/Camera Uploads/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files = [ fi for fi in onlyfiles if fi.endswith('.jpg') ]
print(files[len(files) - 1])
input_filename = '/mnt/c/users/jm796/Dropbox/Camera Uploads/'+files[len(files)-1]
main(input_filename,4)


textts.tts(detect_labels(input_filename))
# from pygame import mixer # Load the required library

# mixer.init()
# mixer.music.load('output.mp3')
# mixer.music.play()

#upload_blob("pictures-lab",'output.mp3',"output.mp3")
# from playsound import playsound
# playsound("output.mp3")
'''import vlc
print(dir(vlc))
p = vlc.("output.mp3")
p.play()'''
