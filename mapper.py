#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
   # make lower case
    line = line.lower()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in line:
      if char not in punctuations:
       no_punct = no_punct + char 
    # split the line into words; splits on any whitespace
    words = no_punct.split()
    stopwords = set(['the' , 'and' ])
    # output tuples (word, 1) in tab-delimited format
    for word in words:
      if word not in stopwords:
       print '%s\t%s' % (word, "1")

    
