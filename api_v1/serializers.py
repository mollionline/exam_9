from rest_framework import serializers
from webapp.models import Photo, ChoosePhoto
from django.contrib.auth import get_user_model


class PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True, required=False)

    class Meta:
        model = Photo
        fields = ['id', 'photo', 'sign', 'created_at', 'author']
        read_only_fields = ['id']


class ChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoosePhoto
        fields = ['id', 'photo_id', 'author_id']
        read_only_fields = ['id']
