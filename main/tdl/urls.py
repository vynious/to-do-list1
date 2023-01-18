from django.urls import path
from . import views


urlpatterns = [
    path('', views.TDLListAPIView.as_view()),
    path('<int:pk>/',views.TDLDetailAPIView.as_view()),
    path('<int:pk>/update/',views.TDLUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.TDLDestroyAPIView.as_view()),
    path('create/',views.TDLCreateAPIView.as_view()),
]
   