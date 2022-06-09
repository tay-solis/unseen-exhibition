from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Photo

# Create your views here.
class PhotoListView(ListView):
    model = Photo
    template_name = "gallery/gallery.html"

# Create your views here.
class PhotoConversationView(DetailView):
    model = Photo
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = "conversation/conversation_photo_page.html"
