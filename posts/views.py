from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [1,5,2,5,7,7,4]

def list_posts(request):
    return render(request,'feed.html',{'posts':posts})

