from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):

    return render(request, 'home.html',{'helothere':'Ficaria feliz se sim'})

def about(request):

    return render(request,'about.html')

def count(request):

    fulltext = request.GET['fulltext']
    fulltext1 = fulltext.lower()
    wordlist = fulltext1.split()

    worddicionary = {}
    for word in wordlist:
        if word in worddicionary:
            worddicionary[word] += 1
        else:
            worddicionary[word] = 1

    wordsorted = sorted(worddicionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'wordsorted': wordsorted})




'''from django.http import H
def home(request):

    return HttpResponse("Hello")'''
