from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Photo, ResponseForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]

        form = ResponseForm()
        photo = get_object_or_404(Photo, slug=slug)
        comments = photo.comments.all()

        context['photo'] = photo
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        from .models import Response
        form = ResponseForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        photo= Photo.objects.filter(slug=self.kwargs['slug'])[0]
        comments = photo.comments.all()

        context['photo'] = photo
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            response = form.cleaned_data['response']
            consent_to_share = form.cleaned_data['consent_to_share']

            response = Response.objects.create(
                first_name=first_name, last_name=last_name,
                email=email, response=response,
                consent_to_share=consent_to_share, photo=photo,
                featured=False
            )

            form = ResponseForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


class PhotoListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all photos
        '''
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
