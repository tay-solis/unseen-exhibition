from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from unseen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/artist/', views.about_artist_view, name='about_artist'),
    path('about/show/', views.about_show_view, name='about_artist'),
    path('conversation/', views.conversation_home_view, name='conversation_home'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('gallery/', include('unseen.gallery.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
