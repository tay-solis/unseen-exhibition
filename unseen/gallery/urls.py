from django.urls import path

from .views import PhotoListView, PhotoView, PhotoConversationView, PhotoListApiView, PhotoApiView

urlpatterns = [
    path("<slug:slug>/conversation/", PhotoConversationView.as_view(), name="photo_convo"),
    path("api/", PhotoListApiView.as_view(), name="photo_list_api"),
    path("api/<slug:slug>/", PhotoApiView.as_view(), name="photo_api"),
    path("<slug:slug>/", PhotoView.as_view(), name="gallery"),
    path("", PhotoListView.as_view(), name="gallery"),
]