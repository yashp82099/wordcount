from django.http import HttpResponse
from django.shortcuts import render
import operator

import wordcount

def home(request):
    return render(request,'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()

    wordcout = {}
    for word in wordlist:
        if word in wordcout:
            wordcout[word] += 1 
        else:
            wordcout[word] = 1
    wordcout = wordcout.items()
    wordcount1 = sorted(wordcout, key=operator.itemgetter(1), reverse=True)
    
    return render(request,'count.html', {'fulltext': fulltext, 'count': len(wordlist),'wordcout': wordcount1})