from django.shortcuts import render
#from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def remoiseli(request):
    return render(request, 'remoiseli.html')    

def orellhuerzeler(request):
    return render(request, 'orellhuerzeler.html')  

def janhuerzeler(request):
    return render(request, 'janhuerzeler.html')  

def natefrank(request):
    return render(request, 'natefrank.html')  