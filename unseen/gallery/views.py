from django.shortcuts import render
from django.views.generic import ListView, DetailView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Photo
from .serializers import PhotoSerializer

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


class PhotoListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all photos
        '''
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
