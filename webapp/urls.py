from django.urls import path
from webapp.views.photo_views import (DetailPhotoView, DeletePhotoView,
                                      CreatePhotoView, ListPhotoView,
                                      UpdatePhotoView, ChoosePhotoView)

urlpatterns = []

photo_urls = [
    path('', ListPhotoView.as_view(), name='list_photo'),
    path('photo/<int:pk>', DetailPhotoView.as_view(), name='detail_photo'),
    path('photo/<int:pk>/delete', DeletePhotoView.as_view(), name='delete_photo'),
    path('photo/<int:pk>/update', UpdatePhotoView.as_view(), name='update_photo'),
    path('photo/add/', CreatePhotoView.as_view(), name='create_photo'),
    path('photo/<int:pk>/choose', ChoosePhotoView.as_view(), name='choose_photo')
]

urlpatterns += photo_urls
