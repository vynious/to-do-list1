from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('',views.user_home, name='home')
]