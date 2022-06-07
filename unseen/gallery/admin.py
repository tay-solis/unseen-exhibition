from django.contrib import admin

from .models import Photo, Response


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.display(description='Name', ordering='first_name')
def response_name(obj):
    return ("%s %s." % (obj.first_name, obj.last_name[0]))

@admin.display(description='Photo')
def photo_name(obj):
    if obj.photo.name:
        return obj.photo.name
    return None

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (response_name, photo_name)
