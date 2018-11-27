

from google.cloud import vision
from google.cloud.vision import types

#client Object
client = vision.ImageAnnotatorClient()


image = vision.types.Image()

#image location
image.source.image_uri = 'gs://pictures-lab/happy.001.jpeg'

#gets words
resp = client.text_detection(image=image)

#print words
"""
for d in resp.text_annotations:
	print(d)"""

print(resp.text_annotations[0].description)
print()
print('\n'.join([d.description for d in resp.text_annotations]))
