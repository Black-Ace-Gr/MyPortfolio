from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "gregory_otieno_ace/home.html")