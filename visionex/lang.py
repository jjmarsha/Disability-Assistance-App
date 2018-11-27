"""from google.cloud import language

def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    dir(sent_analysis)
    sentiment = sent_analysis.sentiment

    ent_analysis = document.analyze_entities()
    dir(ent_analysis)
    entities = ent_analysis.entities

    return sentiment, entities


example_text = 'Python is such a great programming language'
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)
for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience) """

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
##text = u'Hello, world!'
from sentence import *

text = u'Michelangelo Caravaggio, Italian painter, is known for "The Calling of Saint Matthew".'
#put text into document
document = types.Document(
    content=text,
    type=language.enums.Document.Type.PLAIN_TEXT)



# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment
ent_analysis = client.analyze_entities(document=document)
#entities = ent_analysis.entities

response = client.analyze_entities(
document=document,
encoding_type='UTF32',)
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
for entity in response.entities:
    print('=' * 20)
    print('         name: {0}'.format(entity.name))
    print('         type: {0}'.format(entity_type[entity.type]))
    print('     metadata: {0}'.format(entity.metadata))
    print('     salience: {0}'.format(entity.salience))

"""
for e in entities:
    print(e.name)
    print(dir(e.DESCRIPTOR))


print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
"""
    