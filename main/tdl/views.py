from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, permissions, authentication
from .models import ToDoList, User
from .serializers import TDLSerializer
from django.views.generic.edit import CreateView
from rest_framework.views import APIView

class TDLListAPIView(generics.ListAPIView):
    queryset = ToDoList.objects.all()
    serializer_class= TDLSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
 
class TDLCreateAPIView(generics.CreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TDLSerializer
    def perform_create(self, serializer):
  
        return super().perform_create(serializer)

class TDLDetailAPIView(generics.RetrieveAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TDLSerializer

class TDLUpdateAPIView(generics.UpdateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TDLDetailAPIView
    lookup_field = 'pk'
    def perform_update(self, serializer):
        return super().perform_update(serializer)

class TDLDestroyAPIView(generics.DestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TDLCreateAPIView
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

