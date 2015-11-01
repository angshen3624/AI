# Name: Jixiao Ma, Huaipei Lu, Ang Shen
# Date: 05/24/2015
# Description: naive bayes classifier for text classification
#
#

import math, os, pickle, re
import random

class Bayes_Classifier:

   def __init__(self):
      """This method initializes and trains the Naive Bayes Sentiment Classifier.  If a 
      cache of a trained classifier has been stored, it loads this cache.  Otherwise, 
      the system will proceed through training.  After running this method, the classifier 
      is ready to classify input text."""

      if os.path.exists(r'./positive.txt') and os.path.exists(r'./negative.txt'):
         self.positive = self.load('positive.txt')
         self.negative = self.load('negative.txt')
      else:
         self.positive = {}
         self.positive['total*'] = 0
         self.positive['pos_num*'] = 0
         self.negative = {}
         self.negative['total*'] = 0
         self.negative['neg_num*'] = 0
         self.train()

   def train(self):   
      """Trains the Naive Bayes Sentiment Classifier."""
      lFileList = []
      for fFileObj in os.walk("./movies_reviews/"):
         lFileList = fFileObj[2]
         break

      for file_name in lFileList:
         self.genData_pres(file_name)

      self.save(self.positive, "positive.txt")
      self.save(self.negative, "negative.txt")
    
   def classify(self, sText):
      """Given a target string sText, this function returns the most likely document
      class to which the target string belongs (i.e., positive, negative or neutral).
      """
      word_lst = self.tokenize(sText)
      pos_num = self.positive['pos_num*']
      neg_num = self.negative['neg_num*']

      pos_prior = float(pos_num)/(pos_num+neg_num)
      neg_prior = float(neg_num)/(pos_num+neg_num)

      temp_positive = {}
      temp_negative = {}
      pos_sum = 0
      neg_sum = 0

      for word in word_lst:
         if word not in self.positive:
            temp_positive[word] = 1
         if word not in self.negative:
            temp_negative[word] = 1

      pos_V = len(self.positive.keys()) + len(temp_positive.keys())
      neg_V = len(self.negative.keys()) + len(temp_negative.keys())
      pos_denominator = float(self.positive['total*'] + pos_V)
      neg_denominator = float(self.negative['total*'] + neg_V)

      for word in word_lst:
         if word in self.positive:
            pos_sum += math.log((self.positive[word]+1)/pos_denominator)
         else:
            pos_sum += math.log(1/pos_denominator)

         if word in self.negative:
            neg_sum += math.log((self.negative[word]+1)/neg_denominator)
         else:
            neg_sum += math.log(1/neg_denominator)

      pos_prob = pos_sum + math.log(pos_prior)
      neg_prob = neg_sum + math.log(neg_prior)

      diff = pos_prob - neg_prob
      if math.fabs(diff) < 0.1:
         return 'neutral'
      elif diff > 0:
         return 'positive'
      else:
         return 'negative'


   def loadFile(self, sFilename):
      """Given a file name, return the contents of the file as a string."""

      f = open(sFilename, "r")
      sTxt = f.read()
      f.close()
      return sTxt
   
   def save(self, dObj, sFilename):
      """Given an object and a file name, write the object to the file using pickle."""

      f = open(sFilename, "w")
      p = pickle.Pickler(f)
      p.dump(dObj)
      f.close()
   
   def load(self, sFilename):
      """Given a file name, load and return the object stored in the file."""

      f = open(sFilename, "r")
      u = pickle.Unpickler(f)
      dObj = u.load()
      f.close()
      return dObj

   def tokenize(self, sText): 
      """Given a string of text sText, returns a list of the individual tokens that 
      occur in that string (in order)."""

      lTokens = []
      ## sText = sText.lower().strip()
      sToken = ""
      for c in sText:
         if re.match("[a-zA-Z0-9]", str(c)) != None or c == "\"" or c == "_" or c == "-":
            sToken += c
         else:
            if sToken != "":
               lTokens.append(sToken)
               sToken = ""
            if c.strip() != "":
               lTokens.append(str(c.strip()))
               
      if sToken != "":
         lTokens.append(sToken)

      return lTokens

   def genData(self, file_name):
      """
      generate data for each training document
      and modify the positive dict(freq) or negative dict(freq)
      """
      temp_label = re.search("-[0-9]-", file_name).group(0) ##get -1- or -5-
      label = re.search("[0-9]", temp_label).group(0) ##get 1 or 5
      path = "./movies_reviews/" + str(file_name) ##training sets location
      dat = self.loadFile(path) ##load file
      words = self.tokenize(dat) ##get words
      if label == '5': ##positive label
         self.positive['pos_num*'] += 1
         for word in words:
            self.positive['total*'] += 1 ##define a name to store the total number of words being checked for positive
            if word not in self.positive:
               self.positive[word] = 1 ## word is not in dict, add it
            else:
               self.positive[word] += 1 ## word is in dict, add one to its number
      elif label == '1': ##negative label
         self.negative['neg_num*'] += 1
         for word in words:
            self.negative['total*'] += 1 ##define a name to store the total number of words being checked for negative
            if word not in self.negative:
               self.negative[word] = 1 ## word is not in dict, add it
            else:
               self.negative[word] += 1 ## word is in dict, add one to its number
   def genData_freq(self, file_name):
      """
      generate data for each training document
      and modify the positive dict(freq) or negative dict(freq)
      """
      temp_label = re.search("-[0-9]-", file_name).group(0) ##get -1- or -5-
      label = re.search("[0-9]", temp_label).group(0) ##get 1 or 5
      path = "./movies_reviews/" + str(file_name) ##training sets location
      dat = self.loadFile(path) ##load file
      words = self.tokenize(dat) ##get words

      if label == '5': ##positive label
         self.positive['pos_num*'] += 1
         for word in words:
            self.positive['total*'] += 1 ##define a name to store the total number of words being checked for positive
            if word not in self.positive:
               self.positive[word] = 1 ## word is not in dict, add it
            else:
               self.positive[word] += 1 ## word is in dict, add one to its number
      elif label == '1': ##negative label
         self.negative['neg_num*'] += 1
         for word in words:
            self.negative['total*'] += 1 ##define a name to store the total number of words being checked for negative
            if word not in self.negative:
               self.negative[word] = 1 ## word is not in dict, add it
            else:
               self.negative[word] += 1 ## word is in dict, add one to its number

   def genData_pres(self, file_name):
      """
      generate data for each training document
      and modify the positive dict(freq) or negative dict(pres)
      """
      temp_label = re.search("-[0-9]-", file_name).group(0) ##get -1- or -5-
      label = re.search("[0-9]", temp_label).group(0) ##get 1 or 5
      path = "./movies_reviews/" + str(file_name) ##training sets location
      dat = self.loadFile(path) ##load file
      words = self.tokenize(dat) ##get words

      ## get unique words
      uniq_words = list(set(words))

      if label == '5': ##positive label
         self.positive['pos_num*'] += 1
         for word in uniq_words:
            self.positive['total*'] += 1 ##define a name to store the total number of words being checked for positive
            if word not in self.positive:
               self.positive[word] = 1 ## word is not in dict, add it
            else:
               self.positive[word] += 1 ## word is in dict, add one to its number
      elif label == '1': ##negative label
         self.negative['neg_num*'] += 1
         for word in uniq_words:
            self.negative['total*'] += 1 ##define a name to store the total number of words being checked for negative
            if word not in self.negative:
               self.negative[word] = 1 ## word is not in dict, add it
            else:
               self.negative[word] += 1 ## word is in dict, add one to its number

   def test(self):
      """
      we use 10-fold validation to test the naive bayes classifier.
      we can also get the tp/tn/fp/fn.
      """
      ##lFileList = []
      lFileList = []
      for fFileObj in os.walk("./movies_reviews/"):
         lFileList = fFileObj[2]
         break

      file_list = lFileList
      random.shuffle(file_list) ##random the order

      err_num = 0
      tp = 0
      fp = 0
      tn = 0
      fn = 0

      total_num = len(file_list) ## total number of training
      test_num = round(0.1 * total_num) ## 10% of training to test
      train_num = total_num - test_num ## 90% of training to train

      for i in range(10):

         self.positive = {}
         self.positive['total*'] = 0
         self.positive['pos_num*'] = 0
         self.negative = {}
         self.negative['total*'] = 0
         self.negative['neg_num*'] = 0

         test_start = int(test_num*i)
         test_end = int((test_num-1) + test_num*i)

         for j in range(total_num):
            if j < test_start or j > test_end:
               self.genData_freq(file_list[j])

         for k in range(test_start, test_end):
            temp_label = re.search("-[0-9]-", file_list[k]).group(0) ##get -1- or -5-
            true_label = re.search("[0-9]", file_list[k]).group(0) ##get 1 or 5
            if true_label == '5':
               true_label = 'positive'
            elif true_label == '1':
               true_label = 'negative'
            path = "./movies_reviews/" + str(file_list[k])
            dat = self.loadFile(path)
            classified_label = self.classify(dat)

            if classified_label == true_label:
               if classified_label == 'positive':
                  tp += 1
               if classified_label == 'negative':
                  tn += 1
            if classified_label != true_label:
               err_num += 1
               if classified_label == 'positive':
                  fp += 1
               if classified_label == 'negative':
                  fn += 1

      acc = float(err_num)/(10*test_num)
      precision = float(tp)/(tp+fp)
      recall = float(tp)/(tp+fn)
      F1 = float(2*(precision*recall))/(precision+recall)
      print acc,precision,recall,F1









