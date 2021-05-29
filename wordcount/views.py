from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(self):
    return render(self, 'home.html', {"introduction":"Integrating Python with HTML for first time"})

def count(self):
    enteredtext = self.GET['fulltext']
    textlist = enteredtext.split()
    count = len(enteredtext.split())
    wordcount = {}
    for word in textlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    sortedword = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    return render(self, 'count.html', {'count':count,"enteredtext":enteredtext,"sortedword":sortedword})

def login(self):
    return HttpResponse("Will provide you a login page soon")

def about(self):
    return HttpResponse("This Website is created by Himanshu Tak on 23/5/20201 with purpose of learning web designing with help of python and django")
