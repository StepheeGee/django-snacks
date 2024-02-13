from django.shortcuts import render

def home(request):
    return render(request, 'snacks/home.html')

def about(request):
    return render(request, 'snacks/about.html')
