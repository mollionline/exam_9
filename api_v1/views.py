from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Photo, ChoosePhoto
from api_v1.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ChoosePhotoAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    model = ChoosePhoto

    def post(self, request, *args, **kwargs):
        photo_pk = kwargs.get('pk')
        photo = get_object_or_404(Photo, pk=photo_pk)
        print(photo)
        if not self.model.objects.filter(photo_id=photo_pk, author_id=self.request.user.pk):
            self.model.objects.create(photo_id=photo_pk, author_id=self.request.user.pk)
            photo.save()
            return JsonResponse({'choosed': '+'})
        else:
            photo.save()
            self.model.objects.filter(photo_id=photo_pk, author_id=self.request.user.pk).delete()
            return JsonResponse({'choosed': '-'})
