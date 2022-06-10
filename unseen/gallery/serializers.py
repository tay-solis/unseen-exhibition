from rest_framework import serializers

from .models import Photo, Response


class PhotoSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=256)
  description = serializers.CharField(max_length=256)
  url = serializers.URLField(max_length=256)
  photo = serializers.ImageField()
  conversation_url = serializers.SerializerMethodField()

  def conversation_url(self, obj):
    return obj.get_conversation_url()

  class Meta:
    model = Photo
    fields = '__all__'
