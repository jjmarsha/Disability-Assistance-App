def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''
    import re
    # to split by multile characters

    #   regular expressions are easiest (and fastest)
    sentenceEnders = re.compile('[.!?]')
    
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList

p = """This is a sentence.  This is an excited sentence! And do you think this is a question?"""


sentences = splitParagraphIntoSentences(p)
for s in sentences:
    print (s.strip())