from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list_posts():
    posts = [1,5,2,5,7,7,4]
    