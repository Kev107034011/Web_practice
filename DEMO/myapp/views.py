from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def sayhello(request,username):
    now = datetime.now()
    return render(request,'hello.html',locals()) #locals 包含 now 和 username 變數

def showimg(request,username):
    now = datetime.now()
    return render(request,'Show_img.html',locals()) #locals 包含 now 和 username 變數

