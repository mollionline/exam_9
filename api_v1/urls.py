from django.urls import path, include
from rest_framework import routers
from api_v1 import views
from rest_framework.authtoken.views import obtain_auth_token
from api_v1.views import PhotoViewSet, LogoutView, ChoosePhotoAPIView

router = routers.DefaultRouter()
router.register(r'photos', viewset=PhotoViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('choose/<int:pk>/', views.ChoosePhotoAPIView.as_view(), name='choose_photo')
]
