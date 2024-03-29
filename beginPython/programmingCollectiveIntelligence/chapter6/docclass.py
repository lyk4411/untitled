# from pysqlite2 import dbapi2 as sqlite
import re
import math
import sqlite3 as sqlite


def getwords(doc):
  splitter=re.compile('\\W+')
  print ('str: ', str(doc))
  # Split the words by non-alpha characters
  # temp = [s for s in splitter.split(str(doc)) if s != None]
  words=[s.lower() for s in splitter.split(str(doc)) if len(s)>2 and len(s)<20 and s != None and s != '']
  
  # Return the unique set of words only
  return dict([(w,1) for w in words])

class classifier:
  def __init__(self,getfeatures,filename=None):
    # Counts of feature/category combinations
    self.fc={}
    # Counts of documents in each category
    self.cc={}
    self.getfeatures=getfeatures
    
  def setdb(self,dbfile):
    self.con=sqlite.connect(dbfile)    
    self.con.execute('create table if not exists fc(feature,category,count)')
    self.con.execute('create table if not exists cc(category,count)')


  def incf(self,f,cat):
    count=self.fcount(f,cat)
    if count==0:
      self.con.execute("insert into fc values ('%s','%s',1)"
                       % (f,cat))
    else:
      self.con.execute(
        "update fc set count=%d where feature='%s' and category='%s'"
        % (count+1,f,cat))
    # self.fc.setdefault(f,{})
    # self.fc[f].setdefault(cat,0)
    # self.fc[f][cat]+=1
  
  def fcount(self,f,cat):
    res=self.con.execute(
      'select count from fc where feature="%s" and category="%s"'
      %(f,cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])
    # if f in self.fc and cat in self.fc[f]:
    #   return float(self.fc[f][cat])
    # return 0.0

  def incc(self,cat):
    count=self.catcount(cat)
    if count==0:
      self.con.execute("insert into cc values ('%s',1)" % (cat))
    else:
      self.con.execute("update cc set count=%d where category='%s'"
                       % (count+1,cat))
    # self.cc.setdefault(cat,0)
    # self.cc[cat]+=1

  def catcount(self,cat):
    res=self.con.execute('select count from cc where category="%s"'
                         %(cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])
    # if cat in self.cc:
    #   return float(self.cc[cat])
    # return 0

  def categories(self):
    cur=self.con.execute('select category from cc');
    return [d[0] for d in cur]
    # return self.cc.keys()

  def totalcount(self):
    res=self.con.execute('select sum(count) from cc').fetchone();
    if res==None: return 0
    return res[0]
    # return sum(self.cc.values())


  def train(self,item,cat):
    features=self.getfeatures(item)
    # Increment the count for every feature with this category
    for f in features:
      self.incf(f,cat)

    # Increment the count for this category
    self.incc(cat)
    self.con.commit()

  def fprob(self,f,cat):
    if self.catcount(cat)==0: return 0

    # The total number of times this feature appeared in this 
    # category divided by the total number of items in this category
    return self.fcount(f,cat)/self.catcount(cat)

  def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
    # Calculate current probability
    basicprob=prf(f,cat)

    # Count the number of times this feature has appeared in
    # all categories
    totals=sum([self.fcount(f,c) for c in self.categories()])

    # Calculate the weighted average
    bp=((weight*ap)+(totals*basicprob))/(weight+totals)
    return bp




class naivebayes(classifier):
  
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.thresholds={}
  
  def docprob(self,item,cat):
    features=self.getfeatures(item)   

    # Multiply the probabilities of all the features together
    p=1
    for f in features: p*=self.weightedprob(f,cat,self.fprob)
    return p

  def prob(self,item,cat):
    catprob=self.catcount(cat)/self.totalcount()
    docprob=self.docprob(item,cat)
    return docprob*catprob
  
  def setthreshold(self,cat,t):
    self.thresholds[cat]=t
    
  def getthreshold(self,cat):
    if cat not in self.thresholds: return 1.0
    return self.thresholds[cat]
  
  def classify(self,item,default=None):
    probs={}
    # Find the category with the highest probability
    max=0.0
    for cat in self.categories():
      probs[cat]=self.prob(item,cat)
      if probs[cat]>max: 
        max=probs[cat]
        best=cat

    # Make sure the probability exceeds threshold*next best
    for cat in probs:
      if cat==best: continue
      if probs[cat]*self.getthreshold(best)>probs[best]: return default
    return best

