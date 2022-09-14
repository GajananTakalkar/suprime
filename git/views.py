from html.entities import name2codepoint
from tracemalloc import start
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from git.models import Contacts
import webbrowser as wb
from dateutil.parser import parse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect








# Create your views here.
def index(request):
    
     return render(request,'suprime.html')

def about(request):
    
    return render (request,"about.html")

def services(request):
    return HttpResponse (" services of World Automation-WE AUTOMATE")

def contactus(request):

    if request.method =="POST":
        
        name= request.POST.get('name')
        Addr= request.POST.get('Addr')
        mobile=request.POST.get('mobile')
        mail=request.POST.get('mail')
        Inquiry=request.POST.get('Inquiry')
        print(name)
        pq= Contacts(name=name,Addr=Addr,mobile=mobile,mail=mail,Inquiry=Inquiry )  #'2022/04/04 12:16:03'
        Contacts.save(pq)
    
    return render (request,"contactus.html")

def gitplayer(request):
    
    return render (request,"gitplayer.html")

def CQM(request):
    
    return render (request,"CQM.html")

def EANDI(request):
    
    return render (request,"EANDI.html")

def LA(request):
    
    return render (request,"LA.html")

def MFPW(request):
    
    return render (request,"MFPW.html")

def STPM(request):
    
    return render (request,"STPM.html")
def PLC(request):
    
    return render (request,"PLC.html")





