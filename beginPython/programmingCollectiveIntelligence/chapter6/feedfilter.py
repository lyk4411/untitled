import feedparser
import re

# Takes a filename of URL of a blog feed and classifies the entries
from beginPython.programmingCollectiveIntelligence.chapter6 import docclass


def read(feed,classifier):
  # Get feed entries and loop over them
  f=feedparser.parse(feed)
  for entry in f['entries']:
    print
    print ('-----')
    # Print the contents of the entry
    print ('Title:     '+ str(entry['title'].encode('utf-8')))
    print ('Publisher: '+ str(entry['publisher'].encode('utf-8')))
    print
    print (entry['summary'].encode('utf-8'))
    

    # Combine all the text to create one item for the classifier
    fulltext='%s\n%s\n%s' % (entry['title'],entry['publisher'],entry['summary'])
    print("fulltext:", fulltext)
    # Print the best guess at the current category
    print ('Guess: '+str(classifier.classify(entry)))

    # Ask the user to specify the correct category and train on that
    cl=input('Enter category: ')
    classifier.train(entry,cl)


def entryfeatures(entry):
  splitter=re.compile('\\W+')
  f={}
  
  # Extract the title words and annotate
  titlewords=[s.lower() for s in splitter.split(entry['title']) 
          if len(s)>2 and len(s)<20]
  for w in titlewords: f['Title:'+w]=1
  
  # Extract the summary words
  summarywords=[s.lower() for s in splitter.split(entry['summary']) 
          if len(s)>2 and len(s)<20]

  # Count uppercase words
  uc=0
  for i in range(len(summarywords)):
    w=summarywords[i]
    f[w]=1
    if w.isupper(): uc+=1
    
    # Get word pairs in summary as features
    if i<len(summarywords)-1:
      twowords=' '.join(summarywords[i:i+1])
      f[twowords]=1
    
  # Keep creator and publisher whole
  f['Publisher:'+entry['publisher']]=1

  # UPPERCASE is a virtual word flagging too much shouting  
  if float(uc)/len(summarywords)>0.3: f['UPPERCASE']=1
  
  return f

if __name__ == '__main__':
    cl = docclass.fisherclassifier(docclass.getwords)
    cl.setdb('python_feed.db')
    # read('python_search.xml', cl)

    print(cl.cprob('python', 'language'))
    print(cl.cprob('python', 'snake'))
    print(cl.cprob('python', 'monty'))
    print(cl.cprob('python', 'python'))
    print(cl.cprob('python', 'other'))
    print('===================================')
    print(cl.cprob('eric', 'monty'))
    print(cl.fprob('eric', 'monty'))
