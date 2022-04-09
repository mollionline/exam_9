from django.urls import path
from accounts.views import (LoginView,
                            LogoutView,
                            RegisterView,
                            UserDetailView)

urlpatterns = []

accounts_urls = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_page')
]

urlpatterns += accounts_urls
