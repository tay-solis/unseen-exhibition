from rest_framework import serializers

from .models import Photo, Response


class PhotoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=256)
    slug = serializers.CharField(max_length=256)
    url = serializers.URLField(max_length=256)
    photo = serializers.ImageField()
    conversation_url = serializers.SerializerMethodField()
    previous_photo_slug = serializers.SerializerMethodField()
    next_photo_slug = serializers.SerializerMethodField()

    def get_conversation_url(self, obj):
        return obj.get_conversation_url()

    def get_previous_photo_slug(self, obj):
        return obj.get_previous_photo_slug()

    def get_next_photo_slug(self, obj):
        return obj.get_next_photo_slug()

    class Meta:
        model = Photo
        fields = ('name', 'description', 'slug', 'url', 'photo',
                  'conversation_url', 'previous_photo_slug', 'next_photo_slug')
