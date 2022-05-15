from multiprocessing import context
import re
from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, About



def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context=context)

def about(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'about.html', context=context)


    
    
        
