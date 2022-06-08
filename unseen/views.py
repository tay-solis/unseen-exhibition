# Import render module from django
from django.shortcuts import render

def home_view(request):
    return render(request, "home/home.html")

def about_artist_view(request):
    return render(request, "about/about_artist.html")

def about_show_view(request):
    return render(request, "about/about_show.html")
