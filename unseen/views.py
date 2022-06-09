# Import render module from django
from django.shortcuts import render
from django.template.response import TemplateResponse

from unseen.gallery.models import Photo

def home_view(request):
    return render(request, "home/home.html")

def about_artist_view(request):
    return render(request, "about/about_artist.html")

def about_show_view(request):
    return render(request, "about/about_show.html")

def conversation_home_view(request):
    return TemplateResponse(request, 'conversation/conversation_home.html', {'photos': Photo.objects.all()})
