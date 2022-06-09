from django.urls import path

from .views import PhotoListView, PhotoConversationView

urlpatterns = [
    path("<slug:slug>/conversation/", PhotoConversationView.as_view(), name="photo_convo"),
    path("", PhotoListView.as_view(), name="gallery"),
]