class fisherclassifier(classifier):
  def cprob(self,f,cat):
    # The frequency of this feature in this category    
    clf=self.fprob(f,cat)
    if clf==0: return 0

    # The frequency of this feature in all the categories
    freqsum=sum([self.fprob(f,c) for c in self.categories()])

    # The probability is the frequency in this category divided by
    # the overall frequency
    p=clf/(freqsum)
    
    return p
  def fisherprob(self,item,cat):
    # Multiply all the probabilities together
    p=1
    features=self.getfeatures(item)
    for f in features:
      p*=(self.weightedprob(f,cat,self.cprob))

    # Take the natural log and multiply by -2
    fscore=-2*math.log(p)

    # Use the inverse chi2 function to get a probability
    return self.invchi2(fscore,len(features)*2)
  def invchi2(self,chi, df):
    m = chi / 2.0
    sum = term = math.exp(-m)
    for i in range(1, df//2):
        term *= m / i
        sum += term
    return min(sum, 1.0)
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.minimums={}

  def setminimum(self,cat,min):
    self.minimums[cat]=min
  
  def getminimum(self,cat):
    if cat not in self.minimums: return 0
    return self.minimums[cat]
  def classify(self,item,default=None):
    # Loop through looking for the best result
    best=default
    max=0.0
    for c in self.categories():
      p=self.fisherprob(item,c)
      # Make sure it exceeds its minimum
      if p>self.getminimum(c) and p>max:
        best=c
        max=p
    return best


def sampletrain(cl):
  cl.train('Nobody owns the water.','good')
  cl.train('the quick rabbit jumps fences','good')
  cl.train('buy pharmaceuticals now','bad')
  cl.train('make quick money at the online casino','bad')
  cl.train('the quick brown fox jumps','good')

if __name__ == '__main__':
    # cl = classifier(getwords)
    # cl.train('the quick brown fox jumps over the lazy dog', 'good')
    # cl.train('make quick money in the online casino', 'bad')
    # print(cl.fcount('quick', 'good'))
    # print(cl.fcount('quick', 'bad'))

    # sampletrain(cl)
    # # print(cl.fprob('quick','good'))
    # print(cl.weightedprob('money','good',cl.fprob))
    # sampletrain(cl)
    # print(cl.weightedprob('money','good',cl.fprob))

    # cl = naivebayes(getwords)
    # sampletrain(cl)
    # print(cl.prob('quick rabbit', 'good'))
    # print(cl.prob('quick rabbit', 'bad'))
    # print('===============================================================================')
    # print(cl.classify('quick rabbit', default='unknown'))
    # print(cl.classify('quick money', default='unknown'))
    # cl.setthreshold('bad', 3.0)
    # print(cl.classify('quick rabbit', default='unknown'))
    # print(cl.classify('quick money', default='unknown'))
    # print('===============================================================================')
    # for i in range(10):
    #   sampletrain(cl)
    # print('===============================================================================')
    #
    # print(cl.classify('quick money', default='unknown'))
    #
    # print('===============================================================================')

    # cl = fisherclassifier(getwords)
    # sampletrain(cl)
    # print('quick: ',   cl.cprob('quick', 'good'))
    # # print('money: ',   cl.cprob('money', 'bad'))
    # # print('casino: ',  cl.cprob('casino', 'good'))
    # # print('weight of money: ', cl.weightedprob('money', 'bad', cl.cprob))
    # print('fisher''s quick: ', cl.fisherprob('guick','good'))
    # print('fisher''s quick rabbit: ', cl.fisherprob('guick rabbit','good'))
    # print('quick rabbit: ', cl.cprob('guick rabbit','good'))
    # print('fisher''s quick rabbit: ', cl.fisherprob('guick rabbit','bad'))

    cl = fisherclassifier(getwords)
    cl.setdb('test2.db')
    sampletrain(cl)
    cl2 = naivebayes(getwords)
    cl2.setdb('test2.db')
    print(cl2.classify('quick money'))
    print(cl2.weightedprob('quick', 'good', cl2.fprob))
    print(cl2.weightedprob('quick', 'bad', cl2.fprob))






