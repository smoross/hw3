print('Samantha Moross''\n''Project 3''\n''Section 002: Wednesday 5:30-6:30 pm''\n''Madlib')

print('-----------')

# A) Madlib: madlibhw3.py

import nltk
import random

from nltk import word_tokenize, sent_tokenize
from nltk.corpus import gutenberg 

debug = False

if debug:
	print ("Getting information from text2...\n")

text2 = "austen-sense.txt"
f = open(text2, 'r')
para = f.read() #reads through the lines of text

tokens = nltk.word_tokenize(para)

tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PRP":"Preposition"}
#Added preposition
substitution_probabilities = {"NN":.15,"NNS":.10,"VB":.10,"JJ":.10,"PRP":.10} #probabilities added
#Nouns are 15% likely to be asked, and the rest are 10%

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

sent = ''
for word in para.split()[:150]:
	x = spaced(word)
	sent = sent + x
print (sent) #prints the first 150 words of the original text2

final_words = []
count = 0

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))
		count += 1
		if count == 10: #User imports 10 words
			break
		else:
			continue

sent2 = ''
final_text = "".join(final_words)
for words in final_text.split()[:150]:
	word = spaced(words)
	sent2 = sent2 + word
print(sent2) #print the changed words from text2


