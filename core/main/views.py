import re
from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    return render(request, 'index.html')

def result(request):
    number=int(request.POST['number'])
    
    def fibonacci(number):
        res = 0
        if number < 0:
            res = 'noooo'
        elif number == 0:
            res = 0
        elif number == 1 or number == 2:
            res = 1
        else:
            res = fibonacci(number-1) + fibonacci(number-2)
        return res
    res = fibonacci(number)

    return render(request, 'result.html', {'res' : res})
    
    
        
