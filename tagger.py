# running the Stanford POS Tagger from NLTK
from turtle import pos
import nltk
from nltk import word_tokenize
#from nltk import StanfordTagger
from fractions import Fraction 
import os
import pandas as pd
import scipy.stats as stats

 
#list of words that get mis-tagged in this specific case
mistags = ['allow', 'up']

data = [];

for file in os.listdir("./"):
    if file.endswith(".txt"):

        text_raw = open(os.path.join("./", file)).read()
        #text_raw = text_raw.replace("\n", " ")
        text = nltk.word_tokenize(text_raw)
        pos_tagged = nltk.pos_tag(text)
        
        determinerCount = 0
        demonstrativeDeterminerCount = 0

        wordIndex = 0
        for word,word_class in pos_tagged:
            #if the word is a determiner 
            if (word_class == "DT"):
                #increment the determiner count
                determinerCount += 1
                #if this determiner has the potential to be demonstrative
                if (word == "this" or word == "that" or word == "these" or word == "those"):
                    #and this is not the last word in the data set
                    if (wordIndex+1<len(pos_tagged)):
                        #then determine the tag of the following word
                        tag = pos_tagged[wordIndex+1][1]
                        following_word = pos_tagged[wordIndex+1][0]
                        #and if followed by noun or adjective
                        if (tag == "NN" or tag == "NNS" or tag == "NNP" or tag == "NNPS" or tag == "JJ" or tag == "JJR" or tag == "JJS"):
                            #if the following word is not marked as a mis-tag in the case of demonstrative determiners
                            if following_word not in mistags:
                                #then increment the demonstrative determiner count
                                demonstrativeDeterminerCount += 1
                                print(word + " " + following_word)
            #increment the index used to keep track of current touple
            wordIndex += 1

        print("For file {}:".format(file)) 
        print("Amount of total determiners: {}".format(determinerCount))
        print("Amount of demonstrative determiners: {}".format(demonstrativeDeterminerCount))
        print("Proportion of demonstrative determinters to total determiners: {}".format(demonstrativeDeterminerCount/determinerCount))