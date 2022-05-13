from asyncio.windows_events import NULL
from email.mime import image
from tkinter.tix import InputOnly
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import os
# Create your views here.

def index(request):
    if request.method=='POST':
      if (request.POST.get('send')=="send"):
        username1= request.POST.get('username')
        password1= request.POST.get('password')
        ident1= request.POST.get('indenti')
        img = request.FILES.get('image')
        print(username1+"\n\n")
        data=Etudiant(username=username1,password=password1,indenti=ident1,image=img)
        data.save()
    return render(request , 'pages/index.html')
