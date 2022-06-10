from django.urls import path

from .views import PhotoListView, PhotoConversationView, PhotoListApiView

urlpatterns = [
    path("<slug:slug>/conversation/", PhotoConversationView.as_view(), name="photo_convo"),
    path("api/", PhotoListApiView.as_view(), name="photo_list_api"),
    path("", PhotoListView.as_view(), name="gallery"),
]