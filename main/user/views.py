from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import UserSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from .models import User
# Create your views here.

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()

        return Response({
            'user': UserSerializer(user,context=self.get_serializer_context()).data,
        })


@api_view(['GET']) # FBVs of List API View 
def user_home(request, *args,**kwargs):
    qs = User.objects.all()
    data = UserSerializer(qs,many=True).data
    return Response(data)
